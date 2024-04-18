from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        self.expression = ''
        self.result = ''
        
        layout = BoxLayout(orientation='vertical')
        
        self.display = Button(text='0', font_size=40, size_hint_y=0.75, background_color=[0,0,0,1], color=[1,1,1,1], background_normal='')
        layout.add_widget(self.display)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+']
        ]
        
        for row in buttons:
            row_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=40, background_color=[0,0,0,1], color=[1,1,1,1], background_normal='')
                button.bind(on_press=self.on_button_press)
                row_layout.add_widget(button)
            layout.add_widget(row_layout)
        
        return layout
    
    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.result = str(eval(self.expression))
            except Exception as e:
                self.result = 'Error'
            self.display.text = self.result
            self.expression = self.result
        else:
            if instance.text == 'C':
                self.expression = ''
                self.display.text = ''
            else:
                self.expression += instance.text
                self.display.text = self.expression

if __name__ == '__main__':
    CalculatorApp().run()