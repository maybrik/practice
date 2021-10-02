from django.db import models

from django.conf import settings


class PostManager(models.Manager):
    use_for_related_fields = True

    def published(self):
        return Post.objects.filter(is_published=True)

    def get_query_set(self):
        return PostQuerySet(self.model)


class Post(models.Model):
    objects = PostManager()
    label = models.CharField(max_length=160, required=True)
    short_description = models.TextField(max_length=300, required=True)
    image = models.UrlField(max_length=200)
    full_description = models.CharField(max_length=1000, required=True)
    user = models.ForeingKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.label


# + admin page
class Comment(models.Model):
    objects = PostManager()
    username = models.CharField(max_length=20, required=True)
    text = models.CharField(max_length=300, required=True)
    for_post = models.ForeingKey(Post, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.text

