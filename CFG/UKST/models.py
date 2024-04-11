from django.db import models

class SurveyResponse(models.Model):
    AGE_CHOICES = (
        ('0', '0-18'),
        ('1', '18-24'),
        ('2', '24-65'),
        ('3', '65+'),  
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    QUESTION_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    age = models.CharField(max_length=1, choices=AGE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Q1 = models.CharField(max_length=1, choices=QUESTION_CHOICES)
    Q2 = models.CharField(max_length=1, choices=QUESTION_CHOICES)
    Q3 = models.CharField(max_length=1, choices=QUESTION_CHOICES)
    Q4 = models.CharField(max_length=1, choices=QUESTION_CHOICES)
    Q5 = models.CharField(max_length=1, choices=QUESTION_CHOICES)
    Q6 = models.CharField(max_length=1, choices=QUESTION_CHOICES)

    def __str__(self):
        return f"Age: {self.get_age_display()}, Gender: {self.get_gender_display()}"
