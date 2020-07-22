import Image
from tesseract import image_to_stringprint image_to_string(Image.open('test.png'))
print image_to_string(Image.open('test-english.jpg'), lang='eng')
