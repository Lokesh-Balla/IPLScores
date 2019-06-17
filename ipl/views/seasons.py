from django.views import View
from ipl import models
from django.shortcuts import render, redirect
from django.urls import resolve


class SesonsView(View):
    def get(self, request, **kwargs):
        year = models.Seasons.objects.get(year=kwargs['year'])
        seasons = models.Seasons.objects.all()
        tables = models.Matches.objects.values_list('team1', 'team2',
                                                    'city', 'tossWinner', 'tossDecision', 'winner', 'playerOfTheMatch',
                                                    'match_id').filter(year=year)
        return render(
            request,
            template_name='ipl/seasons.html',
            context={
                'year': kwargs['year'],
                'seasons': seasons,
                'tables': tables,
            },
        )

    def post(self, request, **kwargs):
        pass


class MatchView(View):
    def get(self, request, **kwargs):
        tables = models.Matches.objects.values_list('tossWinner', 'tossDecision',
                                                    'winner', 'playerOfTheMatch').get(match_id=kwargs['mid'])
        match_id=models.Matches.objects.get(match_id=kwargs['mid'])
        balls = models.Deliveries.objects.values().filter(matchId=match_id)
        return render(
            request,
            template_name='ipl/matchs.html',
            context={
                'year': kwargs['year'],
                'info': tables,
                'balls': balls,
            },
        )
