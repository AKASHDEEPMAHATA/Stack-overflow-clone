from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from . models import *
from django.core.paginator import Paginator
from . forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count

# Create your views here.


# Home Page
def home(request):

    if 'search' in request.GET:
        search = request.GET['search']
        qstn = Question.objects.annotate(total_comments=Count('answer__comment')).filter(title__icontains=search).order_by('-id')
    else:
        qstn = Question.objects.annotate(total_comments=Count('answer__comment')).all().order_by('-id')

    paginator = Paginator(qstn,2)
    page_no = request.GET.get('page', 1)
    qstn = paginator.page(page_no)



    return render(request,'home.html',{'questions':qstn,})

# ----------------------------------------------------
# Question Detail Page
def detail(request,id):
    qstn = Question.objects.get(pk=id)
    tags = qstn.tags.split(',')
    answer = Answer.objects.filter(question=qstn)

    answerform=AnswerForm
    if request.method=='POST':
        answerData=AnswerForm(request.POST)
        if answerData.is_valid():
            ans=answerData.save(commit=False)
            ans.question=qstn
            ans.user=request.user
            ans.save()
            messages.success(request,'Answer has been submitted.')

    return render(request,'detail.html',{'questions':qstn,'tags':tags,'answer':answer,'answerform':answerform,})

#----------------------------------------------------
# Save Comment
def save_comment(request):
    if request.method=='POST':
        comment=request.POST.get('comment')
        answerid=request.POST.get('answerid')
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        Comment.objects.create(
            answer=answer,
            details=comment,
            user=user
        )
        return JsonResponse({'bool':True})

# -----------------------------------------------------
# Save Upvote
def save_upvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=Upvote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            Upvote.objects.create(
                answer=answer,
                user=user
            )
            return JsonResponse({'bool':True})

# -----------------------------------------------------
# Save Downvote
def save_downvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=Downvote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            Downvote.objects.create(
                answer=answer,
                user=user
            )
            return JsonResponse({'bool':True})
        
# --------------------------------------------
# User Register
def register(request):
    form=UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been registered!!')
    return render(request,'registration/register.html',{'form':form})

# -------------------------------------------------

# Question ask
def ask_form(request):
    form=QuestionForm
    if request.method=='POST':
        questForm=QuestionForm(request.POST)
        if questForm.is_valid():
            questForm=questForm.save(commit=False)
            questForm.user=request.user
            questForm.save()
            messages.success(request,'Question has been added.')
    return render(request,'ask-question.html',{'form':form})


# -----------------------------------------------
# Questions according to tag
def tag(request,tag):
    quests=Question.objects.annotate(total_comments=Count('answer__comment')).filter(tags__icontains=tag).order_by('-id')
    paginator=Paginator(quests,10)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    
    return render(request,'tag.html',{'quests':quests,'tag':tag})

# --------------------------------------------------

# Tags Page
def tags(request):
    quests=Question.objects.all()
    tags=[]
    for quest in quests:
        qtags=[tag.strip() for tag in quest.tags.split(',')]
        for tag in qtags:
            if tag not in tags:
                tags.append(tag)
    # Fetch Questions
    tag_with_count=[]
    for tag in tags:
        tag_data={
            'name':tag,
            'count':Question.objects.filter(tags__icontains=tag).count()
        }
        tag_with_count.append(tag_data)
        
    return render(request,'tags.html',{'tags':tag_with_count})


# -------------------------------------------------

# Profile
def profile(request):
    quests=Question.objects.filter(user=request.user).order_by('-id')
    answers=Answer.objects.filter(user=request.user).order_by('-id')
    comments=Comment.objects.filter(user=request.user).order_by('-id')
    upvotes=Upvote.objects.filter(user=request.user).order_by('-id')
    downvotes=Downvote.objects.filter(user=request.user).order_by('-id')
    if request.method=='POST':
        profileForm=ProfileForm(request.POST,instance=request.user)
        if profileForm.is_valid():
            profileForm.save()
            messages.success(request,'Profile has been updated.')
    form=ProfileForm(instance=request.user)
    return render(request,'registration/profile.html',{
        'form':form,
        'quests':quests,
        'answers':answers,
        'comments':comments,
        'upvotes':upvotes,
        'downvotes':downvotes,
    })