import qrcode


def generate_qrcode(data):
    qr = qrcode.make(data)
    return qr