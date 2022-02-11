from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Views 내에 선언된 함수로 인자로 HttpRequest 라는 객체로 Django가 주입시켜준다.
def post_list(request):
    myname = '장고웹프레임워크'

    http_method = request.method ##객체를 받을 변수, request.method = 속성 # get or post
    # httpresponse 객체를 생성하겠다
    return HttpResponse('''  
        <h2>Welcome {name}</h2>
        <p>Http Method {method}</p>         
        <p>Http Headers {hed}</p>
        <p>Http Path {mypath}
    '''.format(name=myname,method=http_method,hed=request.headers['user-agent'],mypath=request.path))
    #응답결과로 준다!