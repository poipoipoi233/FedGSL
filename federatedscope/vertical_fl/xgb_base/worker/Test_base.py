import time

import numpy as np
import pandas as pd
import logging

logger = logging.getLogger(__name__)
from federatedscope.core.message import Message


class Test_base:
    def __init__(self, obj):
        self.client = obj
        self.client.register_handlers('test_data',
                                      self.callback_func_for_test_data)
        self.client.register_handlers('test_value',
                                      self.callback_func_for_test_value)
        self.client.register_handlers(
            'split_lr_for_test_data',
            self.callback_func_for_split_lr_for_test_data)
        self.client.register_handlers('LR', self.callback_func_for_LR)

    def callback_func_for_test_value(self, message: Message):
        self.test_y = message.content

    def callback_func_for_test_data(self, message: Message):
        self.test_x = message.content

        if self.client.own_label:
            self.test_z = np.zeros(self.test_x.shape[0])

            tree_num = 0
            self.test_for_root(tree_num)

    def test_for_root(self, tree_num):
        node_num = 0
        self.client.tree_list[tree_num][node_num].indicator = np.ones(
            self.test_x.shape[0])
        self.test_for_node(tree_num, node_num)

    def test_for_node(self, tree_num, node_num):
        if node_num >= 2**self.client.max_tree_depth - 1:
            if tree_num + 1 == self.client.num_of_trees:
                metric = self.client.ls.metric(self.test_y, self.test_z)
                loss = self.client.ls.loss(self.test_y, self.test_z)
                metrics = {
                    'test_loss': loss,
                    'test_acc': metric[1],
                    'test_total': len(self.test_y)
                }

                self.client.comm_manager.send(
                    Message(msg_type='test_result',
                            sender=self.client.ID,
                            state=self.client.state,
                            receiver=self.client.server_id,
                            content=metrics))

            else:
                self.test_for_root(tree_num + 1)
        elif self.client.tree_list[tree_num][node_num].weight:
            self.test_z += self.client.tree_list[tree_num][
                node_num].indicator * self.client.tree_list[tree_num][
                    node_num].weight
            self.test_for_node(tree_num, node_num + 1)
        elif self.client.tree_list[tree_num][node_num].member:
            self.client.comm_manager.send(
                Message(
                    msg_type='split_lr_for_test_data',
                    sender=self.client.ID,
                    state=self.client.state,
                    receiver=self.client.tree_list[tree_num][node_num].member,
                    content=(tree_num, node_num)))
        else:
            self.test_for_node(tree_num, node_num + 1)

    def callback_func_for_split_lr_for_test_data(self, message: Message):
        tree_num, node_num = message.content
        feature_idx = self.client.tree_list[tree_num][node_num].feature_idx
        feature_value = self.client.tree_list[tree_num][node_num].feature_value
        L, R = self.client.split_for_lr(self.test_x[:, feature_idx],
                                        feature_value)
        self.client.comm_manager.send(
            Message(msg_type='LR',
                    sender=self.client.ID,
                    state=self.client.state,
                    receiver=self.client.num_of_parties,
                    content=(tree_num, node_num, L, R)))

    def callback_func_for_LR(self, message: Message):
        tree_num, node_num, L, R = message.content
        self.client.tree_list[tree_num][2 * node_num +
                                        1].indicator = self.client.tree_list[
                                            tree_num][node_num].indicator * L
        self.client.tree_list[tree_num][2 * node_num +
                                        2].indicator = self.client.tree_list[
                                            tree_num][node_num].indicator * R
        self.test_for_node(tree_num, node_num + 1)
