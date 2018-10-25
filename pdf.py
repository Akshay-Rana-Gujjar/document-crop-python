# from fpdf import FPDF
# from PIL import Image

# pdf = FPDF()
# # imagelist is the list with all image filenames

# imagelist = ["test.jpg", "testout.jpg"]
# for image in imagelist:
#     base_image = Image.open(image)
#     width, height = base_image.size
#     print(width, height)
#     pdf.add_page()
#     pdf.image(image,0,0,width,height)
# pdf.output("yourfile.pdf", "F")


from PIL import Image
from os import walk
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

im_list = []
mypath = "output/"
for (dirpath, dirnames, filenames) in walk(mypath):
    filenames.sort(key=natural_keys)
    for image_name in filenames:
        print(image_name)
        im_list.append(Image.open(f"{mypath}{image_name}"))
    break

# print(im_list)
im1 = im_list.pop(0)

pdf1_filename = f"{mypath}/output.pdf"

im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)