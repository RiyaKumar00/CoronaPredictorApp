from django.shortcuts import render
from django.http import HttpResponse
from Predictor.StateToCode import *
from Predictor.PredictCases import *
# Create your views here.

def index(request):
    return render(request,'HomePage.html')

def GoToForm(request):
    return render(request,'CPForm.html')

def GoToSymptoms(request):
    return render(request, 'CheckSymptoms.html')

def GoToPrevention(request):
    return render(request, 'Preventions.html')

def GoToTest(request):
    return render(request, 'TestForm.html')

def GoToHome(request):
    return render(request, 'HomePage.html')

def GoToTech(request):
    return render(request, 'Technology.html')

def GoToAbout(request):
    return render(request, 'AboutUs.html')

def predictCovid(request):
    if request.method=='POST':
        data={}
        data['first_name']=request.POST.get('fNameVal')
        data['last_name']=request.POST.get('lNameVal')
        data['MailID']=request.POST.get('EmailVal')
        data['age']=request.POST.get('AgeVal')
        data['stateName']=request.POST.get('StateVal')
        data['NumbDays']=request.POST.get('DaysVal')
    code = changeToCode(data['stateName'])
    Total_Cases = Cases(code, int(data['NumbDays']))
    Total_Cases[0] = data['stateName']
    context={'PredictedCases':Total_Cases,
             'day': data['NumbDays']
            }
    return render(request,'CPResult.html',context)

def ShowResults(request):
    if(request.method=='POST'):
        data={}
        data['A']=request.POST.get('Option1')
        data['B']=request.POST.get('Option2')
        data['C']=request.POST.get('Option3')
        data['D']=request.POST.get('Option4')
        data['E']=request.POST.get('Option5')
        data['F']=request.POST.get('Option6')
        data['G']=request.POST.get('Option7')
        data['H']=request.POST.get('Option8')
        #if else input lene ke baad
        danger=0
        if(data['A']=='Yes'):
            danger += 9;
        if(data['A']=='Sometimes'):
            danger += 6;
        if(data['B']=='Yes'):
            danger += 7;
        if(data['B']=='Sometimes'):
            danger += 4;
        if(data['C']=='Yes'):
            danger += 5;
        if(data['C']=='Sometimes'):
            danger += 3;
        if(data['D']=='Yes'):
            danger += 3;
        if(data['D']=='Sometimes'):
            danger += 2;
        if(data['E']=='Yes'):
            danger += 2;
        if(data['E']=='Sometimes'):
            danger += 1;
        if(data['F']=='Yes'):
            danger += 10;
        if(data['F']=='Sometimes'):
            danger += 7;
        if(data['G']=='Yes'):
            danger += 4;
        if(data['G']=='Sometimes'):
            danger += 3;
        if(data['H']=='Yes'):
            danger += 4;
        if(data['H']=='Sometimes'):
            danger += 3;
        if(danger>=10):
            context={'answer':"Do not panic! Reach any Covid hospital and have a check for Covid-19!"}
        elif(danger>=6):
            context={'answer':"Seems ok! Contact a doctor if it has been a while."}
        else:
            context={'answer':"You are safe! Take precautions and live a healty life. :)"}
    return render(request,'TestForm.html',context)
