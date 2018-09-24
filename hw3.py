#Part 1
from image import *
image = "arch.jpg"

def change_colors(pic):
    img = Image(pic)
    pixels = img.getPixels()
    for pix in pixels:
        r = pix.getRed()
        g = pix.getGreen()
        b = pix.getBlue()
        pix.setRed(b)
        pix.setGreen(r)
        pix.setBlue(g)
        img.updatePixel(pix)
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)
    
change_colors(image)


#Part 2
from image import *
image = "arch.jpg"

def stripe_manipulation(pic):
    img = Image(pic)
    fifth = int(img.getWidth() / 5)
    width = int(img.getWidth())
    height = int(img.getHeight())
    counter = 0
    for i in range(5):
        start = fifth * i
        end = start + fifth
        counter += 1
        for x in range(start, end):
            for y in range(height):
                p = img.getPixel(x, y)
                
                #current pixel rgb values
                r = p.getRed()
                g = p.getGreen()
                b = p.getBlue()
                
                #1st stripe
                if counter == 1:
                    if r < 120:
                        r = 0
                    if r >= 120:
                        r = 120
                    if g < 120:
                        g = 0
                    if g >= 120:
                        g = 120
                    if b < 120:
                        b = 0
                    if b >= 120:
                        b = 120
                    newPixel = Pixel(r,g,b)
                    img.setPixel(x, y, newPixel)
                    
                #2nd stripe
                elif counter == 2:
                    newPixel = Pixel(255-r, 255-g, 255-b)
                    img.setPixel(x, y, newPixel)

                #3rd stripe
                elif counter == 3:
                    None
                
                #4th stripe
                elif counter == 4:
                    p.setGreen(g * 2.5)
                    img.updatePixel(p)
                    
                #5 stripe
                else:
                    p.setRed(g)
                    p.setGreen(b)
                    p.setBlue(r)
                    img.updatePixel(p)
                    
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)
    
stripe_manipulation(image)

#Part 3
from image import *
image = "arch.jpg"

def posterize(pic):
    img = Image(pic)
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            p = img.getPixel(x, y)

            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()

            if r >= 0 and r < 64:
                r = 31
            elif r >= 64 and r < 128:
                r = 95
            elif r >= 128 and r < 192:
                r = 159
            else:
                r = 223

            if g >= 0 and g < 64:
                g = 31
            elif g >= 64 and g < 128:
                g = 95
            elif g >= 128 and g < 192:
                g = 159
            else:
                g = 223

            if b >= 0 and b < 64:
                b = 31
            elif b >= 64 and b < 128:
                b = 95
            elif b >= 128 and b < 192:
                b = 159
            else:
                b = 223

            newPixel = Pixel(r,g,b)
            img.setPixel(x, y, newPixel)

    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)

posterize(image)