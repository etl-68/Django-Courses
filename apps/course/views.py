from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def start(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'course/index.html', context)

def add(request):
    if request.method == 'POST':
        course = Course.objects.create(course_name=request.POST['name'], description=request.POST['description'])
        course_id = course.id
        return redirect('/')

def delete(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    request.session['course_id']=course_id
    print request.POST
    return render(request, 'course/delete.html', context)

def actions(request):
    if request.method == 'POST':
        if 'confirm' in request.POST:
            Course.objects.get(id=request.session['course_id']).delete()
            return redirect('/')
        else:
            print 'cool beans'
            return redirect('/')
