from kivy.app import App
from kivy.uix.recycleview import RecycleView

class RV(RecycleView):
    def __init__(self):
        super().__init__()
        self.data = [{'text':str(i)} for i in range(21)]

class MyRVApp(App):
    def build(self):
        return RV()
    
MyRVApp().run()