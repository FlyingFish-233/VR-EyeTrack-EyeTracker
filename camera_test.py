import cv2
import sys

def list_available_cameras(max_index=10):
    """列出所有可用的摄像头"""
    available_cameras = []
    
    for i in range(max_index):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap.isOpened():
            # 获取摄像头信息
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            # 尝试读取一帧来确认摄像头真正可用
            ret, frame = cap.read()
            cv2.imwrite(f'frame_{i}.jpg', frame)
            if ret:
                camera_info = {
                    'index': i,
                    'resolution': f"{width}x{height}",
                    'fps': fps,
                    'status': '工作正常'
                }
                available_cameras.append(camera_info)
                print(f"摄像头索引 {i}: {width}x{height}, FPS: {fps} - 工作正常")
            else:
                print(f"摄像头索引 {i}: 已检测到但无法读取图像")
            
            cap.release()
        else:
            print(f"摄像头索引 {i}: 不可用")
    
    return available_cameras

print("正在检测可用摄像头...")
cameras = list_available_cameras()

if cameras:
    print(f"\n找到 {len(cameras)} 个可用摄像头:")
    for cam in cameras:
        print(f"  索引 {cam['index']}: {cam['resolution']}, FPS: {cam['fps']}")
else:
    print("未找到可用摄像头")