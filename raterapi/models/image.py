from django.db import models


class Image(models.Model):
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="game_images")
    player = models.ForeignKey(
        "Player", on_delete=models.CASCADE, related_name="uploaded_images")
