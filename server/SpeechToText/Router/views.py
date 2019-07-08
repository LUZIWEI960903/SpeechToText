# from django.shortcuts import render
import os
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from aip import AipSpeech
# Create your views here.

data = str()
count=0
@csrf_exempt
def index(request):
    global count,data
    count+=1
    print(count)
    if request.method == "POST":
        # print(request.FILES)
        # print(type(request.FILES))
        Blob = request.FILES['audioData']
        # print(Blob)
        # print(type(Blob))
        # print(bin(hash(Blob)))
        # print(id(Blob))
        print(Blob.file)

        """ 你的 APPID AK SK """
        APP_ID = '16710665'
        API_KEY = 'lAm7pwiagTIHIqksaTRQILnL'
        SECRET_KEY = 'w4KIhKEKrmiNq4kBtD7Cu0hVjXgO2b1N'

        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


        return_file = client.asr(Blob.file.read(), 'wav', 16000, {
            'dev_pid': 1536,
        })
        print(return_file)
        if return_file['err_no']==0:
        # global data
            data=return_file['result']
            return HttpResponse(data)
        else:
            return HttpResponse('error')
    else:
        # global data
        # print(data)
        if len(data)>0:
            return HttpResponse(data)
        else:
            return HttpResponse('error')
    # return HttpResponse('ok')
