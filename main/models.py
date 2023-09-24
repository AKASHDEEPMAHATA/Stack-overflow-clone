from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField 

# Create your models here.


# Custom User Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(blank=True,unique=True)
    bio = models.TextField(max_length=100, blank=True)
    


# Question Model
class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    details = models.TextField()
    # details = RichTextField()
    add_time = models.DateTimeField(auto_now_add=True)
    tags = models.TextField(default='')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Question'


# ------------------------

# Answer Model
class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    details = models.TextField()
    # details = RichTextField()
    add_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.question.title
    
    class Meta:
        verbose_name_plural = 'Answer'


# --------------------------

# Comment Model
class Comment(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_user')
    add_time = models.DateTimeField(auto_now_add=True)
    details = models.TextField(null=True)

    def __str__(self):
        return self.answer.question.title


    class Meta:
        verbose_name_plural = 'Comment'


# ----------------------------
# Upvote
class Upvote(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='upvote_user')

    class Meta:
        verbose_name_plural = 'Upvote'
    def __str__(self):
        return self.answer.question.title

# ----------------------------
# Downvote
class Downvote(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='downvote_user')

    class Meta:
        verbose_name_plural = 'Downvote'

    def __str__(self):
        return self.answer.question.title
