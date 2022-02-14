from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

# Create your views here.
# Views 내에 선언된 함수로 인자로 HttpRequest 라는 객체로 Django가 주입시켜준다.





##글목록 함수
def post_list(request):
    myname = '장고웹프레임워크'

    http_method = request.method ##객체를 받을 변수, request.method = 속성 # get or post
    # httpresponse 객체를 생성하겠다


    #
    # return HttpResponse('''
    #     <h2>Welcome {name}</h2>
    #     <p>Http Method {method}</p>
    #     <p>Http Headers {hed}</p>
    #     <p>Http Path {mypath}
    # '''.format(name=myname,method=http_method,hed=request.headers['user-agent'],mypath=request.path))
    # #응답결과로 준다!
    # return render(request,'blog/post_list.html') ##render는 결국 HttpResponse객체를 반환한다.
    posts = Post.objects.filter(published_date__lte = timezone.now()).\
        order_by('published_date')
    return render(request,'blog/post_list.html',{'post_list':posts}) ##html에서 for loop에서 쓰이는 post_lisst



##글상세정보

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk) #받은 pk값을 준다
    return render(request,'blog/post_detail.html',{'post_key':post}) ##마지막 파라미터는 post객체를 사용하기위해 pk로 객체를 읽어옴 {}에서 앞의 post는 html에서 사용할 key값이고 뒤에
#뒤에 post는 위에서 받은 객체 post
