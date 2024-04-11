from django import forms
from .models import SurveyResponse

class SurveyForm(forms.ModelForm):
    ageChoices =  (
        ('0', '0-18'),
        ('1', '18-24'),
        ('2', '24-65'),
        ('3', '65+'),  
    )
    age = forms.ChoiceField(choices=ageChoices)

    genderChoices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = forms.ChoiceField(choices=genderChoices)
    
    q1Choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    q1 = forms.ChoiceField(choices=q1Choices)
    
    q2Choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    q2 = forms.ChoiceField(choices=q2Choices)
    
    q3Choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    q3 = forms.ChoiceField(choices=q3Choices)
    
    q4Choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    q4 = forms.ChoiceField(choices=q4Choices)
    
    q5Choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    q5 = forms.ChoiceField(choices=q5Choices)
    
    q6Choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    q6 = forms.ChoiceField(choices=q6Choices)

    class Meta:
        model = SurveyResponse
        fields = ['age', 'gender', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']