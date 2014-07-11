
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.views import generic
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext

from lms_app.forms import CategoryForm, BookForm, StudentForm, IssueForm
from lms_app.models import Book, Student, Category

from models import Issue


class Login(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated():
            return redirect('lms_home')
        return render(request,'lms_app/login.html',{})

    def post(self,request,*args,**kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user and user.is_active:
            login(request, user)
        else:
            context = {
                'message' : 'Username or password is incorrect'
            }
            return render(request, 'lms_app/login.html',context)
        # context =  request.POST['username']
        data = {}
        return render(request, 'lms_app/lms_home.html', {}) 
        # return render(request, 'lms_app/lms_home.html', { "username": context })


class Logout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('lms_login')


class HomeView(View):
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')
        return render(request, 'lms_app/lms_home.html',     
        )

class ListBook(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')
        object_list = Book.objects.all()
        return render(request, 'lms_app/book_manage.html', {
            'object_list': object_list
        })


class ListStudent(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')
        object_list = Student.objects.all()
        return render(request, 'lms_app/student_manage.html', {
            'object_list': object_list
        })


class ListCategory(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')
        object_list = Category.objects.all()
        return render(request, 'lms_app/category_manage.html', {
            'object_list': object_list
        })


class CreateBook(View):
        
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')
        form = BookForm(None)
        context = { "form": form }  
        return render(request, 'lms_app/book_add.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')
        form = BookForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully.')
            return redirect('book_add')
        context = { "form": form }  
        return render(request, 'lms_app/book_add.html', context)
  

class CreateStudent(View):
       
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')
        form = StudentForm(None)
        context = { "form": form }  
        return render(request, 'lms_app/student_add.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')
        form = StudentForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('student_add')
        context = { "form": form }
        return render(request, 'lms_app/student_add.html', context)


class CreateCategory(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
           return redirect('lms_login')
        form = CategoryForm(None)
        context = { "form": form }  
        return render(request, 'lms_app/category_add.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        form = CategoryForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect('category_add')
        context = { "form": form }
        return render(request, 'lms_app/category_add.html', context)


class CreateIssue(View):
        
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        students = Student.objects.filter(block=False)
        books = Book.objects.filter(is_available=True)
        context = { "books": books, "students": students}
        return render(request, 'lms_app/book_issue.html', context)

    def post(self,request,*args,**kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        student_id  =  request.POST['student_id']
        student = Student.objects.get(id=student_id)
        if student.book_number <3:
            book_id = request.POST['book_id']
            book = Book.objects.get(id=book_id)
            if book.is_available == True:
                issue_date = datetime.now()
                return_date = datetime.now()+timedelta(days=7)
                return_status = False
                book.is_available = False
                issue = Issue.objects.create(student=student, book=book, issue_date=issue_date, return_date=return_date, return_status=return_status)
                student.book_number = student.book_number + 1
                if student.book_number==3:
                    student.block = True
                student.save()
                book.save()
        return redirect('book_issue')
        # return redirect('error_page')


class CreateReturn(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        issue = Issue.objects.get(id=kwargs['issue_id'])
        book =  issue.book
        student = issue.student
        issue.return_status = True
        book.is_available = True
        student.book_number = student.book_number-1
        if student.block == True:
            student.block = False
        issue.save()
        book.save()
        student.save()
        return redirect('book_manage')


class DeleteBook(View):

     def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        book = Book.objects.get(id=kwargs['book_id'])
        issues = Issue.objects.filter(book__id=kwargs['book_id'], return_status=False)
        for issue in issues:
            student = issue.student
            student.book_number = student.book_number-1
            if student.block == True:
                student.block = False
            student.save()
            issue.delete()
        book.delete()

        return redirect('book_manage')


class DeleteStudent(View):

     def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        student = Student.objects.get(id=kwargs['student_id'])
        issues = Issue.objects.filter(student__id=kwargs['student_id'], return_status=False)
        for issue in issues:
            book = issue.book
            book.is_available = True
            book.save()
            issue.delete()
        student.delete()

        return redirect('student_manage')


class DeleteCategory(View):

     def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        category = Category.objects.get(id=kwargs['category_id'])
        category.delete()

        return redirect('category_manage')

class EditBook(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        book = Book.objects.get(id=kwargs['book_id'])
        form = BookForm(instance=book)
        context = { "form": form }  
        return render(request, 'lms_app/book_add.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        book = Book.objects.get(id=kwargs['book_id'])
        form = BookForm(request.POST, instance=book) 
        if form.is_valid():
            form.save()
        return redirect('book_manage')


class EditStudent(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        student = Student.objects.get(id=kwargs['student_id'])
        form = StudentForm(instance=student)
        context = { "form": form }  
        return render(request, 'lms_app/student_add.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        student = Student.objects.get(id=kwargs['student_id'])
        form = StudentForm(request.POST, instance=student) 
        if form.is_valid():
            form.save()
        return redirect('student_manage')


class EditCategory(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        category = Category.objects.get(id=kwargs['category_id'])
        form = CategoryForm(instance=category)
        context = { "form": form }  
        return render(request, 'lms_app/category_add.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        category = Category.objects.get(id=kwargs['category_id'])
        form = CategoryForm(request.POST, instance=category) 
        if form.is_valid():
            form.save()
        return redirect('category_manage')


class ListBookinHand(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        issues = Issue.objects.filter(student__id=kwargs['student_id'], return_status=False)
        for issue in issues:
            if issue.return_date < timezone.now() :
                end_date = datetime.now()
                start_date = issue.return_date
                difference_in_days = abs((end_date.date() - start_date.date()).days)
                issue.fine_amount = difference_in_days*5
        context = { "form": issues }
        return render(request, 'lms_app/book_view.html', context)


class ListBookinCategory(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        books = Book.objects.filter(category__id=kwargs['category_id'])
        context = { "form": books }
        return render(request, 'lms_app/book_view_category.html', context)


class SearchBook(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        object_list = Book.objects.filter(name=request.GET['search_text'])
        return render(request, 'lms_app/book_manage.html', {'object_list': object_list})


class SearchStudent(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('lms_login')        
        object_list = Student.objects.filter(name=request.GET['search_text'])
        return render(request, 'lms_app/student_manage.html', {'object_list': object_list})
