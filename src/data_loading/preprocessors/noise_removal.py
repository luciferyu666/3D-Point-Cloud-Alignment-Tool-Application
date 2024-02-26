import open3d as o3d

def remove_noise_from_point_cloud(point_cloud_path, nb_neighbors=20, std_ratio=2.0):
    """
    使用統計分析方法從3D點雲數據中移除噪聲。

    參數:
    - point_cloud_path: 3D點雲文件的路徑。
    - nb_neighbors: 用於計算每個點的鄰域數量。
    - std_ratio: 用於過濾點的標準差比例。

    返回:
    - 去噪後的點雲。
    """
    # 加載點雲數據
    pcd = o3d.io.read_point_cloud(point_cloud_path)
    
    # 執行去噪處理
    cl, ind = pcd.remove_statistical_outlier(nb_neighbors=nb_neighbors,
                                             std_ratio=std_ratio)
    noise_removed_pcd = pcd.select_by_index(ind)
    
    return noise_removed_pcd

# 使用示例
if __name__ == "__main__":
    input_path = 'path_to_your_point_cloud.ply'
    cleaned_pcd = remove_noise_from_point_cloud(input_path)
    # 保存去噪後的點雲，用於後續處理或可視化
    o3d.io.write_point_cloud('cleaned_point_cloud.ply', cleaned_pcd)
    print("去噪處理完成，結果已保存。")
