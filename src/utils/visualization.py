import open3d as o3d

class Visualization:
    def __init__(self):
        pass

    @staticmethod
    def visualize_point_cloud(point_cloud_path):
        """3D點雲視覺化"""
        pcd = o3d.io.read_point_cloud(point_cloud_path)
        o3d.visualization.draw_geometries([pcd], window_name="3D 點雲視覺化")

    @staticmethod
    def visualize_alignment(source_path, target_path, transformation):
        """點雲對齊結果展示"""
        source = o3d.io.read_point_cloud(source_path)
        target = o3d.io.read_point_cloud(target_path)
        source.transform(transformation)
        o3d.visualization.draw_geometries([source, target], window_name="點雲對齊結果")

    @staticmethod
    def highlight_features(point_cloud_path, features_indices):
        """標註和高亮顯示特定特徵"""
        pcd = o3d.io.read_point_cloud(point_cloud_path)
        colors = [[1, 0, 0] for i in range(len(pcd.points))]
        for i in features_indices:
            colors[i] = [0, 1, 0]  # 將特徵點標記為綠色
        pcd.colors = o3d.utility.Vector3dVector(colors)
        o3d.visualization.draw_geometries([pcd], window_name="特徵高亮顯示")

# 示例使用
if __name__ == "__main__":
    vis = Visualization()
    # 假設有兩個點雲文件 'source.ply' 和 'target.ply'，以及一個變換矩陣
    transformation = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    vis.visualize_point_cloud('source.ply')
    vis.visualize_alignment('source.ply', 'target.ply', transformation)
    vis.highlight_features('source.ply', [10, 20, 30])  # 假設這些索引代表了特徵點
