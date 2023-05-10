"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CreateBookRequest(google.protobuf.message.Message):
    """create book by admin"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISBN_FIELD_NUMBER: builtins.int
    BOOK_NAME_FIELD_NUMBER: builtins.int
    BOOK_AUTHOR_FIELD_NUMBER: builtins.int
    BOOK_DESC_FIELD_NUMBER: builtins.int
    BOOK_URL_FIELD_NUMBER: builtins.int
    isbn: builtins.str
    book_name: builtins.str
    book_author: builtins.str
    book_desc: builtins.str
    book_url: builtins.str
    def __init__(
        self,
        *,
        isbn: builtins.str = ...,
        book_name: builtins.str = ...,
        book_author: builtins.str = ...,
        book_desc: builtins.str = ...,
        book_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["book_author", b"book_author", "book_desc", b"book_desc", "book_name", b"book_name", "book_url", b"book_url", "isbn", b"isbn"]) -> None: ...

global___CreateBookRequest = CreateBookRequest

@typing_extensions.final
class DeleteBookRequest(google.protobuf.message.Message):
    """delete book by admin"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISBN_FIELD_NUMBER: builtins.int
    isbn: builtins.str
    def __init__(
        self,
        *,
        isbn: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["isbn", b"isbn"]) -> None: ...

global___DeleteBookRequest = DeleteBookRequest

@typing_extensions.final
class GetBookRequest(google.protobuf.message.Message):
    """get book by user"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISBN_FIELD_NUMBER: builtins.int
    isbn: builtins.str
    def __init__(
        self,
        *,
        isbn: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["isbn", b"isbn"]) -> None: ...

global___GetBookRequest = GetBookRequest

@typing_extensions.final
class GetBookResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISBN_FIELD_NUMBER: builtins.int
    BOOK_NAME_FIELD_NUMBER: builtins.int
    BOOK_AUTHOR_FIELD_NUMBER: builtins.int
    BOOK_DESC_FIELD_NUMBER: builtins.int
    BOOK_URL_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    isbn: builtins.str
    book_name: builtins.str
    book_author: builtins.str
    book_desc: builtins.str
    book_url: builtins.str
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        isbn: builtins.str = ...,
        book_name: builtins.str = ...,
        book_author: builtins.str = ...,
        book_desc: builtins.str = ...,
        book_url: builtins.str = ...,
        create_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        update_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time", b"create_time", "update_time", b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["book_author", b"book_author", "book_desc", b"book_desc", "book_name", b"book_name", "book_url", b"book_url", "create_time", b"create_time", "isbn", b"isbn", "update_time", b"update_time"]) -> None: ...

global___GetBookResult = GetBookResult

@typing_extensions.final
class GetBookListRequest(google.protobuf.message.Message):
    """get book list by user"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NEXT_CREATE_TIME_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    @property
    def next_create_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    limit: builtins.int
    def __init__(
        self,
        *,
        next_create_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        limit: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_next_create_time", b"_next_create_time", "next_create_time", b"next_create_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_next_create_time", b"_next_create_time", "limit", b"limit", "next_create_time", b"next_create_time"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_next_create_time", b"_next_create_time"]) -> typing_extensions.Literal["next_create_time"] | None: ...

global___GetBookListRequest = GetBookListRequest

@typing_extensions.final
class GetBookListResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetBookResult]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[global___GetBookResult] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["result", b"result"]) -> None: ...

global___GetBookListResult = GetBookListResult
