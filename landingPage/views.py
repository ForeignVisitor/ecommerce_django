from django.shortcuts import render

def landingPage(request):
    return render(request, 'landingPage/landingPage.html')
