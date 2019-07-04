# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from aip import AipSpeech
# Create your views here.


@csrf_exempt
def index(request):

    if request.method == "POST":
        print(request.FILES)
        Blob = request.FILES['audioData']
        # print(type(Blob))
        # print(Blob.file)
        # data_base64 = base64.b64encode(Blob.file.read())
        # print(data_base64)

        """ 你的 APPID AK SK """
        APP_ID = '16710665'
        API_KEY = 'lAm7pwiagTIHIqksaTRQILnL'
        SECRET_KEY = 'w4KIhKEKrmiNq4kBtD7Cu0hVjXgO2b1N'

        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

        return_file = client.asr(Blob.file.read(), 'wav', 16000, {
            'dev_pid': 1536,
        })
        # print(return_file)
        # if return_file['err_no'] == 0:
        print(return_file)
        if return_file['err_no']==0:
            return JsonResponse({'data':return_file['result']})
        else :
            return JsonResponse({'data':'error'})
