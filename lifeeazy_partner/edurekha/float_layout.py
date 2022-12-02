from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class Float_layout(FloatLayout):
    def __init__(self,**kwargs):    
        super().__init__(**kwargs)
        self.btn = Button(
            text ='btn Float',size_hint =(0.4,0.4),
                    pos_hint={'x':0.5,'y':0.8})
        self.btn2 = Button(text ='btn Float2',
                    size_hint =(0.4,0.4),
                    pos_hint={'x':0.5,'y':0.3})
        self.add_widget(self.btn)
        self.add_widget(self.btn2)
            

class DemoApp(App):
    def build(self):
        return Float_layout()


ob = DemoApp()
ob.run()