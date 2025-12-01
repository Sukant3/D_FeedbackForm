from django.shortcuts import render
from .models import *

# Create your views here.

def feedback_view(request):
    success=False

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        Feedback.objects.create(
            name=name,
            email=email,
            message=message
        )

        success=True
    return render(request,'feedback/feedback_form.html',{"success":success})

    
