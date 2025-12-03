from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def feedback_view(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Feedback.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Redirect so refreshing page does NOT re-submit form
        return redirect('/feedback/?success=true')

    
    success = request.GET.get("success") == "true"

    return render(request, 'feedback/feedback_form.html', {"success": success})



# if we use form directly. create form.py then create view 


# def feedback_view(request):
#     if request.method == 'POST':
#         form = Feedback(request.POST)
#         if form.is_valid():
#             form.save()
#             message.success(request, "Form submitted successfully!")
#             return redirect('feedback')  # important: NO query params
#     else:
#         form = Feedback()

#     return render(request, 'feedback/feedback_form.html', {'form': form})
