# 导入UART
from machine import UART
# 导入wifiat依赖中的at类
from wifiat import at
uart=UART(0,115200)
AT=at(uart)
# 连接wifi
AT.connect("wifi_name","wifi_pw")

# 查看信息
# AT.info()


# 查看联网信息
AT.netinfo()