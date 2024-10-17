import logging
from datetime import datetime
from colorama import Fore, Back, Style, init

# 初始化colorama
init(autoreset=True)

class Logger:
    _instance = None

    def __new__(cls, name="DefaultLogger", log_file=None, level=logging.INFO):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize(name, log_file, level)
        return cls._instance

    def _initialize(self, name, log_file, level):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # 自定义格式化器
        class ColoredFormatter(logging.Formatter):
            FORMATS = {
                logging.DEBUG: Fore.CYAN + Style.DIM + '%(asctime)s - %(name)s - %(levelname)s - %(message)s' + Style.RESET_ALL,
                logging.INFO: Fore.GREEN + '%(asctime)s - %(name)s - %(levelname)s - %(message)s' + Style.RESET_ALL,
                logging.WARNING: Fore.YELLOW + '%(asctime)s - %(name)s - %(levelname)s - %(message)s' + Style.RESET_ALL,
                logging.ERROR: Fore.RED + '%(asctime)s - %(name)s - %(levelname)s - %(message)s' + Style.RESET_ALL,
                logging.CRITICAL: Fore.WHITE + Back.RED + Style.BRIGHT + '%(asctime)s - %(name)s - %(levelname)s - %(message)s' + Style.RESET_ALL
            }

            def format(self, record):
                log_fmt = self.FORMATS.get(record.levelno)
                formatter = logging.Formatter(log_fmt, datefmt='%Y-%m-%d %H:%M:%S')
                return formatter.format(record)

        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(ColoredFormatter())
        self.logger.addHandler(console_handler)

        # 如果提供了日志文件名，则创建文件处理器
        if log_file:
            file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    @staticmethod
    def get_current_time():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 创建全局日志实例
global_logger = Logger()

if __name__ == "__main__":
    global_logger.debug("这是一个调试日志")
    global_logger.info("这是一个信息日志")
    global_logger.warning("这是一个警告日志")
    global_logger.error("这是一个错误日志")

    # 测试单例模式
    another_logger = Logger()
    another_logger.info("这条日志应该使用相同的日志实例")
