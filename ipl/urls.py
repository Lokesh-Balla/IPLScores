from django.urls import include, path
from ipl.views import *

urlpatterns = [
    path('seasons/<int:year>', SesonsView.as_view(), name='seasonsview'),
    path('seasons/<int:year>/match/<int:mid>', MatchView.as_view(), name='matchview'),
]