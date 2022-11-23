text_config ="""
MDTextField:
    hint_text :"enter your Last name here"
    helper_text :" enter your name"
    helper_text_mode : "on_focus"
    icon_right: 'android'
    icon_right_color: 'Red'
    pos_hint:{'center_x':0.5,'center_y':0.6}
    size_hint_x:None
    width:300

"""

label_name="""
MDLabel:
    text: "First Name"
    halign: "center"
    
    theme_text_color: "Primary"
    bold: True
    font_style: "H3"
    text_color: "blue"
"""

labellast = """
MDLabel:
    text: "Last Name"
    halign: "left"
    valign: "bottom"
    bold: True
    font_style: "H5"
    theme_text_color: "Custom"
    text_color: (1,0,0,3)
"""

label_name2 = """
MDLabel:
    text: "Custom color"
    halign: "right"
    theme_text_color: "Custom"
    text_color: (236/255,98/255,24/255)
    bold:True
    font_style:"H5"
"""

icon_1 ="""
MDIcon:
    icon:"bullseye-arrow"
    pos_hint:{'center_x':0.5,'center_y':0.4}
"""