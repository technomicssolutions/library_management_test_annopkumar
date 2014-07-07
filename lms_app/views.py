# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from lms_app.models import Category, Book, Student


from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

class CategoryForm(ModelForm):
    class Meta:
        model = Category


class BookForm(ModelForm):
    class Meta:
        model = Book


class StudentForm(ModelForm):
    class Meta:
        model = Student


def lms_home(request, template_name='lms_app/lms_home.html'):
    return render(request, template_name)        

def book_create(request, template_name='lms_app/book_add.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_add')
    return render(request, template_name, {'form':form})

def book_manage(request, template_name='lms_app/book_manage.html'):
    books = Book.objects.all()
    data = {}
    data['object_list'] = books
    return render(request, template_name, data)

def category_create(request, template_name='lms_app/category_add.html'):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_add')
    return render(request, template_name, {'form':form})

def category_manage(request, template_name='lms_app/category_manage.html'):
    categories = Category.objects.all()
    data = {}
    data['object_list'] = categories
    return render(request, template_name, data)

def student_create(request, template_name='lms_app/student_add.html'):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_add')
    return render(request, template_name, {'form':form})

def student_manage(request, template_name='lms_app/student_manage.html'):
    students = Student.objects.all()
    data = {}
    data['object_list'] = students
    return render(request, template_name, data)

def book_edit(request, pk, template_name='lms_app/book_add.html'):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_manage')
    return render(request, template_name, {'form':form})

def student_edit(request, pk, template_name='lms_app/student_add.html'):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_manage')
    return render(request, template_name, {'form':form})

def category_edit(request, pk, template_name='lms_app/category_add.html'):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_manage')
    return render(request, template_name, {'form':form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk).delete()    
    return HttpResponseRedirect(reverse('book_manage'))

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk).delete()    
    return HttpResponseRedirect(reverse('student_manage'))

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk).delete()    
    return HttpResponseRedirect(reverse('category_manage'))