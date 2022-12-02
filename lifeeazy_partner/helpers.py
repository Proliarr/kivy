user_text ="""
MDTextField:
    hint_text:"Username/Email/Mobile"
    pos_hint:{'center_x':0.5,'center_y':0.7}
    size_hint_x:None
    width:300
    icon_right:"account"
    


"""

password ="""
MDTextField:
    hint_text:"password"
    pos_hint:{'center_x':0.5,'center_y':0.6}
    size_hint_x:None
    width:300
    icon_right:'eye-off'


"""

not_signed="""
MDLabel:
    text:"Not Signedup Yet?"
    theme_text_color: "Custom"
    text_color:'black'

"""


login_btn="""
MDRectangleFlatButton:
    text:"Login"
    pos_hint:{'center_x':0.5,'center_y':0.3}
    on_release:show_data
    
"""
img="""
Image:
    source:r'lifeeazyicon.png'
    pos_hint:{'center_x':0.5,'center_y':0.9}

"""

