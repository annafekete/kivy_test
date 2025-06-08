from kivy.app import App #kivy program fő alkalmazásosztálya
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = FloatLayout() #root layout
        label1 = Label(text='Adja meg a vonalkódot!', size_hint=(0.3, 0.2), pos_hint={'center_x':0.5, 'center_y':0.7})
        label2 = Label(text='..vagy olvassa be!', size_hint=(0.3, 0.2), pos_hint={'center_x':0.5, 'center_y':0.5})
        button = Button(text='Beolvasás', size_hint=(0.5,0.1), pos_hint={'center_x':0.5, 'center_y':0.2})

        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(button)

        return layout
    
if __name__ == '__main__':
    MyApp().run()