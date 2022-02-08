from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('updatelabel.kv')

class MyLayout(Widget):
    def press(self):
        #Create variables for our widgets
        name = self.ids.name_input.text
        
        #Update the label
        self.ids.name_label.text = f' Hello {name}'
        self.ids.name_input.text = ''




class Scrapper(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)
        return MyLayout()

if __name__ == '__main__':
    Scrapper().run()