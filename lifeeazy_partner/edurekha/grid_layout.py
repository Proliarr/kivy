from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label



class grid_layout(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.rows=2
        self.columns=2
        self.l1= Label(
            text = 'label one'
        )
        self.l2= Label(
            text = 'label one'
        )
        self.btn = Button(
            text = 'btn one',
            )
        self.l3= Label(
            text = 'label one'
        )
        self.btn2 = Button(
            text = 'btn one',
            )
        self.add_widget(self.l1)
        self.add_widget(self.l2)
        self.add_widget(self.l3)

        self.add_widget(self.btn)
        self.add_widget(self.btn2)



class Demoapp(App):
    def build(self):
        return grid_layout()

ob= Demoapp()
ob.run()