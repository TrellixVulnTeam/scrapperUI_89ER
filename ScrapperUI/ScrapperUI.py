from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('scrapperdesign.kv')

class MyLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)
    
    #initialize infinite keywords

    def clear(self):
        self.ids.keywords_input.text = ''
        self.ids.limit_input.text = ''
        self.ids.spinner.text = 'Sencilla'

    def spinner_clicked(self, value):
        self.ids.spinner.text = value
    
    def initialize_scrapping(self, value):
        if self.ids.keywords_input.text and self.ids.limit_input.text:
            if value == 'Completa':
                self.ids.status_label.text = "Estatus: Conectando para realizar búsqueda completa"
                self.ids.status_label.color = (0,1,0,1)
            else:
                self.ids.status_label.text = "Estatus: Conectando para realizar búsqueda sencilla"
                self.ids.status_label.color = (0,1,0,1)
        elif self.ids.keywords_input.text :
            self.ids.status_label.text = "Introduce un límite de resultados"
            self.ids.status_label.color = (1,0,0,1)
        elif self.ids.limit_input.text :
            self.ids.status_label.text = "Introduce los conceptos de búsqueda"
            self.ids.status_label.color = (1,0,0,1)



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
        return MyLayout()

if __name__ == '__main__':
    Scrapper().run()