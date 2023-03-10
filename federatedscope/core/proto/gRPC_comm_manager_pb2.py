# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gRPC_comm_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='gRPC_comm_manager.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=
    b'\n\x17gRPC_comm_manager.proto\"n\n\x0eMessageRequest\x12%\n\x03msg\x18\x01 \x03(\x0b\x32\x18.MessageRequest.MsgEntry\x1a\x35\n\x08MsgEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.MsgValue:\x02\x38\x01\"\xac\x01\n\x08MsgValue\x12\x1e\n\nsingle_msg\x18\x01 \x01(\x0b\x32\x08.mSingleH\x00\x12\x1a\n\x08list_msg\x18\x02 \x01(\x0b\x32\x06.mListH\x00\x12\x30\n\x12\x64ict_msg_stringkey\x18\x03 \x01(\x0b\x32\x12.mDict_keyIsStringH\x00\x12*\n\x0f\x64ict_msg_intkey\x18\x04 \x01(\x0b\x32\x0f.mDict_keyIsIntH\x00\x42\x06\n\x04type\"R\n\x07mSingle\x12\x15\n\x0b\x66loat_value\x18\x01 \x01(\x02H\x00\x12\x13\n\tint_value\x18\x02 \x01(\x05H\x00\x12\x13\n\tstr_value\x18\x03 \x01(\tH\x00\x42\x06\n\x04type\"&\n\x05mList\x12\x1d\n\nlist_value\x18\x01 \x03(\x0b\x32\t.MsgValue\"\x87\x01\n\x11mDict_keyIsString\x12\x35\n\ndict_value\x18\x01 \x03(\x0b\x32!.mDict_keyIsString.DictValueEntry\x1a;\n\x0e\x44ictValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.MsgValue:\x02\x38\x01\"\x81\x01\n\x0emDict_keyIsInt\x12\x32\n\ndict_value\x18\x01 \x03(\x0b\x32\x1e.mDict_keyIsInt.DictValueEntry\x1a;\n\x0e\x44ictValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.MsgValue:\x02\x38\x01\"\x1e\n\x0fMessageResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t2F\n\x10gRPCComServeFunc\x12\x32\n\x0bsendMessage\x12\x0f.MessageRequest\x1a\x10.MessageResponse\"\x00\x62\x06proto3'
)

_MESSAGEREQUEST_MSGENTRY = _descriptor.Descriptor(
    name='MsgEntry',
    full_name='MessageRequest.MsgEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='MessageRequest.MsgEntry.key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='MessageRequest.MsgEntry.value',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=84,
    serialized_end=137,
)

_MESSAGEREQUEST = _descriptor.Descriptor(
    name='MessageRequest',
    full_name='MessageRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='msg',
            full_name='MessageRequest.msg',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[
        _MESSAGEREQUEST_MSGENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=27,
    serialized_end=137,
)

_MSGVALUE = _descriptor.Descriptor(
    name='MsgValue',
    full_name='MsgValue',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='single_msg',
            full_name='MsgValue.single_msg',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='list_msg',
            full_name='MsgValue.list_msg',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='dict_msg_stringkey',
            full_name='MsgValue.dict_msg_stringkey',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='dict_msg_intkey',
            full_name='MsgValue.dict_msg_intkey',
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name='type',
            full_name='MsgValue.type',
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[]),
    ],
    serialized_start=140,
    serialized_end=312,
)

_MSINGLE = _descriptor.Descriptor(
    name='mSingle',
    full_name='mSingle',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='float_value',
            full_name='mSingle.float_value',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='int_value',
            full_name='mSingle.int_value',
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='str_value',
            full_name='mSingle.str_value',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name='type',
            full_name='mSingle.type',
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[]),
    ],
    serialized_start=314,
    serialized_end=396,
)

_MLIST = _descriptor.Descriptor(
    name='mList',
    full_name='mList',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='list_value',
            full_name='mList.list_value',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=398,
    serialized_end=436,
)

_MDICT_KEYISSTRING_DICTVALUEENTRY = _descriptor.Descriptor(
    name='DictValueEntry',
    full_name='mDict_keyIsString.DictValueEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='mDict_keyIsString.DictValueEntry.key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='mDict_keyIsString.DictValueEntry.value',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=515,
    serialized_end=574,
)

