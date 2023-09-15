from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
import json
# Create your views here.


@ensure_csrf_cookie
def calculate(request, operation):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if 'A' in data and 'B' in data:
                a  = data['A']
                b = data['B']
                print(True)
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
            return JsonResponse({'answer': result})
        except:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)