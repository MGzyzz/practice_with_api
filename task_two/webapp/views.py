import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView

# Create your views here.


class CalculatorView(TemplateView):
    template_name = 'index.html'

    def calculate(request, operation):
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                if 'A' in data and 'B' in data:
                    a = data['A']
                    b = data['B']
                    if operation == 'add':
                        result = a + b
                    elif operation == 'subtract':
                        result = a - b
                    elif operation == 'multiply':
                        result = a * b
                    elif operation == 'divide':
                        if b == 0:
                            return JsonResponse({'error': 'Division by zero'}, status=400)
                        result = a / b
                    else:
                        return JsonResponse({'error': 'Invalid operation'}, status=400)
                    print('work')
                    print(result)
                    return JsonResponse({'result': result})
            except ValueError:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)

