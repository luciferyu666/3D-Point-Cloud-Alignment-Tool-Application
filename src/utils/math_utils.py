import numpy as np

def vector_add(v1, v2):
    """向量加法"""
    return np.add(v1, v2)

def vector_subtract(v1, v2):
    """向量減法"""
    return np.subtract(v1, v2)

def dot_product(v1, v2):
    """內積"""
    return np.dot(v1, v2)

def cross_product(v1, v2):
    """外積"""
    return np.cross(v1, v2)

def matrix_multiply(m1, m2):
    """矩陣乘法"""
    return np.dot(m1, m2)

def translate(vector, translation):
    """平移變換"""
    return vector + translation

def rotate(vector, rotation_matrix):
    """旋轉變換"""
    return np.dot(rotation_matrix, vector)

def scale(vector, scale_factor):
    """縮放變換"""
    return vector * scale_factor

# 示例使用
if __name__ == "__main__":
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    m1 = np.array([[1, 2], [3, 4]])
    m2 = np.array([[2, 0], [1, 2]])

    print("向量加法:", vector_add(v1, v2))
    print("向量減法:", vector_subtract(v1, v2))
    print("內積:", dot_product(v1, v2))
    print("外積:", cross_product(v1, v2))
    print("矩陣乘法:", matrix_multiply(m1, m2))
