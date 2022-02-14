from django.urls import path
from . import views

urlpatterns = [
    ## localhost:8000/blog
    path('',views.post_list,name = 'post_list_home'), ##views.post_list 함수를 실행한다. name에 들어온 이름으로 요청이와도 views.함수 를 실행한다.
    ## localhost:8000/blog/post/5
    path('post/<int:pk>',views.post_detail,name = 'post_detail'),
]