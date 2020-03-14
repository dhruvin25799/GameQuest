from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=100, blank=False)
    rating = models.IntegerField()
    description = models.CharField(max_length=500)
    hours_played = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    """def update_hours(sender, **kwargs):
        session = kwargs['instance']
        if kwargs['created']:
            game = session.game
            game.hours_played = game.hours_played + session.duration
            game.save()"""

    #post_save.connect(update_hours, sender=Session)
