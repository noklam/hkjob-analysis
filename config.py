import logging
LOG_FORMAT = "%(asctime)s | %(filename)s: %(lineno)d | %(funcName)s: | %(message)s"
logging.basicConfig(
            filename='training.log',
            level=logging.DEBUG,
            format=LOG_FORMAT)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
# 設定輸出格式
formatter = logging.Formatter(LOG_FORMAT)
# handler 設定輸出格式
console.setFormatter(formatter)
# 加入 hander 到 root logger
logging.getLogger('').addHandler(console)
