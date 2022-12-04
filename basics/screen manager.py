from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen,FallOutTransition
from kivy.lang  import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField




sm = ScreenManager(transition=FallOutTransition())

class Demo1(Screen):
    def show_data(self):
        t1=MDTextField(text="name")
        
        print(t1.text)
        print('madhu')
class Demo2(Screen):
    pass

class Main(MDApp):
    def build(self):
        Builder.load_file("uii.kv")
        sm.add_widget(Demo1.show_data.t1)
        sm.add_widget(Demo1(name='demo1'))
        sm.add_widget(Demo2(name='demo2'))

        return sm

ob=Main()
ob.run()