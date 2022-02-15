from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from .forms import PostModelForm,PostForm

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


# 글 등록(Form)사용
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)## 검증을 통과한 입력데이터 출력
            clean_data_dict = form.cleaned_data
            #create() 함수가 호출되면 등록처리가 이루어진다.
            post = Post.objects.create(
                author = request.user,
                title = clean_data_dict['title'],
                text = clean_data_dict['text'],
                published_date = timezone.now()

            )
            return redirect('post_detail',pk = post.pk)
    else:
        form = PostForm() ##title,text 가 비워져있는 화면나옴

    return render(request,'blog/post_edit.html',{'postform':form})

#글 등록(ModelForm 사용)
def post_new_modelform(request):
    #등록버튼을 눌러서 등록을 요청하는 경우
    if request.method == "POST":
        post_form = PostModelForm(request.POST)
        if post_form.is_valid():
            #form 객체의 save() 호출하면 Model 객체가 생성되어진다
            post = post_form.save(commit=False)
            #로그인된 username을 작성자 필드에 저장
            post.author = request.user
            #현재날짜시간을 게시일자 필드에 저장
            post.published_date = timezone.now()
            #post객체가 저장되면서 insert처리가 되어진다.
            post.save()
            #등록 후에 상세페이지로 가기위함(리다이렉션) 객체의 pk번호를 이용하여
            return redirect('post_detail', pk=post.pk)
    else:
        post_form = PostModelForm()


    return render(request,'blog/post_edit.html',{'postform':post_form})
