import requests
import logging
from typing import Dict, Any, Optional

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_request(url: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, timeout: int = 10) -> requests.Response:
    """
    发送GET请求。

    参数:
    url (str): 请求的URL
    params (dict, optional): URL参数
    headers (dict, optional): 请求头
    timeout (int): 请求超时时间(秒)

    返回:
    requests.Response: 响应对象

    异常:
    requests.RequestException: 如果请求失败
    """
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        logger.info(f"GET请求成功: {url}")
        return response
    except requests.RequestException as e:
        logger.error(f"GET请求失败: {url}. 错误: {e}")
        raise

def post_request(url: str, data: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, timeout: int = 10) -> requests.Response:
    """
    发送POST请求。

    参数:
    url (str): 请求的URL
    data (dict, optional): 表单数据
    json (dict, optional): JSON数据
    headers (dict, optional): 请求头
    timeout (int): 请求超时时间(秒)

    返回:
    requests.Response: 响应对象

    异常:
    requests.RequestException: 如果请求失败
    """
    try:
        response = requests.post(url, data=data, json=json, headers=headers, timeout=timeout)
        response.raise_for_status()
        logger.info(f"POST请求成功: {url}")
        return response
    except requests.RequestException as e:
        logger.error(f"POST请求失败: {url}. 错误: {e}")
        raise

# 使用示例
if __name__ == "__main__":
    try:
        # GET请求示例
        get_response = get_request("https://www.baidu.com", params={"key": "value"})
        print(get_response.status_code)

        # POST请求示例
        post_response = post_request("https://www.baidu.com", json={"name": "张三", "age": 30})
        print(post_response.json())

    except requests.RequestException as e:
        print(f"请求失败: {e}")
