from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.num1 = TextInput(multiline=False, input_filter='float', hint_text='Number 1')
        self.num2 = TextInput(multiline=False, input_filter='float', hint_text='Number 2')
        self.result = Label(text='Result:')

        button_layout = BoxLayout()
        add_button = Button(text='Add')
        sub_button = Button(text='Subtract')
        mul_button = Button(text='Multiply')
        div_button = Button(text='Divide')

        add_button.bind(on_press=self.add)
        sub_button.bind(on_press=self.subtract)
        mul_button.bind(on_press=self.multiply)
        div_button.bind(on_press=self.divide)

        button_layout.add_widget(add_button)
        button_layout.add_widget(sub_button)
        button_layout.add_widget(mul_button)
        button_layout.add_widget(div_button)

        layout.add_widget(self.num1)
        layout.add_widget(self.num2)
        layout.add_widget(button_layout)
        layout.add_widget(self.result)

        return layout

    def add(self, instance):
        num1 = float(self.num1.text)
        num2 = float(self.num2.text)
        self.result.text = f'Result: {num1 + num2}'

    def subtract(self, instance):
        num1 = float(self.num1.text)
        num2 = float(self.num2.text)
        self.result.text = f'Result: {num1 - num2}'

    def multiply(self, instance):
        num1 = float(self.num1.text)
        num2 = float(self.num2.text)
        self.result.text = f'Result: {num1 * num2}'

    def divide(self, instance):
        num1 = float(self.num1.text)
        num2 = float(self.num2.text)
        if num2 != 0:
            self.result.text = f'Result: {num1 / num2}'
        else:
            self.result.text = 'Error: Division by zero'


if __name__ == '__main__':
    CalculatorApp().run()
