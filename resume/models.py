from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


"""PROFILE MODEL"""
class Profile(models.Model):
    overview = models.CharField(max_length=600)

    def __str__(self):
        return self.overview


"""WORK EXPERIENCE MODEL"""
class Work_Experience(models.Model):
   
    job_title = models.CharField(max_length=150, blank=False, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    date = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.job_title


"""EDUCATION MODEL"""
class Education(models.Model):
   
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    degree_name = models.CharField(max_length=250, blank=False, unique=True)
    univeristy = models.CharField(max_length=200, blank=False)
    date = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.degree_name


"""TRAINING MODEL"""
class Internships(models.Model):
   
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    name = models.CharField(max_length=250, blank=False, unique=True)
    institute = models.CharField(max_length=200, blank=False)
    date = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


"""PORTFOLIO MODEL"""
class Portfolio(models.Model):
   
    name = models.CharField(max_length=250, blank=False, unique=True)
    description = models.CharField(max_length=500, blank=False, unique=True)
    link = models.URLField(max_length=234, null=True, blank=True)
    
    def __str__(self):
        return self.name


"""TECHNICAL SKILLS MODEL"""
class Technical_skills(models.Model):
   
    name = models.CharField(max_length=250, blank=False, unique=True)
    proficiency = models.IntegerField(default=0, 
        validators=[
            MaxValueValidator(100), 
            MinValueValidator(1)
            ]
        )
    
    def __str__(self):
        return self.name


"""SOFT SKILLS MODEL"""
class Soft_skills(models.Model):
   
    name = models.CharField(max_length=250, blank=False, unique=True)
    
    def __str__(self):
        return self.name


# """VOLUNTEER MODEL"""
# class Volunteer(models.Model):
   
#     name = models.CharField(max_length=250, blank=False, unique=True)
#     description = models.TextField()
#     date = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.name


# """INTERESTS MODEL"""
# class Interest(models.Model):
   
#     name = models.CharField(max_length=250, blank=False, unique=True)
    
#     def __str__(self):
#         return self.name

