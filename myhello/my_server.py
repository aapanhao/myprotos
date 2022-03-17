import grpc
from concurrent import futures
from myhello_pb2_grpc import MyHelloReplyServicer, add_MyHelloReplyServicer_to_server
from myhello_pb2 import Reply


# 实现服务类，继承Servicer
class MyServer(MyHelloReplyServicer):

    def GetReply(self, request, context):
        msg = "hello " + request.name
        # 返回指定的类型
        return Reply(msg=msg)


if __name__ == '__main__':
    # grpc的server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 将自定义Server和grpc的server放入
    add_MyHelloReplyServicer_to_server(MyServer(), server)
    # 启动
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
