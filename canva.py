from kivy.app import App
from kivy.graphics import Rectangle, Line
from kivy.uix.widget import Widget

class MyWidget(Widget):
    def on_touch_down(self, touch):
    #   self.canvas.add(Rectangle(pos=(touch.x, touch.y), size=(50, 50)))
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

    def on_touch_up(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyApp(App):
    def build(self):
        return MyWidget()
    
if __name__ == '__main__':
    MyApp().run()