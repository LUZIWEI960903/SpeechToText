# from django.shortcuts import render
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
        print(request.FILES)
        Blob = request.FILES['audioData']

        """ 你的 APPID AK SK """
        APP_ID = '16710665'
        API_KEY = 'lAm7pwiagTIHIqksaTRQILnL'
        SECRET_KEY = 'w4KIhKEKrmiNq4kBtD7Cu0hVjXgO2b1N'

        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

        return_file = client.asr(Blob.file.read(), 'wav', 16000, {
            'dev_pid': 1536,
        })
        if return_file['err_no']==0:

        # global data
            data=return_file['result']
            print(data)
            return JsonResponse(data)
        else:
            return HttpResponse('error')
    else:
        # global data
        print(data)
        if len(data)>0:
            return JsonResponse(data)
        return HttpResponse('error')
    # return HttpResponse('ok')
