from django.db import models
from django.db.models.functions import Lower
from django.conf import settings
from cloudinary.models import CloudinaryField


class Tag(models.Model):
    name = models.CharField(verbose_name="Tag", max_length=10, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"),  # Makes uniqueness through lower()
                name="unique_lower_name_tag",
            )  # Technical identifier
        ]
        ordering = ["name"]  # Sorted (name Tag) alphabetically
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(verbose_name="Title", max_length=100)
    article = models.TextField(verbose_name="Articte")
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="Comments")
    author = models.CharField(verbose_name="Author", max_length=100)
    text = models.TextField()


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="Images")
    image = CloudinaryField("Image")
