from PIL import Image
import os

print('*** Program Started ***')
print("")

image_path_input = input("Give the absolute path of your image folder : ")
compress_quality = str(input("Choose the compress value [1:100] where 100 is low, press Enter for optimize (45) : "))
images = [file for file in os.listdir(image_path_input) if file.endswith(('jpg', 'png', 'jpeg', 'gif'))]
os.mkdir(image_path_input + "compressed/")
image_path_output = (image_path_input + "compressed/")

if compress_quality == '':
    compress_quality = 45
else:
    compress_quality = int(compress_quality)

for file in images:
    print('Input file name   : ', file)
    im = Image.open(image_path_input + file)
    uncompress_image = (image_path_input + file)
    uncompress_image_size = os.path.getsize(uncompress_image) / (1024 * 1024)
    print('Input Image size  : ' "%.2f" % uncompress_image_size, 'MB')
    im.save(image_path_output + file, optimize=False, quality=compress_quality)
    compress_image = (image_path_output + file)
    compress_image_size = os.path.getsize(compress_image) / (1024 * 1024)
    print('Output Image size : ' "%.2f" % compress_image_size, 'MB')
    print("")

print('*** Program Ended ***')
