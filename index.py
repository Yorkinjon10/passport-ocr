from passporteye import read_mrz
import os

image_file = os.path.join(os.path.dirname(__file__), '1.jpg')

mrz = read_mrz(image_file)

print(mrz)