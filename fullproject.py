from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty

class ListWidget(RecycleView):
    
    def update(self):
        self.data = [{'text': str(item)} for item in self.items]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = []

class RootWidget(BoxLayout):
    inputbutton = ObjectProperty(None)
    inputcontent = ObjectProperty(None)
    outputconent = ObjectProperty(None)

    def add_item(self):
        if self.inputcontent.text != "":
            formatted = f'\n •{self.inputcontent.text}'
            self.outputcontent.items.append(formatted)
            self.outputcontent.update()
            self.inputcontent.text = ""

class MyFullApp(App):
    def build(self):
        return RootWidget()

MyFullApp().run()