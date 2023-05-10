# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/book/manager.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19protos/book/manager.proto\x12\x0c\x62ook_manager\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"n\n\x11\x43reateBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x11\n\tbook_name\x18\x02 \x01(\t\x12\x13\n\x0b\x62ook_author\x18\x03 \x01(\t\x12\x11\n\tbook_desc\x18\x04 \x01(\t\x12\x10\n\x08\x62ook_url\x18\x05 \x01(\t\"!\n\x11\x44\x65leteBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"\xcc\x01\n\rGetBookResult\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x11\n\tbook_name\x18\x02 \x01(\t\x12\x13\n\x0b\x62ook_author\x18\x03 \x01(\t\x12\x11\n\tbook_desc\x18\x04 \x01(\t\x12\x10\n\x08\x62ook_url\x18\x05 \x01(\t\x12/\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"s\n\x12GetBookListRequest\x12\x39\n\x10next_create_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x12\r\n\x05limit\x18\x02 \x01(\x05\x42\x13\n\x11_next_create_time\"@\n\x11GetBookListResult\x12+\n\x06result\x18\x01 \x03(\x0b\x32\x1b.book_manager.GetBookResult2\xb8\x02\n\x0b\x42ookManager\x12\x46\n\x0b\x63reate_book\x12\x1f.book_manager.CreateBookRequest\x1a\x16.google.protobuf.Empty\x12\x46\n\x0b\x64\x65lete_book\x12\x1f.book_manager.DeleteBookRequest\x1a\x16.google.protobuf.Empty\x12\x45\n\x08get_book\x12\x1c.book_manager.GetBookRequest\x1a\x1b.book_manager.GetBookResult\x12R\n\rget_book_list\x12 .book_manager.GetBookListRequest\x1a\x1f.book_manager.GetBookListResultb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.book.manager_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEBOOKREQUEST._serialized_start=105
  _CREATEBOOKREQUEST._serialized_end=215
  _DELETEBOOKREQUEST._serialized_start=217
  _DELETEBOOKREQUEST._serialized_end=250
  _GETBOOKREQUEST._serialized_start=252
  _GETBOOKREQUEST._serialized_end=282
  _GETBOOKRESULT._serialized_start=285
  _GETBOOKRESULT._serialized_end=489
  _GETBOOKLISTREQUEST._serialized_start=491
  _GETBOOKLISTREQUEST._serialized_end=606
  _GETBOOKLISTRESULT._serialized_start=608
  _GETBOOKLISTRESULT._serialized_end=672
  _BOOKMANAGER._serialized_start=675
  _BOOKMANAGER._serialized_end=987
# @@protoc_insertion_point(module_scope)