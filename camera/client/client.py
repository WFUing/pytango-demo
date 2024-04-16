from tango import DeviceProxy, DevFailed

def take_picture(device_name):
    try:
        # 创建一个设备代理
        device_proxy = DeviceProxy(device_name)
        device_proxy.set_timeout_millis(100000) 

        # 调用 TakePicture 命令
        device_proxy.command_inout("TakePicture")
        
        print("拍照命令已发送")
    except DevFailed as e:
        print("拍照失败:", e)

if __name__ == "__main__":
    # 设备名称，确保与服务器上的名称匹配
    device_name = "my/home/camera01"
    take_picture(device_name)
