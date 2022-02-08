from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('design.kv')

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)
    
    #initialize infinite keywords

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        #print(f'Hello {name}, you like {pizza} and your color is {color}')
        #print to the screen
        #self.add_widget(Label(text=f'Hello {name}, you like {pizza} and your color is {color}'))
        print(f'Hello {name}, you like {pizza} and your color is {color}')

        #Clear the input boxes
        self.name.text= ""
        self.pizza.text= ""
        self.color.text= ""


class Scrapper(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    Scrapper().run()