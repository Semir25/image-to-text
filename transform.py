from PIL import Image
import numpy

image_path = input('Enter the path to the image (image.jpg): ')

image_name = image_path.strip().split('/')
image_name = image_name[len(image_name) - 1].split('.')
image_extension = image_name[len(image_name) - 1]
image_name = image_name[0]
if image_extension != 'jpg' and image_extension != 'jpeg' and image_extension != 'png':
    raise Exception('not a valid format!')


char_width = input('Enter width of output file (1 = 1 characte): ')
palette = input('Enter chatacters for palette/gradient (leave blank for default palette): ')

if len(palette) == 0:
    palette = '@@@@###$?//--_______'

im = Image.open(image_path, 'r')
width, height = im.size
pixel_values = list(im.getdata())
pixel_values = numpy.array(pixel_values).reshape((width, height, 3))


f = open(image_name+'.txt', "w")

blur_width = int(width/int(char_width))
blur_height = blur_width*2
w = width - width%blur_width - blur_width
h = height - height%blur_height - blur_height


for i in range(0, h, blur_height):
    for j in range(0, w, blur_width):
        tmp = 0
        for x in range(blur_height):
            for y in range(blur_width):
                if i+y < width and j+x < height:
                    tmp += pixel_values[i+y][j+x][0] + pixel_values[i+y][j+x][1] + pixel_values[i+y][j+x][2]
        tmp /= blur_width*blur_height*3
        tmp = int(tmp/(256/len(palette)))
        f.write(palette[tmp])
        # if tmp < 50:
        #     f.write('#')
        # elif tmp < 90:
        #     f.write('@')
        # elif tmp < 120:
        #     f.write('$')
        # elif tmp < 130:
        #     f.write('?')
        # elif tmp < 145:
        #     f.write('/')
        # elif tmp < 165:
        #     f.write('-')
        # else:
        #     f.write('_')
    f.write("\n")
f.close()
im.close()
