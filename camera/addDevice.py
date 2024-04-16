from tango import Database, DbDevInfo

# 假设Tango数据库运行在远程主机上，指定其地址和端口
# 例如，Tango数据库运行在192.168.1.100主机上的10000端口
# db_host = "192.168.1.100"
# db_port = "10000"
# db = Database(db_host, db_port)

db = Database()

# 创建服务器的定义
server_name = "CameraDevice/camera1"
device_class = "CameraDevice"
device_name = "my/home/camera01"

dev_info = DbDevInfo()
dev_info.name = device_name
dev_info._class = device_class
dev_info.server = server_name

# 向数据库添加服务器
db.add_device(dev_info)

print("服务器添加成功")
