import requests
import requests

img = "https://sun9-23.userapi.com/impg/TTMyZWYTF-BGQrjaB3C6R7pmXisXF9-LeWrBeA/FDFPlyK1x24.jpg?size=1200x1600&quality=96&sign=67cd22470cec41619c09d18cca45e5ea&type=album"
response = requests.get(img)

with open("test.jpg", "wb") as file:
    file.write(response.content)
