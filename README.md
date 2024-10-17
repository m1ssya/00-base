# base-python

base-python 是一个包含通用 Python 代码的仓库,旨在提供可重复使用的组件,以简化常见任务的开发过程。所有代码均使用cursor自动生成。

## 功能

这个仓库包含以下几个主要类别的通用代码:

| 模块 | 文件 | 描述 |
|------|------|------|
| 日志 | [log/logger.py](log/logger.py) | 日志配置和自定义格式化 |
| 数据库 | [db/db_connector_mysql.py](db/db_connector_mysql.py) | MySQL数据库连接器 |
| HTTP | [http/http_client.py](http/http_client.py) | HTTP请求客户端 |

## 使用方法

要使用这个仓库中的代码,您可以:

1. 克隆整个仓库:   ```
   git clone https://github.com/miss/base-python.git   ```

2. 复制所需的特定模块到您的项目中

3. 将此仓库作为子模块添加到您的项目中
