# import module
from pdf2image import convert_from_path

#file_name = './ch01_test.pdf'
file_name = '/Users/bruce_t_wang/dev/pdfTest/ch04_test.pdf'
# Store Pdf with convert_from_path function
images = convert_from_path(file_name)
 
for i in range(len(images)):
    # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')


