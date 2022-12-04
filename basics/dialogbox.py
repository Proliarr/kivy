from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton 
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
# from helpers import text_config
import helpers
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog




class demoapp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Blue"
        self.theme_cls.theme_style="Dark"
        screen= Screen()
        self.text_field=MDTextField(text='enter your First name here',pos_hint={'center_x':0.5,'center_y':0.7},size_hint=(0.5,1))
        btn = MDRectangleFlatButton(text= "button",pos_hint={'center_x':0.5,"center_y":0.5},on_release=self.show_data)
       
        self.text_field_buider = Builder.load_string(helpers.text_config)
        self.label_name=MDLabel(text="first APP",font_style='H1',pos_hint={'center_x':0.5,'center_y':0.9},size_hint=(0.5,1))
        screen.add_widget(self.text_field_buider)
        screen.add_widget(self.text_field)
        screen.add_widget(btn)
        
        screen.add_widget(self.label_name)


        return screen
    def show_data(self,obj):
        print(self.text_field_buider)
        firstname=((self.text_field_buider.text))
        lastname = ((self.text_field.text))
        dialog_box=MDDialog(title = 'check your relationship',text=firstname+' hubby and wiffy '+lastname,size_hint=(0.5,1))
        dialog_box.open()
        

ob=demoapp()
ob.run()