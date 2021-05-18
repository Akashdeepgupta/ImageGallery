from PIL import Image
import os
from fpdf import FPDF
import glob
base_dir = os.path.dirname(__file__)


pdf = FPDF()
# imagelist is the list with all image filenames
target=os.path.join(base_dir, 'imagesForpdf')
imagelist = glob.glob(target+'/*.jpg')
print(os.listdir(target))
for img in imagelist:
    print(img)
    pdf.add_page()
    pdf.image(img )
pdf.output("yourfile.pdf", "F")
