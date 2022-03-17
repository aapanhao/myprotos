# 安装与学习grpc
    官方文档：https://grpc.io/docs/languages/python/quickstart/
    推荐中文文档：https://doc.oschina.net/grpc?t=58008

# 第一步：先写proto文件
    1、定义服务
    2、定义提供的方法（参数与返回的消息类型） 与 消息类型（message类型）

# 第二步：python run_codegen.py

# 第三步：写服务端代码
    1、写服务类，继承_grpc下的MyHelloReplyServicer；
    2、实现rpc方法，返回.proto中指定类型
    3、起服务端的服务，将服务类和grpc的server，指定地址与端口

# 第四步：写客户端代码
    1、建立grpc的channel，指定地址与端口
    2、建立stub - 存根
    3、使用存根，调用请求的方法与指定的参数

# 第五步：更好的代码
    1、组织代码
    2、尝试异步

# 百度脑图：http://naotu.baidu.com/file/77adbd7861ad271174b5e7a2b319dc91?token=043c4efa59432ac0