import tango

# 获取数据库对象
db = tango.Database()

# 现在你可以使用db对象进行查询和操作
devices = db.get_device_exported('*')
for device in devices:
    print(device)

# 获取所有服务器的列表
servers = db.get_server_list()

# 打印每个服务器及其实例
for server in servers:
    print(f"Server: {server}")
    # 获取并打印服务器的实例
    instances = db.get_server_class_list(server)
    for instance in instances:
        print(f"  Instance: {instance}")
