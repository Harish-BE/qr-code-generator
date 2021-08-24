from flask import Flask, render_template
import qrcode

input_data="www.google.com"
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
print(img)
qr_code=img.save('qrcode001.png')
print(qr_code)

app=Flask(__name__)


@app.route('/')
def hello1():
    return render_template('home.html',img=qr_code,item="hi")
