from django.db import models

# Create your Web Dev models here.
# STILL NEED TO MIGRATE!

class Skills(models.Model):
    name = models.CharField(max_length=100, default='skills')
    skill_icon = models.FileField()
    
    def __str__(self):
        return self.name

class AboutMe(models.Model):
    name = models.CharField(max_length=100, default='About Me')
    location = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=200)
    bio = models.TextField()
    selfie = models.FileField()

    def __str__ (self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50, default='contact')
    email = models.CharField(max_length=50, default='clrnfllr(at)gmail.com')
    github = models.URLField(default='https://github.com/brittgalloway/')
    linkedIn = models.URLField(default='https://www.linkedin.com/brittneygalloway/')
    resume = models.FileField()

    def __str__ (self):
        return self.name

class ProjectPage(models.Model):
    title = models.CharField(max_length=50)
    github = models.URLField() 
    liveApp = models.URLField() 
    description = models.TextField()
    image = models.FileField()
    alt_text = models.CharField(max_length=50)
    tools = models.TextField()
    improvements = models.TextField()
    year = models.IntegerField(max_digits=4, default=2020)
    extra_title = models.CharField(max_length=50)
    extra_link = models.URLField() 
    extra_note = models.TextField()

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title