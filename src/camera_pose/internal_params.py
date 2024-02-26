class CameraInternalParams:
    def __init__(self, focal_length=None, principal_point=None, distortion_coeffs=None):
        self.focal_length = focal_length  # 焦距
        self.principal_point = principal_point  # 主點坐標（光學中心）
        self.distortion_coeffs = distortion_coeffs  # 畸變係數

    def set_params(self, focal_length, principal_point, distortion_coeffs):
        self.focal_length = focal_length
        self.principal_point = principal_point
        self.distortion_coeffs = distortion_coeffs

    def get_params(self):
        return self.focal_length, self.principal_point, self.distortion_coeffs

# 使用示例
if __name__ == "__main__":
    # 假設的相機內參
    focal_length = (fx, fy)
    principal_point = (cx, cy)
    distortion_coeffs = (k1, k2, p1, p2, k3)

    # 創建相機內參對象
    camera_params = CameraInternalParams()
    
    # 設置相機內參
    camera_params.set_params(focal_length, principal_point, distortion_coeffs)
    
    # 獲取相機內參
    print(camera_params.get_params())
