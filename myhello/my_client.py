import grpc
import myhello_pb2_grpc
from myhello_pb2 import Name

if __name__ == '__main__':
    # grpc通道
    with grpc.insecure_channel('localhost:50051') as channel:
        # 建立stub - 存根
        stub = myhello_pb2_grpc.MyHelloReplyStub(channel)
        # 调用请求方法，指定参数类型
        response = stub.GetReply(Name(name="panhao"))
    print(response)
    print(response.msg)
