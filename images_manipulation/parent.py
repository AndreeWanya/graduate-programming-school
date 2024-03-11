import os.path
import logging
from PIL import Image, ImageDraw, ImageColor

def grep(path, ext):
    for root, dirs, files in os.walk(path):
        files = [fi for fi in files if fi.split('.')[-1] == ext]
        break
    return files

def image_converting(ext_1, ext_2):
    files = grep('.', ext_1)
    logging.warning(f'in this folder there are such files with extension {ext_1}: {files}')
    for fi in files:
        im = Image.open(fi)
        fn = fi[0:-len(ext_1)] + ext_2
        logging.warning(f'файл сохранится под именем {fn}')
        try:
            im.save(fn)
        except OSError:
            rgb_im = im.convert('RGB')
            rgb_im.save(fn)

image_converting('png', 'jpg')
image_converting('jpg', 'bmp')
