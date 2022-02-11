from django.db import models
from django.utils import timezone

class Post(models.Model): # 글 클래스 만들기
    #작성자
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    #제목
    title = models.CharField(max_length=200)
    #내용
    text = models.TextField()
    #작성일
    created_date = models.DateTimeField(default=timezone.now)
    #게시일
    published_date = models.DateTimeField(blank=True, null=True)
    # #임의컬럼
    # test = models.TextField()

    #published_data 필드에 현재날짜를 저장하는 메서드
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #글 저장할때 제목 저장
    def __str__(self):
        return self.title+ '(' +str(self.id) + ')'