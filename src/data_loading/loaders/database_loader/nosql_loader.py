# path/filename: nosql_loader.py

from pymongo import MongoClient

def load_data_from_mongodb(connection_string, database_name, collection_name, query={}):
    """
    從 MongoDB 加載數據。

    :param connection_string: MongoDB 連接字符串
    :param database_name: 數據庫名稱
    :param collection_name: 集合名稱
    :param query: 查詢字典，默認為空字典以加載所有文檔
    :return: 查詢結果的列表
    """
    # 建立連接
    client = MongoClient(connection_string)
    # 指定數據庫和集合
    db = client[database_name]
    collection = db[collection_name]
    # 執行查詢
    results = collection.find(query)
    # 將查詢結果轉換為列表
    return list(results)

# 使用範例
if __name__ == '__main__':
    conn_string = "your-connection-string"
    db_name = "your-database-name"
    collection_name = "your-collection-name"
    query = {}  # 可以指定查詢條件
    data = load_data_from_mongodb(conn_string, db_name, collection_name, query)
    print(data)
