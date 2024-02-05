# API參考文檔

本文檔提供了關於3D點雲處理與分析工具的API接口詳細說明，幫助開發者理解和使用各個功能模組。

## 數據加載模組 (`data_loader`)

### `load_point_cloud(file_path)`
加載3D點雲數據。

- 參數
  - `file_path` (str): 點雲文件的路徑。
  
- 返回
  - `o3d.geometry.PointCloud`: 加載的點雲對象。

### `load_image(file_path)`
加載影像數據。

- 參數
  - `file_path` (str): 影像文件的路徑。
  
- 返回
  - `Image`: 加載的影像對象。

## 預處理模組 (`preprocess`)

### `preprocess_point_cloud(point_cloud, voxel_size)`
對點雲進行預處理。

- 參數
  - `point_cloud` (o3d.geometry.PointCloud): 原始點雲對象。
  - `voxel_size` (float): 降採樣的像素大小。
  
- 返回
  - `o3d.geometry.PointCloud`: 預處理後的點雲對象。

## 點雲對齊模組 (`alignment`)

### `perform_initial_alignment(source, target)`
進行初步點雲對齊。

- 參數
  - `source` (np.ndarray): 源點雲數據。
  - `target` (np.ndarray): 目標點雲數據。
  
- 返回
  - `np.ndarray`: 初步對齊的變換矩陣。

### `perform_icp(source, target, initial_alignment)`
利用ICP算法進行點雲精確對齊。

- 參數
  - `source` (np.ndarray): 源點雲數據。
  - `target` (np.ndarray): 目標點雲數據。
  - `initial_alignment` (np.ndarray): 初步對齊提供的變換矩陣。
  
- 返回
  - `np.ndarray`: ICP對齊後的變換矩陣。

## 結果可視化模組 (`visualization`)

### `visualize_point_cloud(point_cloud_path)`
顯示3D點雲。

- 參數
  - `point_cloud_path` (str): 點雲文件的路徑。
  
### `visualize_alignment_error(source_points, target_points)`
顯示點雲對齊誤差分析視圖。

- 參數
  - `source_points` (np.ndarray): 源點雲的點座標。
  - `target_points` (np.ndarray): 目標點雲的點座標。

本API文檔提供了各個模組的主要接口說明，有助於開發者快速瞭解如何在自己的項目中整合和使用這些功能。在實際應用中，可能需要根據具體需求進行適當的調整和擴展。