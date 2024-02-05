# src/test_visualization.py
import numpy as np
import matplotlib.pyplot as plt

def generate_random_data(size=100):
    """
    生成隨機數據用於測試可視化。
    """
    x = np.random.rand(size)
    y = np.random.rand(size)
    return x, y

def test_plot():
    """
    測試繪製隨機數據的散點圖。
    """
    x, y = generate_random_data()
    plt.scatter(x, y)
    plt.title('隨機數據散點圖')
    plt.xlabel('X 軸')
    plt.ylabel('Y 軸')
    plt.show()

if __name__ == "__main__":
    test_plot()
