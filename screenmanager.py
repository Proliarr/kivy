from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
   
    Button:
        text: 'Goto settings'
        pos_hint:{'center_x':0.5, 'center_y':0.5}
       
        on_press: root.manager.current = 'settings'
    Button:
        text: 'Quit'
        pos_hint:{'center_x':0.5, 'center_y':0.4}

<SettingsScreen>:
    
    Button:
        text: 'My settings button'
        pos_hint:{'center_x':0.5, 'center_y':0.3}
    Button:
        text: 'Back to menu'
        on_press: root.manager.current = 'menu'
        pos_hint:{'center_x':0.5, 'center_y':0.2}
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == '__main__':
    TestApp().run()