from django import forms
from .models import Post

class PostModelForm(forms.ModelForm): ##ModelForm을 상속 받을수도있고 Form을 상속받을수도있다.
    class Meta:
        model = Post
        #fields = ['title','text'] #리스트,튜플 둘다 가능
        fields = ('title','text',) #튜플은 마지막에 , 찍어줘야함








def min_length_5_validator(value):
    if len(value) < 5 :
        #ValidatationError 예외를 강제로 발생시킨다
        raise forms.ValidationError('Text는 5글자 이상 입력해주세요')

## Form을 상속받는 PostForm 클래스 정의
class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea,validators=[min_length_5_validator])