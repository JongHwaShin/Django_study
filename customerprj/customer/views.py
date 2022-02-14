from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def customer_list(request):
    myname = '장고연습프로젝트'
    http_method = request.method  ##객체를 받을 변수, request.method = 속성 # get or post
    # httpresponse 객체를 생성하겠다
    # return HttpResponse('''
    #         <h2>Welcome {name}</h2>
    #         <p>Http Method {method}</p>
    #         <p>Http Headers {hed}</p>
    #         <p>Http Path {mypath}
    #     '''.format(name=myname, method=http_method, hed=request.headers['user-agent'], mypath=request.path))
    customer = Customer.objects.all()

    return render(request,'customer/customer_list.html',{'customer_text':customer})

def customer_detail(request,pk):
    customer = get_object_or_404(Customer,pk=pk)
    return render(request,'customer/customer_detail.html',{'customer_detail':customer})