from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def ideas(request):
    response_data = {}
    response_data['description'] = ""
    response_data['employerNumbers'] = ""
    response_data['investments'] = ""
    return JsonResponse(response_data)


