import tango
from tango.server import Device, attribute, command
from miio.integrations.airpurifier.zhimi import airpurifier

class XiaomiAirPurifier(Device):
    # 定义Tango设备属性
    PowerStatus = attribute(label="Power Status", dtype=bool)
    LEDStatus = attribute(label="LED Status", dtype=bool)
    AirQualityIndex = attribute(label="Air Quality Index", dtype=int)

    def init_device(self):
        super().init_device()
        self.device = airpurifier.AirPurifier(ip="192.168.28.22", token="b08f61cbc5f5f5e867a5b8750c683831")
        print("Device initialized")

    @command
    def PowerOn(self):
        self.device.on()
        self.push_change_event("PowerStatus", True)

    @command
    def PowerOff(self):
        self.device.off()
        self.push_change_event("PowerStatus", False)

    @command(dtype_in=str)
    def SetLED(self, value):
        if value.lower() == "on":
            self.device.set_led(True)
            self.push_change_event("LEDStatus", True)
        elif value.lower() == "off":
            self.device.set_led(False)
            self.push_change_event("LEDStatus", False)
    
    # 定义获取设备状态的方法
    def read_PowerStatus(self):
        return self.device.get_properties(["power"])[0] == "on"

    def read_LEDStatus(self):
        return self.device.get_properties(["led"])[0] == "on"

    def read_AirQualityIndex(self):
        return int(self.device.get_properties(["aqi"])[0])

if __name__ == "__main__":
    XiaomiAirPurifier.run_server()
    