from kivy.app import App #kivy program fő alkalmazásosztálya
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty #we can link between the python file and the kv file

class MyBox(Widget):
    myinput = ObjectProperty(None)

    def printOut(self):
        print(self.myInput.text)

class MyApp(App):
    def build(self):
        return MyBox()
    
if __name__ == '__main__':
    MyApp().run()