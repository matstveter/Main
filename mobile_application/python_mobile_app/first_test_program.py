from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.image import Image


class MainApp(App):

    def build(self):
        # label = Label(text="First Kivy App", size_hint=(.7, .7), pos_hint={'center_x': 0.5,'center_y': 0.75 })
    
        img = Image(source='kivy.jpeg', size_hint=(1, 0.5), pos_hint={'center_x':.5, 'center_y':0.25})

        return img #, label
    

if __name__ == "__main__":
    app = MainApp()
    app.run()
