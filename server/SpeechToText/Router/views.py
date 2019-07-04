from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
# Create your views here.


@csrf_exempt
def index(request):

    if request.method == "POST":
        print(request.FILES)
        Blob = request.FILES['audioData']
        # print(type(Blob))
        # print(Blob.file)
        data_base64 = base64.b64encode(Blob.file.read())
        print(data_base64)

    return JsonResponse({'ok': 'ok'})
