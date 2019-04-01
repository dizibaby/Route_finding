from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

# Create an in-memory stream
my_stream = BytesIO()
camera = PiCamera()
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture(my_stream, format='jpeg')
img=Image.open(my_stream)
img.show()


print my_stream
