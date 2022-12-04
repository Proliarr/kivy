from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

class grid_layout(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.rows=4
        self.columns=1
        self.img = Image(
            source = 'lifeeazy_partner\edurekha\lifeeazyicon.png'
        )
        self.lbl = Label(
            text = 'Label one',

        )
        self.inputtext = TextInput(
            text = '',
            font_size =40
        )
        self.btn = Button(
            text='submitted',)
        self.pop = Popup(
            title = "result",
            size=(400,400),
            content = Label(
                text = '')
        )
        self.btn.bind(on_release = self.call_back)
        self.add_widget(self.pop)

        self.add_widget(self.img)
        self.add_widget(self.lbl)
        self.add_widget(self.inputtext)
        self.add_widget(self.btn)

    def call_back(self, elem):
        self.pop.content.text = self.text
        self.pop.open()
        



class Demoapp(App):
    def build(self):
        return grid_layout()

ob= Demoapp()
ob.run()