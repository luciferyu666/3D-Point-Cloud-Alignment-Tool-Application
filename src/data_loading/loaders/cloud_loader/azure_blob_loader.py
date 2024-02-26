# path/filename: azure_blob_loader.py

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import ResourceNotFoundError

def load_data_from_blob(account_url, container_name, blob_name, credential):
    """
    從 Microsoft Azure Blob Storage 加載數據。

    :param account_url: Azure 存儲帳戶的 URL
    :param container_name: Blob 容器名稱
    :param blob_name: Blob 名稱
    :param credential: 認證信息
    :return: 讀取的數據，如果錯誤則返回 None
    """
    try:
        # 創建 Blob 服務客戶端
        blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)
        # 獲取指定容器的客戶端
        container_client = blob_service_client.get_container_client(container=container_name)
        # 獲取 Blob 客戶端以訪問指定的 Blob
        blob_client = container_client.get_blob_client(blob=blob_name)
        # 下載 Blob 內容
        blob_data = blob_client.download_blob()
        data = blob_data.readall()
        return data
    except ResourceNotFoundError:
        print("指定的 Blob 或容器不存在。")
        return None
    except Exception as e:
        print(f"數據加載失敗: {e}")
        return None

# 使用範例
if __name__ == '__main__':
    account_url = "your-account-url"
    container_name = "your-container-name"
    blob_name = "your-blob-name"
    credential = "your-credential"  # 考慮使用 Azure 身份認證
    data = load_data_from_blob(account_url, container_name, blob_name, credential)
    if data:
        print("數據加載成功")
    else:
        print("數據加載失敗")
