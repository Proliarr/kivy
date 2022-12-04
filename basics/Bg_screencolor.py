from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDFloatingActionButton,MDIconButton


# theme_cls.primary_palette=['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
# for adjustment of bg_color theme_cls.primary_hue = ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', 'A100', 'A200', 'A400', 'A700']
# screen bg_color = Light ,Dark
class demoapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Red'
        self.theme_cls.primary_hue="300"
        self.theme_cls.theme_style='Light'
        screen= Screen()
        btn=MDRectangleFlatButton(text="newbutton",
                        pos_hint={'center_x':0.5,'center_y':0.5})
        icon_btn = MDIconButton(icon="language-python",pos_hint={'center_x':0.8,'center_y':0.8})
        icon_btn2 = MDFloatingActionButton(icon="language-python",pos_hint={'center_x':0.8,'center_y':0.8})

        screen.add_widget(icon_btn2)

        return screen

ob=demoapp()
ob.run()