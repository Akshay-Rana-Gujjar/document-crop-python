from PIL import Image
 
def photo_with_watermark(input_image_path, output_image_path, watermark_image_path):
	base_image = Image.open(input_image_path)
	watermark = Image.open(watermark_image_path)
	
	new_image = base_image
	width, height = new_image.size

	if width > height:
		new_image = base_image.transpose(Image.ROTATE_270)
		
	else:
		new_image = base_image
		width, height = new_image.size
	watermark = watermark.resize((int(width*0.8), int(width*0.8)), Image.ANTIALIAS)
	watermark_width, watermark_height = watermark.size
	position = (int(width/2) - int(watermark_width/2), int(height/2) - int(watermark_height/2))
	print(width, height)
	transparent = Image.new('RGB', (width, height), (0,0,0,0))
	transparent.paste(new_image, (0,0))
	transparent.paste(watermark, position, mask=watermark)
	transparent.save(output_image_path)
 

# main_image = '20181023_140526.jpg-out.jpg'
watermark_photo = "watermark-25.png"
# watermark_photo = cv2.resize(watermark_photo, None, fx=2, fy=2)

from os import walk

f = []
mypath = "input/a/"
for (dirpath, dirnames, filenames) in walk(mypath):
	print(dirpath)
	for main_image in filenames:
		photo_with_watermark(mypath+main_image, f'output/{main_image}-watermarked.jpg', watermark_photo)
#     f.extend(filenames)
	break
# print(f)

