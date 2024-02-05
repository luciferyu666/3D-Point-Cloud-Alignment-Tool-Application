# 結果可視化模組開發文件

## 主要目標在
結果可視化模組的主要目標在於提供一組強大的視覺化工具，用於展示3D點雲處理和對齊過程中的結果。這包括3D點雲的展示、對齊效果的視覺化比較，以及對齊誤差的分析視圖等。

## 功能特點
- 3D點雲展示：支援從文件讀取並顯示3D點雲，並提供交互式探索功能。
- 對齊效果比較：展示對齊前後點雲的視覺化比較，幫助使用者評估對齊質量。
- 誤差分析視圖：通過誤差熱圖等方法，對點雲對齊過程中的誤差進行分析和展示。

## 主要接口

### `display_point_cloud(point_cloud_path)`
顯示3D點雲。

- 參數
  - `point_cloud_path` (str): 點雲文件的路徑。

### `visualize_alignment_error(source_points, target_points)`
展示點雲對齊誤差分析視圖。

- 參數
  - `source_points` (np.ndarray): 源點雲的點座標。
  - `target_points` (np.ndarray): 目標點雲的點座標。

## 使用範例
以下是使用結果可視化模組展示3D點雲和對齊誤差分析的範例。

```python
from visualization.display import display_point_cloud
from visualization.error_heatmap import visualize_alignment_error

# 展示3D點雲
display_point_cloud("path/to/your/pointcloud.ply")

# 展示點雲對齊誤差分析
source_points = ...  # 源點雲數據
target_points = ...  # 目標點雲數據
visualize_alignment_error(source_points, target_points)
```

## 模組維護
本模組由我方團隊開發和維護，致力於提供高質量的3D點雲處理結果可視化工具。對於任何使用上的問題或建議，我方歡迎社區的回饋和貢獻，以幫助我方不斷改進和擴充可視化功能。

## 版權和許可
本模組採用Apache License Version 2許可協議。詳細的許可協議內容請參考項目根目錄下的`LICENSE`文件。