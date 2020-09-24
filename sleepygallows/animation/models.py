from django.db import models

# Create your ANIMATION models here.
# STILL NEED TO MIGRATE!

class AnimatedVideo(models.Model):
    title = models.CharField(max_length=50)
    embed = models.URLField() 
    year = models.IntegerField(max_digits=4, default=2020)
    video_credits = models.TextField(default='Brittney Galloway')
    description = models.TextField()

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class AnimatedSection(models.Model):
    title = models.ForeignKey(AnimatedVideo, on_delete=models.CASCADE)
    animation_type = models.CharField(max_length=50)

    def __str__(self):
        return self.animation_type