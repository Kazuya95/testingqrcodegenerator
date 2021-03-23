'''
QR code generator
From:
https://https://www.youtube.com/watch?v=l4ugfcj7qrI

'''

import qrcode

# function to generate qr code
def qr_generator(site,where_to_save):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=50,
                       border=2)

    qr.add_data(site)
    qr.make(fit=True)

    img = qr.make_image(fill_color = "black",back_color="white")
    img.save(where_to_save)
    print('Done')

## example:
##site = "www.google.com"
##name = 'google.jpg'
##where_to_save = f"C:/Users/Desktop/{name}"


if __name__ == '__main__':
    qr_generator(site,where_to_save)