_MDICT_KEYISSTRING = _descriptor.Descriptor(
    name='mDict_keyIsString',
    full_name='mDict_keyIsString',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='dict_value',
            full_name='mDict_keyIsString.dict_value',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[
        _MDICT_KEYISSTRING_DICTVALUEENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=439,
    serialized_end=574,
)

_MDICT_KEYISINT_DICTVALUEENTRY = _descriptor.Descriptor(
    name='DictValueEntry',
    full_name='mDict_keyIsInt.DictValueEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='mDict_keyIsInt.DictValueEntry.key',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='mDict_keyIsInt.DictValueEntry.value',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=647,
    serialized_end=706,
)

_MDICT_KEYISINT = _descriptor.Descriptor(
    name='mDict_keyIsInt',
    full_name='mDict_keyIsInt',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='dict_value',
            full_name='mDict_keyIsInt.dict_value',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[
        _MDICT_KEYISINT_DICTVALUEENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=577,
    serialized_end=706,
)

_MESSAGERESPONSE = _descriptor.Descriptor(
    name='MessageResponse',
    full_name='MessageResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='msg',
            full_name='MessageResponse.msg',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=708,
    serialized_end=738,
)

_MESSAGEREQUEST_MSGENTRY.fields_by_name['value'].message_type = _MSGVALUE
_MESSAGEREQUEST_MSGENTRY.containing_type = _MESSAGEREQUEST
_MESSAGEREQUEST.fields_by_name['msg'].message_type = _MESSAGEREQUEST_MSGENTRY
_MSGVALUE.fields_by_name['single_msg'].message_type = _MSINGLE
_MSGVALUE.fields_by_name['list_msg'].message_type = _MLIST
_MSGVALUE.fields_by_name[
    'dict_msg_stringkey'].message_type = _MDICT_KEYISSTRING
_MSGVALUE.fields_by_name['dict_msg_intkey'].message_type = _MDICT_KEYISINT
_MSGVALUE.oneofs_by_name['type'].fields.append(
    _MSGVALUE.fields_by_name['single_msg'])
_MSGVALUE.fields_by_name[
    'single_msg'].containing_oneof = _MSGVALUE.oneofs_by_name['type']
_MSGVALUE.oneofs_by_name['type'].fields.append(
    _MSGVALUE.fields_by_name['list_msg'])
_MSGVALUE.fields_by_name[
    'list_msg'].containing_oneof = _MSGVALUE.oneofs_by_name['type']
_MSGVALUE.oneofs_by_name['type'].fields.append(
    _MSGVALUE.fields_by_name['dict_msg_stringkey'])
_MSGVALUE.fields_by_name[
    'dict_msg_stringkey'].containing_oneof = _MSGVALUE.oneofs_by_name['type']
_MSGVALUE.oneofs_by_name['type'].fields.append(
    _MSGVALUE.fields_by_name['dict_msg_intkey'])
_MSGVALUE.fields_by_name[
    'dict_msg_intkey'].containing_oneof = _MSGVALUE.oneofs_by_name['type']
_MSINGLE.oneofs_by_name['type'].fields.append(
    _MSINGLE.fields_by_name['float_value'])
_MSINGLE.fields_by_name[
    'float_value'].containing_oneof = _MSINGLE.oneofs_by_name['type']
_MSINGLE.oneofs_by_name['type'].fields.append(
    _MSINGLE.fields_by_name['int_value'])
_MSINGLE.fields_by_name[
    'int_value'].containing_oneof = _MSINGLE.oneofs_by_name['type']
_MSINGLE.oneofs_by_name['type'].fields.append(
    _MSINGLE.fields_by_name['str_value'])
_MSINGLE.fields_by_name[
    'str_value'].containing_oneof = _MSINGLE.oneofs_by_name['type']
_MLIST.fields_by_name['list_value'].message_type = _MSGVALUE
_MDICT_KEYISSTRING_DICTVALUEENTRY.fields_by_name[
    'value'].message_type = _MSGVALUE
_MDICT_KEYISSTRING_DICTVALUEENTRY.containing_type = _MDICT_KEYISSTRING
_MDICT_KEYISSTRING.fields_by_name[
    'dict_value'].message_type = _MDICT_KEYISSTRING_DICTVALUEENTRY
_MDICT_KEYISINT_DICTVALUEENTRY.fields_by_name['value'].message_type = _MSGVALUE
_MDICT_KEYISINT_DICTVALUEENTRY.containing_type = _MDICT_KEYISINT
_MDICT_KEYISINT.fields_by_name[
    'dict_value'].message_type = _MDICT_KEYISINT_DICTVALUEENTRY
DESCRIPTOR.message_types_by_name['MessageRequest'] = _MESSAGEREQUEST
DESCRIPTOR.message_types_by_name['MsgValue'] = _MSGVALUE
DESCRIPTOR.message_types_by_name['mSingle'] = _MSINGLE
DESCRIPTOR.message_types_by_name['mList'] = _MLIST
DESCRIPTOR.message_types_by_name['mDict_keyIsString'] = _MDICT_KEYISSTRING
DESCRIPTOR.message_types_by_name['mDict_keyIsInt'] = _MDICT_KEYISINT
DESCRIPTOR.message_types_by_name['MessageResponse'] = _MESSAGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageRequest = _reflection.GeneratedProtocolMessageType(
    'MessageRequest',
    (_message.Message, ),
    {
        'MsgEntry': _reflection.GeneratedProtocolMessageType(
            'MsgEntry',
            (_message.Message, ),
            {
                'DESCRIPTOR': _MESSAGEREQUEST_MSGENTRY,
                '__module__': 'gRPC_comm_manager_pb2'
                # @@protoc_insertion_point(class_scope:MessageRequest.MsgEntry)
            }),
        'DESCRIPTOR': _MESSAGEREQUEST,
        '__module__': 'gRPC_comm_manager_pb2'
        # @@protoc_insertion_point(class_scope:MessageRequest)
    })
_sym_db.RegisterMessage(MessageRequest)
_sym_db.RegisterMessage(MessageRequest.MsgEntry)

MsgValue = _reflection.GeneratedProtocolMessageType(
    'MsgValue',
    (_message.Message, ),
    {
        'DESCRIPTOR': _MSGVALUE,
        '__module__': 'gRPC_comm_manager_pb2'
        # @@protoc_insertion_point(class_scope:MsgValue)
    })
_sym_db.RegisterMessage(MsgValue)

mSingle = _reflection.GeneratedProtocolMessageType(
    'mSingle',
    (_message.Message, ),
    {
        'DESCRIPTOR': _MSINGLE,
        '__module__': 'gRPC_comm_manager_pb2'
        # @@protoc_insertion_point(class_scope:mSingle)
    })
_sym_db.RegisterMessage(mSingle)

mList = _reflection.GeneratedProtocolMessageType(
    'mList',
    (_message.Message, ),
    {
        'DESCRIPTOR': _MLIST,
        '__module__': 'gRPC_comm_manager_pb2'
        # @@protoc_insertion_point(class_scope:mList)
    })
_sym_db.RegisterMessage(mList)

mDict_keyIsString = _reflection.GeneratedProtocolMessageType(
    'mDict_keyIsString',
    (_message.Message, ),
    {
        'DictValueEntry': _reflection.GeneratedProtocolMessageType(
            'DictValueEntry',
            (_message.Message, ),
            {
                'DESCRIPTOR': _MDICT_KEYISSTRING_DICTVALUEENTRY,
                '__module__': 'gRPC_comm_manager_pb2'
                # @@protoc_insertion_point(class_scope:mDict_keyIsString.DictValueEntry)
            }),
        'DESCRIPTOR': _MDICT_KEYISSTRING,
        '__module__': 'gRPC_comm_manager_pb2'
        # @@protoc_insertion_point(class_scope:mDict_keyIsString)
    })
_sym_db.RegisterMessage(mDict_keyIsString)
_sym_db.RegisterMessage(mDict_keyIsString.DictValueEntry)

mDict_keyIsInt = _reflection.GeneratedProtocolMessageType(
    'mDict_keyIsInt',
    (_message.Message, ),
    {
        'DictValueEntry': _reflection.GeneratedProtocolMessageType(
            'DictValueEntry',
            (_message.Message, ),
            {
                'DESCRIPTOR': _MDICT_KEYISINT_DICTVALUEENTRY,
                '__module__': 'gRPC_comm_manager_pb2'
                # @@protoc_insertion_point(class_scope:mDict_keyIsInt.DictValueEntry)
            }),
        'DESCRIPTOR': _MDICT_KEYISINT,
        '__module__': 'gRPC_comm_manager_pb2'
        # @@protoc_insertion_point(class_scope:mDict_keyIsInt)
    })
_sym_db.RegisterMessage(mDict_keyIsInt)
_sym_db.RegisterMessage(mDict_keyIsInt.DictValueEntry)

MessageResponse = _reflection.GeneratedProtocolMessageType(
    'MessageResponse',
    (_message.Message, ),
    {
        'DESCRIPTOR': _MESSAGERESPONSE,
        '__module__': 'gRPC_comm_manager_pb2'
        # @@protoc_insertion_point(class_scope:MessageResponse)
    })
_sym_db.RegisterMessage(MessageResponse)

_MESSAGEREQUEST_MSGENTRY._options = None
_MDICT_KEYISSTRING_DICTVALUEENTRY._options = None
_MDICT_KEYISINT_DICTVALUEENTRY._options = None

_GRPCCOMSERVEFUNC = _descriptor.ServiceDescriptor(
    name='gRPCComServeFunc',
    full_name='gRPCComServeFunc',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=740,
    serialized_end=810,
    methods=[
        _descriptor.MethodDescriptor(
            name='sendMessage',
            full_name='gRPCComServeFunc.sendMessage',
            index=0,
            containing_service=None,
            input_type=_MESSAGEREQUEST,
            output_type=_MESSAGERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_GRPCCOMSERVEFUNC)

DESCRIPTOR.services_by_name['gRPCComServeFunc'] = _GRPCCOMSERVEFUNC

# @@protoc_insertion_point(module_scope)
