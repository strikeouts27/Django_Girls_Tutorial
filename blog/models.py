from django.conf import settings
from django.db import models 
from django.utils import timezone 

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title 

# explain what is going on line by line
"""
So it looks like the django girls want to create a blogpost. So they created a python class and than inside that python class they activate django models functionality
by passing in models.Model. Once they do that, they asked themselves what does our blog need? And they had an author, title, text, created_date, and published_date fields.

They also created a published function and said had this publish method save the published date and used the save() function on it.  
"""
