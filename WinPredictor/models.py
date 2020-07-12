from django.db import models

# Create your models here.
class Approval(models.Model) :
    BATTING_CHOICES = (('RCB', 'Royal Chalengers Bangalore'), ('KKR', 'Kolkata Knight Riders'),
    ('MI', 'Mumbai Indians'), ('CSK', 'Chennai Super Kings'), ('DC', 'Delhi Capitals'))

    CHASING_CHOICES = (('RCB', 'Royal Chalengers Bangalore'), ('KKR', 'Kolkata Knight Riders'),
    ('MI', 'Mumbai Indians'), ('CSK', 'Chennai Super Kings'), ('DC', 'Delhi Capitals'))

    username = models.CharField(max_length = 25)
    batting = models.CharField(max_length = 10, choices = BATTING_CHOICES)
    chasing = models.CharField(max_length = 10, choices = CHASING_CHOICES)
    venue = models.CharField(max_length = 50)
    score = models.IntegerField(default = 0)
    wickets = models.IntegerField(default = 0)
    balls_left = models.IntegerField(default = 0)
    runs_l5 = models.IntegerField(default = 0)
    wick_l5 = models.IntegerField(default = 0)
    target = models.IntegerField(default = 0)

    def __str__(self) :
        return self.username
