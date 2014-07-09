from lms_app.models import Category, Book, Student, Issue

from django.forms import ModelForm

class CategoryForm(ModelForm):
    class Meta:
        model = Category


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ('is_available', )


class StudentForm(ModelForm):
    class Meta:
        model = Student


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        exclude = ('return_status', )