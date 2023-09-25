from datetime import datetime
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')  # A CharField for the post title.
    slug = models.CharField(null=True, blank=True, max_length=150, verbose_name='Slug')  # A CharField for a URL slug (can be blank).
    text = models.TextField(verbose_name='Description')  # A TextField for the post content.
    preview = models.ImageField(null=True, blank=True, verbose_name='Preview')  # An ImageField for a post preview image (can be blank).
    made_date = models.DateField(default=datetime.now, verbose_name='Creation Date')  # A DateField representing the date the post was created.
    is_published = models.BooleanField(default=True, verbose_name='Publication Status')  # A BooleanField indicating whether the post is published or not.
    views_count = models.PositiveIntegerField(default=0, verbose_name='View Count')  # A PositiveIntegerField to keep track of the number of post views.

    def __str__(self):
        # String representation of the object
        return f'Post number {self.pk}. {self.title}'

    class Meta:
        verbose_name = 'Post'  # Custom display name for a single object
        verbose_name_plural = 'Posts'  # Custom display name for a collection of objects
