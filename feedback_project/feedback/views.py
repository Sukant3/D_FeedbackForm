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

        #  page does NOT re-submit form
        return redirect('/feedback/?success=true')

    
    success = request.GET.get("success") == "true"

    return render(request, 'feedback/feedback_form.html', {"success": success})

def feedback_list(request):
    data=Feedback.objects.all().order_by('id')
    return render(request,'feedback/list.html',{"data":data})


def feedback_edit(request,id):
    fb=Feedback.objects.get(id=id)

    if request.method=="POST":
        fb.name=request.POST.get('name')
        fb.email=request.POST.get('email')
        fb.message=request.POST.get('message')
        fb.save()

        return redirect('/list/')
    return render(request,'feedback/edit.html',{"fb":fb})

def feedback_delete(request,id):
    fb=Feedback.objects.get(id=id)

    if request.method=="POST":
        fb.delete()
        return redirect('/list/')

    # return render(request,'feedback/delete_confirm.html',{'fb':fb})

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
