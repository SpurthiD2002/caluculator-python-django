from django import forms

class CalculatorForm(forms.Form):
    number1 = forms.FloatField(label='First Number')
    number2 = forms.FloatField(label='Second Number')
    operation = forms.ChoiceField(
        choices=[
            ('add', 'Add'),
            ('subtract', 'Subtract'),
            ('multiply', 'Multiply'),
            ('divide', 'Divide')
        ],
        label='Operation'
    ) 
