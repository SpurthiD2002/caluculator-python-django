from django.shortcuts import render
from .forms import CalculatorForm

def calculator_view(request):
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data['number1']
            n2 = form.cleaned_data['number2']
            op = form.cleaned_data['operation']
            if op == 'add':
                result = n1 + n2
            elif op == 'subtract':
                result = n1 - n2
            elif op == 'multiply':
                result = n1 * n2
            elif op == 'divide':
                result = n1 / n2 if n2 != 0 else 'Error: Division by zero'
    else:
        form = CalculatorForm()
    return render(request, 'calculator/calculator.html', {'form': form, 'result': result}) 
