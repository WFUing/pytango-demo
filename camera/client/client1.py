from tango import DeviceProxy, DevFailed, EventType

def on_camera_status_change(event):
    if event.err:
        print("接收事件时发生错误:", event.errors)
    else:
        print("摄像头状态变化:", event.attr_value.value)

def take_picture(device_name):
    try:
        device_proxy = DeviceProxy(device_name)
        device_proxy.set_timeout_millis(100000)
        
        evt_id = device_proxy.subscribe_event("CameraStatus", EventType.CHANGE_EVENT, on_camera_status_change)
        
        device_proxy.command_inout("TakePicture")
        
        print("拍照命令已发送")
        input("按 Enter 键继续...\n")
        
        device_proxy.unsubscribe_event(evt_id)
        
    except DevFailed as e:
        print("拍照失败:", e)

if __name__ == "__main__":
    device_name = "my/home/camera01"
    take_picture(device_name)
