from kivymd.app import MDApp
from kivy.lang import Builder


screen_helper ="""
Screen:
    BoxLayout: 
        orientation: 'vertical'
        MDToolbar:
            title: 'HelWorld'
        MDLabel:
            text: 'Hello World'
            halign: 'center'

"""

class Demoapp(MDApp):

    def build(self):
        screen=Builder.load_string(screen_helper)
        return screen


ob=Demoapp()
ob.run()