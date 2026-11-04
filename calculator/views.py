from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class AdditionView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 + n2
        print(request_body)
        data = {
            "sum": result
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class SubtractionView(View):
    def post(self, request):
        form_data = loads(request.body)
        n1 = float(form_data.get('num1'))
        n2 = float(form_data.get('num2'))

        result = n1 - n2
        data = {
            "difference": result
        }
        return JsonResponse(data)
    
    
@method_decorator(csrf_exempt, name='dispatch')
class DivisionView(View):
    def post(self, request):
        form_data = loads(request.body)
        n1 = float(form_data.get('num1'))
        n2 = float(form_data.get('num2'))

        if n2 == 0:
            return JsonResponse({"error": "Cannot divide by zero"}, status=400)

        result = n1 / n2
        data = {
            "quotient": result
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class ModuloView(View):
    def post(self, request):
        form_data = loads(request.body)
        n1 = float(form_data.get('num1'))
        n2 = float(form_data.get('num2'))

        if n2 == 0:
            return JsonResponse({"error": "Cannot take modulo by zero"}, status=400)

        result = n1 % n2
        data = {
            "remainder": result
        }
        return JsonResponse(data)

    
@method_decorator(csrf_exempt, name='dispatch')
class MultiplicationView(View):
    def post(self, request):
        form_data = loads(request.body)
        n1 = float(form_data.get('num1'))
        n2 = float(form_data.get('num2'))

        result = n1 * n2
        data = {
            "product": result
        }
        return JsonResponse(data)

    
@method_decorator(csrf_exempt, name='dispatch')
class PercentageView(View):
    def post(self, request):
        form_data = loads(request.body)
        n1 = float(form_data.get('num1'))
        n2 = float(form_data.get('num2'))

        if n2 == 0:
            return JsonResponse({"error": "num2 cannot be zero"}, status=400)

        result = (n1 / n2) * 100
        data = {
            "percentage": result
        }
        return JsonResponse(data)



@method_decorator(csrf_exempt, name='dispatch')
class BMIView(View):
    def post(self, request):
        form_data = loads(request.body)
        weight = float(form_data.get('weight'))
        height = float(form_data.get('height')) /100
        bmi = weight / (height **2)
        result={
            "BMI":bmi
        }
        return JsonResponse(result)



@method_decorator(csrf_exempt, name='dispatch')
class SimpleInterestView(View):
    def post(self, request):
        form_data = loads(request.body)
        principal = float(form_data.get('principal'))
        rate = float(form_data.get('rate'))
        time = float(form_data.get('time'))
        simple_interest = (principal * rate * time) / 100
        result = {
            "principal": principal,
            "rate": rate,
            "time": time,
            "simpleinterest": simple_interest
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class ElectricityBillView(View):
    def post(self, request):
        form_data = loads(request.body)
        units = float(form_data.get('units'))
        rate = float(form_data.get('rate'))
        bill = units * rate
        result = {
            "units": units,
            "rate": rate,
            "bill": bill
        }
        return JsonResponse(result)