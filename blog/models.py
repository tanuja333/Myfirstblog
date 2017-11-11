from django.db import models
from django.utils import timezone
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
#self is like this pointer
    def publish(self):
        self.published_date = timezone.now()
        self.save()  #called for updation
#__str__ its a magical method called prior to all just look for
    def __str__(self):
        return self.title
