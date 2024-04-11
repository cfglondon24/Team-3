from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SurveyForm
from .models import SurveyResponse

def home(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            # Create a SurveyResponse object with cleaned data
            survey_response = SurveyResponse(
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                q1=form.cleaned_data['q1'],
                q2=form.cleaned_data['q2'],
                q3=form.cleaned_data['q3'],
                q4=form.cleaned_data['q4'],
                q5=form.cleaned_data['q5'],
                q6=form.cleaned_data['q6'],
            )
            # Save the object to the database
            survey_response.save()
            # Redirect to a success page or any other desired action
            return redirect('UKST-home')
    else:
        form = SurveyForm()
    return render(request, 'UKST/home.html', {'form': form})

def home(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            # Process the form data
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            # Do something with the selected choice
            # add choice to database
            return render(request, 'UKST/home.html')#,{'gender': gender, 'age': age, }) #send to next page
    else:
        form = SurveyForm()
    return render(request, 'UKST/home.html',{'form': form})

def about(request):
    return render(request, 'UKST/about.html')
