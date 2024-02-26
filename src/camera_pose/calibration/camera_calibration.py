import numpy as np
import cv2
import glob

def calibrate_camera(chessboard_size, square_size, image_paths):
    """
    使用棋盤格進行相機校準。

    參數:
    - chessboard_size: 棋盤格的格數，格式為(rows, cols)。
    - square_size: 棋盤格每個方塊的實際尺寸。
    - image_paths: 包含棋盤格圖像的路徑列表。

    返回:
    - ret: 校準是否成功的布林值。
    - mtx: 相機內參矩陣。
    - dist: 畸變係數。
    - rvecs: 旋轉向量。
    - tvecs: 平移向量。
    """
    # 準備物體點，如(0,0,0), (1,0,0), (2,0,0) ...，假設棋盤格在XY平面上
    objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:chessboard_size[1], 0:chessboard_size[0]].T.reshape(-1, 2) * square_size

    objpoints = []  # 3d 點在真實世界中的坐標。
    imgpoints = []  # 2d 點在圖像平面上的坐標。

    for image_path in image_paths:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 尋找棋盤格角點
        ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)
        # 如果找到了，添加物體點，圖像點
        if ret:
            objpoints.append(objp)
            imgpoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    return ret, mtx, dist, rvecs, tvecs

# 使用示例
chessboard_size = (6, 9)  # 棋盤格大小
square_size = 0.025  # 棋盤格方塊的實際尺寸（米）
image_paths = glob.glob('path_to_calibration_images/*.jpg')  # 棋盤格圖像的路徑
ret, mtx, dist, rvecs, tvecs = calibrate_camera(chessboard_size, square_size, image_paths)

if ret:
    print("相機校準成功。")
    print("相機內參矩陣:\n", mtx)
    print("畸變係數:\n", dist)
else:
    print("相機校準失敗。")
