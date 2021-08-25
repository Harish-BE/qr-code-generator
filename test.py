from flask import *
import qrcode

def qrCode(url):
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode001.png')

app=Flask(__name__)
@app.route('/')
def root():
    return render_template('index.html')

@app.route('/home', methods = ['POST'])
def home():
    global url
    url = request.form['url']
    print(url)
    return render_template("download.html")

@app.route('/download')
def download():
    qrCode(url)
    return send_file('qrcode001.png')
