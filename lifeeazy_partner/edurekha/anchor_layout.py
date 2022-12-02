from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button



class DemoApp(App):
    def build(self):
        layout = AnchorLayout(
            anchor_x = 'left',anchor_y = 'bottom',
        )
        btn=Button(text="anchor layout button",size_hint=(0.2,0.2),background_color =(0.0,25,86,1),color="black")
        layout.add_widget(btn)
        return (layout)

ob = DemoApp()
ob.run()
