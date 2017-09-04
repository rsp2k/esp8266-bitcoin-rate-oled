import urequests
import time
import ssd1306
import machine
import json

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    r = urequests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    usd = r["bpi"]['USD']['rate']
    oled.fill(0)
    oled.text("The current", 0, 0)
    oled.text("bitcoin price", 0, 10)
    oled.text("is: ${}".format(usd), 0, 20)
    oled.show()
    time.sleep(300)
