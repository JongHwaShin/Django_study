from django.urls import path
from . import views

urlpatterns = [
    ## localhost:8000/blog
    path('',views.post_list,name = 'post_list_home'), ##views.post_list 함수를 실행한다. name에 들어온 이름으로 요청이와도 views.함수 를 실행한다.
    ## localhost:8000/blog/post/5
    path('post/<int:pk>',views.post_detail,name = 'post_detail'),
    ## localhost:8000/blog/post/new   name = 'post_new' 이 alias는 view의 url + post_new 거기로간다
    path('post/new/',views.post_new, name = 'post_new'),
]