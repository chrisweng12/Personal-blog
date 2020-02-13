from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default='default.png',blank=True)
    # add in author later
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        if len(self.body) < 51:
            return self.body[:50] 
        elif len(self.body) > 50:
            return self.body[:50] + ' ...'