from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout

class SoundPlayer(BoxLayout):

    def playSound(self):
        sound = SoundLoader.load('correct.wav')
        if sound:
            sound.volume = 0.5
            sound.play()

class MySoundApp(App):
    def build(self):
        return SoundPlayer()
    
MySoundApp().run()