from django.db import models

# Create your models here.


class Sport(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)


class League(models.Model):
    sport_id = models.ForeignKey(
        Sport, related_name="sport", on_delete=models.CASCADE, db_column="sport_id"
    )
    name = models.CharField(max_length=200, blank=False, null=False)


class Team(models.Model):
    league_id = models.ForeignKey(
        League, related_name="league", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, blank=False, null=False)
    logo = models.TextField()


class Competition(models.Model):
    league_id = models.ForeignKey(
        League, related_name="league", on_delete=models.CASCADE
    )
    competition_champion = models.ForeignKey(
        Team, related_name="team", on_delete=models.CASCADE
    )
    season = models.CharField(max_length=100, blank=False, null=False)


class Nationality(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)


class Player(models.Model):
    nationality_id = models.ForeignKey(
        Nationality, related_name="nationality", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    pseudonym = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)


class PlayerTeamHistory(models.Model):
    player_id = models.ForeignKey(
        Player, related_name="player", on_delete=models.CASCADE
    )
    team_id = models.ForeignKey(Team, related_name="team", on_delete=models.CASCADE)
