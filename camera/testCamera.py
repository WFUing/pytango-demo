import cv2

def capture_image(filename="output.png"):
    # 打开默认的摄像头
    cap = cv2.VideoCapture('/dev/video0')
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    # 设置分辨率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    # 读取一帧
    ret, frame = cap.read()
    if ret:
        # 保存图片
        cv2.imwrite(filename, frame)
    else:
        raise Exception("Failed to capture image")
    
    # 释放摄像头资源
    cap.release()

# 捕获并保存图片
capture_image("./temp/output.png")
