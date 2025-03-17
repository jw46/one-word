import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class B1(Button):
    def callback(self):
        self.text = "Bobby!!!!"

class OneWordApp(App):
    b1 = ObjectProperty(B1)

if __name__ == '__main__':
    OneWordApp().run()