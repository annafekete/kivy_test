from kivy.app import App
from kivy.uix.label import Label

class MyLabel(Label):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def on_touch_down(self, touch):
        print('DOWN', touch)
    def on_touch_up(self, touch):
        print('UP', touch)
    def on_touch_move(self, touch):
        print('MOVE', touch)

class MyApp(App):
    def build(self):
        self.thislabel = MyLabel('hi')
        return self.thislabel
    
if __name__ == '__main__':
    MyApp().run()