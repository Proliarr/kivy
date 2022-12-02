from  kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.widget import Widget
from kivymd.uix.button import MDRectangleFlatButton

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass
class WindowManger(ScreenManager):
    pass
class MyLayout(Widget):
    pass
kv = Builder.load_file('new_window.kv')

class AwesomeWindow(App):
    def build(self):
        return kv

if __name__ == '__main__':
    AwesomeWindow().run()