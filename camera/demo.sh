# /usr/local/tango/bin/tango_admin --add-server CameraDevice/camera1 CameraDevice my/home/camera01

# <exec/inst> - 这似乎代表你要添加的服务器的可执行文件或实例。这可能是可执行文件名称和实例标识符的组合。
# <class> - 这是服务器的类别。它指定了服务器将提供或管理的服务类型。
# <dev list> - 这是服务器将管理或与之关联的设备列表，需要用逗号分隔。

python3 CameraDevice.py camera1

sudo /usr/local/tango/bin/tango restart


jyj@edge2:~/tango/camera$ sudo v4l2-ctl --list-devices
[sudo] password for jyj: 
UVC Camera (046d:0825) (usb-0000:00:14.0-1):
        /dev/video0
        /dev/video1
        /dev/media0
