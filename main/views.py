from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.

def homepage(request):
    questions = Question.objects.all()

    context = {'questions':questions}
    return render(request, 'main/home.html', context)

def question_page(request, pk):
    question = Question.objects.get(id=pk)

    user_input = request.POST.get('question_input')
    correct_answer = Question.objects.values_list('answer', flat=True).get(id=pk)


    if user_input == correct_answer:
        print('CORRECT!')
        if request.method == 'POST':
            #use this line in saving much better
            new_object = Score.objects.create(score=user_input)
            new_object.save()
        return redirect('home')
    else:
        print('WRONG!')

    context={'question':question, 'user_input':user_input, 'correct_answer':correct_answer}
    return render(request, 'main/question1.html', context)

