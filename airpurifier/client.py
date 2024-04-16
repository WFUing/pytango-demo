import tango

# 替换为你的设备名，格式通常是"域/家族/成员"
device_name = "my/home/airpurifier01"

# 创建设备代理
device_proxy = tango.DeviceProxy(device_name)

try:
    # 获取并打印所有属性名称
    attributes = device_proxy.get_attribute_list()
    print("Available attributes for device", device_name, ":")
    for attribute in attributes:
        print(attribute)
except tango.DevFailed as e:
    print("Error accessing device or retrieving attributes:", e)

# host_name = device_proxy.read_attribute("HostName").value
# ip_address = device_proxy.read_attribute("IPAddress").value

# print(f"Host Name: {host_name}, IP Address: {ip_address}")

# 调用PowerOn命令
# device_proxy.PowerOn()

# 调用PowerOff命令
# device_proxy.PowerOff() 

# # 调用SetLED命令，打开LED
# device_proxy.SetLED("on")

# # 调用SetLED命令，关闭LED
# device_proxy.SetLED("off")
