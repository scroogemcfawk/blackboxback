from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random

@csrf_exempt
def ideas(request):
    response_data = {}
    try:
        with open('texts_generated.txt', 'r') as f:
            text = []
            lines = f.readlines()
            for line in lines:
                text.append(line.strip())

        with open('cost_predicted.txt', 'r') as f:
            cost = []
            lines = f.readlines()
            for line in lines:
                cost.append(line.strip())

        with open('emp_predicted.txt', 'r') as f:
            emp = []
            lines = f.readlines()
            for line in lines:
                emp.append(line.strip())

        a = random.randint(0, 206)

        response_data['description'] = text[a]
        response_data['employerNumbers'] = cost[a]
        response_data['investments'] = emp[a]
    except Exception as exc:
        response_data['description'] = "Unable to generate an idea {}".format(exc)
        response_data['employerNumbers'] = "undefined"
        response_data['investments'] = "undefined"

    return JsonResponse(response_data)


