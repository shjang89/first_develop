# questions/forms.py

from django import forms
from .models import Question, Test_User

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        labels = {
            'type' : '문제 유형',
            'num' : '문제 번호', 
            'title' : '문제 내용',
            'm1' : 'A.',
            'm2' : 'B.',
            'm3' : 'C.',
            'm4' : 'D.',
            'answer_m' : '정답',
            'answer_s' : '정답',
            'image' : '이미지 업로드',
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = Test_User
        fields = '__all__'

# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = User_Answer
#         fields = ('question', 'content_m', 'content_s', )
#         labels  = {
#             'answer_m' : '정답',
#             'answer_s' : '정답',
#         }


# class QuestionForm_M(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ('type', 'num', 'title', 'm1', 'm2', 'm3', 'm4', )
#         labels = {
#             'num' : '문제 번호', 
#             'title' : '문제 내용',
#             'm1' : 'A.',
#             'm2' : 'B.',
#             'm3' : 'C.',
#             'm4' : 'D.',
#         }

# class QuestionForm_S(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ('type', 'num', 'title')
#         labels = {
#             'num' : '문제 번호', 
#             'title' : '문제 내용',
#         }

class M_choiceForm(forms.ModelForm):
    pass
