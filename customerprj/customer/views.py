from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def customer_list(request):
    myname = '장고연습프로젝트'
    http_method = request.method  ##객체를 받을 변수, request.method = 속성 # get or post
    # httpresponse 객체를 생성하겠다
    return HttpResponse('''  
            <h2>Welcome {name}</h2>
            <p>Http Method {method}</p>         
            <p>Http Headers {hed}</p>
            <p>Http Path {mypath}
        '''.format(name=myname, method=http_method, hed=request.headers['user-agent'], mypath=request.path))