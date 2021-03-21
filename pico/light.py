import os
from machine import Pin
import time

# LED灯的pin脚
l=Pin(25,Pin.OUT)

# 常亮
# l.high()

# 闪烁
while True:
    l.value(1)
    time.sleep(1)
    l.value(0)
    time.sleep(1)

