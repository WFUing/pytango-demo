import threading
import time
from tango.server import Device, attribute, command, device_property
from tango import DevState, AttrWriteType
import cv2

class CameraDevice(Device):
    image_path = device_property(dtype=str, default_value="./temp/output.png")
    
    CameraStatus = attribute(label="CameraStatus", dtype=str, access=AttrWriteType.READ)
    
    def init_device(self):
        super().init_device()
        self.set_state(DevState.STANDBY)
        self._camera_status = "Ready"
        self.set_change_event("CameraStatus", True, False)
        # self.start_poll_attribute("CameraStatus", 1000)
        # 启动轮询线程
        self._polling_thread = threading.Thread(target=self._polling_loop)
        self._polling_thread.daemon = True  # 设置为守护线程，确保主程序退出时线程也会退出
        self._polling_thread.start()

    def _polling_loop(self):
        """后台线程定期触发 CameraStatus 属性的变更事件。"""
        while True:
            time.sleep(1)  # 每秒轮询一次
            self.push_change_event("CameraStatus", self._camera_status)

    def read_CameraStatus(self):
        return self._camera_status

    @command
    def TakePicture(self):
        self.set_state(DevState.RUNNING)
        self._camera_status = "Taking picture"
        self.push_change_event("CameraStatus", self._camera_status)
        try:
            self.capture_image(self.image_path)
            self._camera_status = "Ready"
            self.push_change_event("CameraStatus", self._camera_status)
            self.set_state(DevState.STANDBY)
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.set_status(str(e))

    @command
    def Stop(self):
        self.set_state(DevState.STANDBY)
    
    def capture_image(self, filename):
        cap = cv2.VideoCapture(0)  # 如果'/dev/video0'无法正常工作，请尝试使用0
        if not cap.isOpened():
            raise IOError("Cannot open webcam")
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(filename, frame)
        else:
            raise Exception("Failed to capture image")
        cap.release()

if __name__ == "__main__":
    CameraDevice.run_server()
