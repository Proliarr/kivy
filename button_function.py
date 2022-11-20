from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton 
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
# from helpers import text_config
import helpers
from kivy.uix.label import Label




class demoapp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Blue"
        self.theme_cls.theme_style="Dark"
        screen= Screen()
        self.text_field=MDTextField(text='enter your First name here',pos_hint={'center_x':0.5,'center_y':0.7},size_hint_x=None,width=300)
        btn = MDRectangleFlatButton(text= "button",pos_hint={'center_x':0.5,"center_y":0.5},on_release=self.show_data)
       
        self.text_field_buider = Builder.load_string(helpers.text_config)
        self.label_name=MDLabel(text="first APP",font_style='H1',pos_hint={'center_x':0.5,'center_y':0.9},size_hint=(0.5,1))
        screen.add_widget(self.text_field_buider)
        screen.add_widget(self.text_field)
        screen.add_widget(btn)
        
        screen.add_widget(self.label_name)


        return screen
    def show_data(self,obj):
        screen2=Screen()
        print(self.text_field_buider)
        print((self.text_field_buider.text))
        print((self.text_field.text))
        label_name2 = Label(text=self.text_field_buider.text,pos_hint={'center_x':0.5,'center_y':0.2})
        screen2.add_widget(label_name2)
        return screen2        

ob=demoapp()
ob.run()