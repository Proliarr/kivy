from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
Window.size = (300,500)
KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Proliar's Heart"
        left_action_items: [["menu", lambda x: app.navigation_draw()]]
        right_action_items: [["dots-vertical", lambda x: nav_draw.toggle_nav_draw()]]
    
        elevation:5
   
    MDLabel:
        text: "I LOVE YOU Wiffy"
        halign: "center"
  

'''


class vedika(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Cyan'
        return Builder.load_string(KV)
    def navigation_draw(self):
        print('madhu')


vedika().run()