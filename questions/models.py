from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Test_User(models.Model):
    name = models.CharField(max_length = 100)
    e_mail = models.EmailField(max_length=254)

class Question(models.Model):
    # test_user = models.ForeignKey(Test_User, on_delete = models.CASCADE)
    num = models.IntegerField(validators=[MinValueValidator(1)])
    type = models.CharField(max_length=1, choices=[('M', '객관식'), ('S', '주관식')])
    title = models.CharField(max_length=300)

    #이미지
    image = models.ImageField(blank=True)

    # 객관식
    m1 = models.CharField(max_length=300, blank=True)
    m2 = models.CharField(max_length=300, blank=True)
    m3 = models.CharField(max_length=300, blank=True)
    m4 = models.CharField(max_length=300, blank=True)
  
    # 객관식 답
    answer_m = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], blank=True)

    # 주관식 답
    answer_s = models.CharField(max_length=200, blank=True)
    # 문제 생성 시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)



class User_Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 객관식 사용자 입력
    content_m = models.CharField(max_length=10, blank=True)
    # 주관식 사용자 입력
    content_s = models.CharField(max_length=300, blank=True)
    # 유저 정답 생성 시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

