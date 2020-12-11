from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class MainApp(App):


    def build(self):
        
        self.operators = ["/","*","+","-"]
        self.last_was_operator = None
        self.last_button = None
        self.special_op = ["sin", "cos", "tan", "sqrt"]
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)

        main_layout.add_widget(self.solution)

        buttons = [
            ["1","2","3","/","sqrt"],
            ["4","5","6","*","sin"],
            ["7","8","9","-","cos"],
            [".","0","C","+","tan"],
        ]


        for row in buttons:
            horizontal_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x':0.5,'center_y':0.5})

                button.bind(on_press=self.on_button_press)
                horizontal_layout.add_widget(button)
            main_layout.add_widget(horizontal_layout)

        
        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        
        current_text = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        else:

            if current_text and (self.last_was_operator and button_text in self.operators):
                
                return
            elif current_text == "" and button_text in self.operators:
                # First cannot be a
                return
            else:
                
                new_text = current_text + button_text
                if button_text in self.special_op:
                    new_text += "("
                self.solution.text  = new_text

            self.last_button = button_text
            self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text

        if text:
            if "sin" in text:
                if text.index("sin") == 0:
                    self.solution.text = str(math.sin(float(text[4:])))
                else:
                    self.solution.text = "Error"
            elif "cos" in text:
                if text.index("cos") == 0:
                    self.solution.text = str(math.cos(float(text[4:])))
                else:
                    self.solution.text = "Error"
            elif "tan" in text:
                if text.index("tan") == 0:
                    self.solution.text = str(math.tan(float(text[4:])))
                else:
                    self.solution.text = "Error"
            elif "sqrt" in text:
                if text.index("sqrt") == 0:
                    self.solution.text = str(math.sqrt(float(text[5:])))
                else:
                    self.solution.text = "Error"
            else:
                solution = str(eval(self.solution.text))
                self.solution.text= solution

if __name__ == "__main__":
    app = MainApp()
    app.run()
