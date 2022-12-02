from kivymd.uix.label import MDLabel,MDIcon
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
import helpers
from kivy.uix.image import Image
from kivymd.uix.screenmanager import ScreenManager
from kivy.network.urlrequest import UrlRequest
import requests
class loginscreen(MDApp):
    
    def build(self):
        screen = Screen()
        username=Builder.load_string(helpers.user_text)
        passsword=Builder.load_string(helpers.password)
        not_signed=Builder.load_string(helpers.not_signed)
        # loginbtn = Builder.load_string(helpers.login_btn,on_release=self.show_data)
        loginbtn = MDRectangleFlatButton(text= "Login",pos_hint={'center_x':0.5,"center_y":0.5},on_release=self.show_data)
        # screen_manager=Builder.load_string(screen_helper)
        wimg= Builder.load_string(helpers.img)
        # wimg = Image(source=r"C:\Users\anves\AppData\Local\Programs\Python\Python310\lifeeazyicon.png")
        # screen.add_widget(not_signed)
        screen.add_widget(username)
        screen.add_widget(wimg)
        screen.add_widget(passsword)
        screen.add_widget(loginbtn)
        self.username = username
        self.password = passsword
        sm = ScreenManager()
        
        return screen
    def show_data(self,obj):
        print( self.username.text+" "+self.password.text)
        payload={
                "Username": self.username.text,
                "Password": self.password.text,
                "DeviceToken": "string"
                }
        print(payload)
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyNjMzMTkzLCJqdGkiOiIzNWI1MDljOWVmOWY0NWVkYmFkZDE5ZmQ3NDgyY2RkMiIsInVzZXJfaWQiOjV9.Dr1cc6j3KXjEE6kLSxtQy-QCbd_j4w7g7870RmVpLbY'}
        

        x=requests.post(url='https://staging-api.vivifyhealthcare.com/HCP/Login/',json=payload,headers=headers)
        print(x)
    
    def registration(self,i,*kwargs):
        api = "http://staging-api.vivifyhealthcare.com/User/Register/"
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyNjMzMTkzLCJqdGkiOiIzNWI1MDljOWVmOWY0NWVkYmFkZDE5ZmQ3NDgyY2RkMiIsInVzZXJfaWQiOjV9.Dr1cc6j3KXjEE6kLSxtQy-QCbd_j4w7g7870RmVpLbY'}
        post = {
            "Firstname": 'vedika',
            "Lastname": 'madhu',
            "Email":'mv@gmail.com',
            "Username": 'Mvedika',
            "Password": 'Madhu@12',
            "MobileNumber": "+919340221920",
            # "Tag": 0,
            "DeviceToken": "string"
            }
        x=requests.post(url=api,json=post,headers=headers)
        print(x)
      





ob=loginscreen()
ob.run()

