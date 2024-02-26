# path/filename: s3_loader.py

import boto3
from botocore.exceptions import NoCredentialsError

def load_data_from_s3(bucket_name, object_key):
    """
    從 Amazon S3 加載數據。

    :param bucket_name: S3 桶名稱
    :param object_key: 對象鍵值
    :return: 讀取的數據，如果錯誤則返回 None
    """
    try:
        # 創建 S3 客戶端
        s3 = boto3.client('s3')
        # 從 S3 桶中獲取對象
        obj = s3.get_object(Bucket=bucket_name, Key=object_key)
        # 讀取數據
        data = obj['Body'].read()
        return data
    except NoCredentialsError:
        print("AWS 認證錯誤。請確保你的認證正確配置。")
        return None
    except Exception as e:
        print(f"數據加載失敗: {e}")
        return None

# 使用範例
if __name__ == '__main__':
    bucket = "your-bucket-name"
    key = "your-object-key"
    data = load_data_from_s3(bucket, key)
    if data:
        print("數據加載成功")
    else:
        print("數據加載失敗")
