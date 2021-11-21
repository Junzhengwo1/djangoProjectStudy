from django.shortcuts import render


# Create your views here.

def home(request):
    # print("项目开始……" + request)
    return render(request, 'home.html')  # render用来打开html文件进行渲染
