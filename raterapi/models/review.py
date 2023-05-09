from django.db import models


class Review(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField()
    player = models.ForeignKey(
        "Player", on_delete=models.CASCADE, related_name="submitted_reviews")
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE, related_name="reviews")
