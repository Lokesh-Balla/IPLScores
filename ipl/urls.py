from django.urls import include, path
from ipl.views import *

urlpatterns = [
    path('seasons/<int:year>', SesonsView.as_view(), name='seasonsview'),
    path('seasons/<int:year>/match/<int:mid>', MatchView.as_view(), name='matchview'),

    path('login', LogIn.as_view(), name='login'),
    path('signup', SignUp.as_view(), name='signup'),
    path('logout', Logout.as_view(), name='logout'),
]