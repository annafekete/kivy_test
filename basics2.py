from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyLayout(BoxLayout): #osztály ami örökli a BoxLayout tulajdonságait
    def __init__(self): #konstruktorfüggvény (példányosításkor fut le)
        super().__init__() #meghívjuk a BoxLayout-ból örökölt konstruktorát (alap viselkedés is megmaradjon)
        self.button = Button(text='Beolvasás')
        self.button.bind(on_press=self.new_label) #összeköti (bind) az on_press eseményt (event) az általunk megírt föggvénnyel

        self.add_widget(self.button)

    def new_label(self, button):
        self.label = Label(text = 'Beolvasás sikeres!')
        self.add_widget(self.label)
        self.remove_widget(button)

class MyApp(App): #fő alkalmazás
    def build(self): #visszaadja az app kezdő felületét
        return MyLayout()
    
if __name__ == '__main__': #python-ban szokásos belépési pont
    MyApp().run()