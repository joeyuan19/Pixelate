from PIL import Image
import numpy as np

def pixelate(img,pixel_size=5):
    X,Y = img.size
    NX = X//pixel_size
    NY = Y//pixel_size
    data = np.array(img)
    avg = []
    for nx in range(NX):
        for ny in range(NY):
            avg = [0,0,0]
            c = 0
            for i in range(pixel_size*pixel_size):
                y = ny*pixel_size + i%pixel_size
                x = nx*pixel_size + i//pixel_size
                c += 1
                for j in range(3):
                    avg[j] += data[y][x][j]
            for j in range(3):
                avg[j] = avg[j]//c
            for i in range(pixel_size*pixel_size):
                y = ny*pixel_size + i%pixel_size
                x = nx*pixel_size + i//pixel_size
                for j in range(3):
                    data[y][x][j] = avg[j]
    img = Image.fromarray(data)
    return img 

if __name__ == '__main__':
    import sys
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-p","--pixel",dest="pixel",default=5)
    opts,args = parser.parse_args()
    if len(args) <= 0:
        print("No image provided")
        sys.exit(1)
    img = Image.open(args[0])
    img = pixelate(img,int(opts.pixel))
    img.save('out.png')
