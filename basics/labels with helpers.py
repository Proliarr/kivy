from kivymd.uix.label import MDLabel,MDIcon
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
import helpers



class demoapp(MDApp):
    def build(self):
        screen= Screen()
        self.theme_cls.theme_style = "Light"
        lb1 = Builder.load_string(helpers.label_name)
        lb2 = Builder.load_string(helpers.labellast)
        lb3 = Builder.load_string(helpers.label_name2)
        icon_label = Builder.load_string(helpers.icon_1)
        screen.add_widget(lb3)
        
        screen.add_widget(lb2)
        screen.add_widget(lb1)
        screen.add_widget(icon_label)
        return screen


ob=demoapp()
ob.run()