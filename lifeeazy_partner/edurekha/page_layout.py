from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button

class page_layout(PageLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.btn = Button(
            text = 'btn one page',
            pos_hint={'x': 0.4, 'y': 0.3})
        self.btn2 = Button(
            text = 'btn two page',
            pos_hint={'x': 0.4, 'y': 0.3})
        self.btn3 = Button(
            text = 'btn three page',
            pos_hint={'x': 0.4, 'y': 0.3})
        self.add_widget(self.btn)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)






class DemoApp(App):
    def build(self):
        return page_layout()

ob= DemoApp()
ob.run()