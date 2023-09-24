from django.urls import path
from . views import *
urlpatterns = [
    path('', home,name='home'),
    path('detail/<int:id>',detail,name='detail'),
    path('save-comment',save_comment,name='save-comment'),
    path('save-upvote',save_upvote,name='save-upvote'),
    path('save-downvote',save_downvote,name='save-downvote'),
    # User Register
    path('accounts/register/',register,name='register'),
    # Ask QUestion
    path('ask-question',ask_form,name='ask-question'),
    # Tag search
    path('tag/<str:tag>',tag,name='tag'),
    # Tags Page
    path('tags',tags,name='tags'),
    # Profile
    # path('accounts/profile/',profile,name='profile'),
]
