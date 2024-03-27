from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })


def view_student(request, id):
    student = student.object.get(pk=id)
    return HttpResponseRedirect(reverse('index'))



def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            new_student_number =  form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study =form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa'] 

            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa
            )
            new_student.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else: 
        form = Student()
    return render(request, 'students/add.html', {
        'form': StudentForm()
    })


def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id) # gets the student whose primary key is equal to the id and stores inside the student vtiable
        form = StudentForm(request.POST,  instance=student) #instantiates the from the instance argument ensures we are editing information from the right student

        if form.is_valid(): #save form
            form.save()
            return render(request, 'students/edit.html',{
                'form': form,
                'student': student,
                'success': True
            })
    else: #none post instance
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html',{
            'form': form ,
        })

def delete(request, id):
    if request.method =='POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))