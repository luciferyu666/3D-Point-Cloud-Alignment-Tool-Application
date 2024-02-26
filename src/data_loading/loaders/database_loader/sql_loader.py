import sqlite3

def load_data_from_db(db_path, query):
    """從SQL數據庫加載數據。

    參數:
    db_path (str): 數據庫文件的路徑。
    query (str): 要執行的SQL查詢。

    返回:
    list: 查詢結果，每一行作為字典返回。
    """
    conn = None
    try:
        # 建立數據庫連接
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # 使查詢結果可以像字典那樣訪問
        cursor = conn.cursor()
        # 執行SQL查詢
        cursor.execute(query)
        # 獲取查詢結果
        rows = cursor.fetchall()
        # 將結果轉換為字典列表
        results = [dict(row) for row in rows]
        return results
    except sqlite3.Error as e:
        print(f"數據庫錯誤: {e}")
        return []
    finally:
        if conn:
            conn.close()

# 使用示例
if __name__ == "__main__":
    db_path = 'path_to_your_database.db'
    query = 'SELECT * FROM your_table'
    data = load_data_from_db(db_path, query)
    for row in data:
        print(row)
