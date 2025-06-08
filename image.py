from kivy.app import App
from kivy.uix.image import Image #AsyncImage for images from a browser

class MyImage(Image):
    pass

class MyImageApp(App):
    def build(self):
        return MyImage()
        #return Image(source = 'image.jpg')

MyImageApp().run()