import pyrebase
from PIL import Image, ImageFont, ImageDraw

firebaseConfig = {
    "apiKey": <your API key>,
    "authDomain": <your auth domain>,
    "databaseURL": <your db url>,
    "projectId": <your firebase project id>,
    "storageBucket": <your firebase storage bucket>,
    "messagingSenderId": <your sender id>,
    "appId": <your app id>,
}


#
#
def gen_certificate(path, name):
    img = Image.open('new.jpg')
    font = ImageFont.truetype('arial.ttf', 60)
    draw = ImageDraw.Draw(img)
    li = name.split(' ')
    if len(li) >= 2:
        draw.text(xy=(365, 320), text=name, fill=(0, 0, 0), font=font)
    else:
        draw.text(xy=(459, 320), text=name, fill=(0, 0, 0), font=font)

    img = img.convert("RGB")
    img.save(f'./upload_certificate/{name}.pdf')

    # firebase1 = pyrebase.initialize_app(firebaseConfig)
    # storage = firebase1.storage()
    #
    # path_on_sys = f'{name}.pdf'
    #
    # storage.child(f'{path}/{name}.pdf').put(f'{name}.pdf')


# def download_certificate(path, name):
#     firebase1 = pyrebase.initialize_app(firebaseConfig)
#     storage = firebase1.storage()
#     # storage.child(f'{path}/{name}.pdf').download(f'{name}.pdf')
#     return storage.child(f'{path}/{name}.pdf').get_url(None)

#
# firebase1 = pyrebase.initialize_app(firebaseConfig)
# storage = firebase1.storage()
# storage.child('img/bootstrap1.PNG').get_url(None)
