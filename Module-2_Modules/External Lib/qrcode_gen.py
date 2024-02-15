import pyqrcode

url="https://www.tops-int.com/"

x=pyqrcode.create(url)
x.png('tops.png')