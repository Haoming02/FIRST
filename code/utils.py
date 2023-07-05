from PIL import Image
import base64

def to_base64(png_bytes):
    return base64.b64encode(png_bytes).decode('utf-8')

def from_base64(base64_string):   
    return base64.b64decode(base64_string)

def encode_image(file_name):
    with open(file_name, 'rb') as FILE:
        return to_base64(FILE.read())

def decode_image(base64_string, file_name):
    with open(file_name, 'wb') as FILE:
        FILE.write(from_base64(base64_string))

def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.size