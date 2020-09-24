from django.db import models

# Create your art models here.
# STILL NEED TO MIGRATE!

ARTIST = (
    ('Brittney'),
    ('Crstal'),
)
PAGE = (
    ('Sketchbook'),
    ('PaperCut'),
    ('Illustration'),
    ('Visual Development'),
)
class Art(models.Model):
    name = models.CharField(max_length=50,default="Art")
    image = models.FileField() 
    alt_text = models.CharField(max_length=200)
    creator = models.CharField(choices=ARTIST,max_length=1)
    page = models.CharField(choices=PAGE,max_length=1)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.image

