# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mail-service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12notification-service.proto\"\xaa\x01\n\x0fNotificationRequest\x12\x17\n\x0fnotification_id\x18\x01 \x01(\t\x12\x1a\n\x12notification_title\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65description\x18\x05 \x01(\t\x12\x10\n\x08\x64\x65\x61\x64username\x18\x06 \x01(\t\"\'\n\x10NotificationResponse\x12\x13\n\x0bsend_status\x18\x01 \x01(\x05\x32M\n\x0eAlertService\x12;\n\x14ScheduleNotification\x12\x10.NotificationRequest\x1a\x11.NotificationResponse\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'alert_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NotificationRequest._serialized_start=23
  _NotificationRequest._serialized_end=193
  _NotificationResponse._serialized_start=195
  _NotificationResponse._serialized_end=234
  _AlertService._serialized_start=236
  _AlertService._serialized_end=313
# @@protoc_insertion_point(module_scope)