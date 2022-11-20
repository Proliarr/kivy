from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDFloatingActionButton,MDIconButton

class demoapp(MDApp):
    def build(self):
        screen= Screen()
        btn=MDRectangleFlatButton(text="newbutton",
                        pos_hint={'center_x':0.5,'center_y':0.5})
        icon_btn = MDIconButton(icon="language-python",pos_hint={'center_x':0.8,'center_y':0.8})
        icon_btn2 = MDFloatingActionButton(icon="language-python",pos_hint={'center_x':0.8,'center_y':0.8})

        screen.add_widget(icon_btn2)

        return screen

ob=demoapp()
ob.run()