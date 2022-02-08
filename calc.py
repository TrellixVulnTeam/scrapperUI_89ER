from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#Set the app size

Window.size = (500,700)

Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = ''
    #Create a function for pressing buttons
    def button_press(self, button):
        #Create a varibale that cointains what is in the tect boz
        prior = self.ids.calc_input.text
        #Check if prior = 0
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
    #Create addition function
    def add(self):
        prior = self.ids.calc_input.text 
        # add a + to the text
        self.ids.calc_input.text = f'{prior}+'
    def subtract(self):
        prior = self.ids.calc_input.text 
        # add a - to the text
        self.ids.calc_input.text = f'{prior}-'
    def multiply(self):
        prior = self.ids.calc_input.text 
        # add a x to the text
        self.ids.calc_input.text = f'{prior}x'
    def divide(self):
        prior = self.ids.calc_input.text 
        # add a / to the text
        self.ids.calc_input.text = f'{prior}/'
    #create equals function
    def equals(self):
        prior = self.ids.calc_input.text
        #addition
        if '+' in prior:
            num_list = prior.split('+')
            answer = 0
            #loop in the list
            for number in num_list:
                answer = answer + int(number)
            #Print the answer in the tect box
        self.ids.calc_input.text = str(answer)

class Calc(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)
        return MyLayout()

if __name__ == '__main__':
    Calc().run()