from PIL import Image, ImageDraw, ImageColor
from parent import grep
import logging

def square_drawing(ext_2):
    files = grep('.', ext_2)
    for fi in files:
        im = Image.open(fi)
        sz = im.size
        draw = ImageDraw.Draw(im)
        draw.regular_polygon((sz[0]/2, sz[1]/2, 40), n_sides=4, fill=None, outline='red')
        draw.multiline_text((sz[0]/2 - 15, sz[1]/2 - 15), 'Hello,\nWorld!', fill=(0, 0, 0))
        fn = fi[0:-len(ext_2) - 1] + '_2.' + ext_2
        im.save(fn)
        del draw
        #im.show()

square_drawing('jpg')
