from django.shortcuts import render, redirect

# Create your views here.
from .models import Question, User_Answer, Test_User
# from .forms import QuestionForm, AnswerForm
from .forms import QuestionForm, UserForm


def index(request):
    # 사용자가 이전에 응답을 제출했는지 확인합니다.
    # user_answer_exists = User_Answer.objects.exists()

    questions = Question.objects.order_by('num')

    context = {
        'questions' : questions,
        # 'user_answer_exists': user_answer_exists,
    }
    return render(request, 'questions/index.html', context)

# def index(request):
    
#     questions = Question.objects.order_by('num')
#     question_form = AnswerForm()

#     context = {
#         'question_form' : question_form,
#         'questions' : questions,
#     }
#     return render(request, 'questions/index.html', context)

def detail(request, pk):
    question = Question.objects.get(pk = pk)

    context = {
        'question' : question,
    }

    return render(request, 'questions/detail.html', context)


# CRUD 구현
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            question = form.save()
            return redirect('questions:detail', question.pk)
    else:
        form = QuestionForm()

    context = {
        'form' : form,
        # 'userform' : userform,
    }
    return render(request, 'questions/create.html', context)


def delete(request, pk):
    question = Question.objects.get(pk = pk)
    question.delete()
    return redirect('questions:index')

def complete(request):
    if request.method == 'POST':
        # 사용자가 선택한 질문의 ID를 폼으로부터 받아옴
        # selected_question_id = request.POST.get('question_id')
        # 선택한 질문 객체 가져오기
        # selected_question = Question.objects.get(pk=selected_question_id)
        # 답변 폼 생성 및 유효성 검사
        # answer_form = AnswerForm(request.POST)

        user_answers = []

        for key, value in request.POST.items():
            if key.endswith('-select'):
                question_pk, question_type = key.split('-')[:-1]
                answer = {
                    'question_id': int(question_pk),
                    'content_m': value if question_type == 'M' else '',
                    'content_s': value if question_type == 'S' else '',
                }
                user_answers.append(answer)

        # user_answers에 있는 데이터를 User_Answer 모델에 저장
        for answer_data in user_answers:
            question = Question.objects.get(pk=answer_data['question_id'])
            # 해당 사용자의 이전 답변 삭제
            
            user_answer = User_Answer.objects.create(
                question=question,
                content_m=answer_data['content_m'],
                content_s=answer_data['content_s']
            )

        return redirect('questions:complete')
    else:
        return render(request, 'questions/complete.html')
        


        # if answer_form.is_valid():
            
            # DB에 저장되기 전에 답변 인스턴스를 가져오고 선택한 질문과 연결
            # answer = answer_form.save(commit=False)
            # answer.question = selected_question  # 선택한 질문과 연결
            # answer.save()  # 답변 저장
            # return redirect('questions:complete')
    # else:
    #     # GET 요청 시, 모든 질문을 가져와서 보여줌
    #     questions = Question.objects.all()
    #     answer_form = AnswerForm()
    #     context = {
    #         'questions': questions,
    #         'answer_form': answer_form,
    #     }
    # return render(request, 'questions/index.html', context)


    # if request.method == 'POST':
    #     form2 = AnswerForm(request.POST)
    #     print(form2)
    #     if form2.is_valid():
    #         answer = form2.save()
    #         return redirect('questions:complete', answer)
    # else:
    #     form2 = AnswerForm()

    # context = {
    #     'form2' : form2,
    # }


def exam(request):
    questions = Question.objects.order_by('num')

    context = {
        'questions' : questions,
    }
    return render(request, 'questions/exam.html', context)


def grading(request):
    questions = Question.objects.order_by('num')
    user_answers = User_Answer.objects.order_by('question_id')
    result = []
    total = 0
    for question, user_answer in zip(questions, user_answers):
        if question.type == 'M':
            answer = question.answer_m
        else:
            answer = question.answer_s
        if question.type == 'M':
            content = user_answer.content_m
        else:
            content = user_answer.content_s
        if answer == content:
            grade = 5
        else:
            grade = 0
        total += grade
        result.append({
            'name' : '',
            'e_mail' :  '',
            'created_at' : user_answer.created_at,
            'updated_at' : user_answer.updated_at,
            'num' : question.num,
            'content' : content,
            'answer': answer,
            'grade' : grade,
        })

    context = {
        'result' : result,
        'total' : total,
    }
    print(result)
    return render(request, 'questions/grading.html', context)

def user(request):
    if request.method == 'POST':
        # global userform
        userform = UserForm(request.POST)
    # print(form)
        if userform.is_valid():
            question = userform.save()
            return redirect('questions:exam')
    else:
        userform = UserForm()

    context = {
        'userform' : userform,
    }
    return render(request, 'questions/user.html', context)