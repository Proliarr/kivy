from kivymd.uix.label import MDLabel,MDIcon
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
import helpers
from kivymd.uix.screenmanager import ScreenManager
from kivy.network.urlrequest import UrlRequest
from functools import partial
import requests

# payload =   {'Username':'Madhu','password':'password'}
# r= requests.post('https://httpbin.org/post', data=payload)

r= requests.get('https://httpbin.org/basic-auth/token/testing',auth=('corey','testing'))
print(r.text)

class loginscreen(MDApp):
    
    def build(self):
        screen = Screen()
        username=Builder.load_string(helpers.user_text)
        passsword=Builder.load_string(helpers.password)
        not_signed=Builder.load_string(helpers.not_signed)
        # loginbtn = Builder.load_string(helpers.login_btn,on_release=self.show_data)
        loginbtn = MDRectangleFlatButton(text= "Login",pos_hint={'center_x':0.5,"center_y":0.5},on_release=self.show_data)
        # screen_manager=Builder.load_string(screen_helper)

        # screen.add_widget(not_signed)
        screen.add_widget(username)
        # screen.add_widget(screen_manager)
        screen.add_widget(passsword)
        screen.add_widget(loginbtn)
        self.username = username
        self.password = passsword

        return screen
    def show_data(self,obj):
        print( self.username.text+self.password.text)
        for i in range(10):
            self.r = UrlRequest('https://www.google.com',on_success=partial(self.update_label,1))

    def update_label(self,i,*kwargs):
        print(i)




ob=loginscreen()
ob.run()

