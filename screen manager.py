from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen,FallOutTransition
from kivy.lang  import Builder

class Demo1(Screen):
    pass

class Demo2(Screen):
    pass

class Main(MDApp):
    def build(self):
        Builder.load_file("uii.kv")
        sm = ScreenManager(transition=FallOutTransition())
        sm.add_widget(Demo1(name='demo1'))
        sm.add_widget(Demo2(name='demo2'))

        return sm

ob=Main()
ob.run()