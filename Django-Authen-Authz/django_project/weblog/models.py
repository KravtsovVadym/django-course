from django.db import models
from django.db.models.functions import Lower
from django.conf import settings
from cloudinary.models import CloudinaryField

# >---------------------------------------<
# (Tag model) ----------------------------<
# >---------------------------------------<
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

# >---------------------------------------<
# (Post model) ---------------------------<
# >---------------------------------------<
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(verbose_name="Title", max_length=100)
    article = models.TextField(verbose_name="Article")
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    image = CloudinaryField(verbose_name="image", blank=True)

    class Meta:
        ordering = ["-created_at"]

# >---------------------------------------<
# (Comment model) ------------------------<
# >---------------------------------------<
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="Comments")
    author = models.CharField(verbose_name="Author", max_length=100)
    text = models.TextField()


