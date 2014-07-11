from django.conf.urls import patterns, url

from lms_app import views

urlpatterns = patterns('',
  url(r'^$', views.Login.as_view(), name='lms_login'),
  url(r'^logout/$', views.Logout.as_view(), name='lms_logout'),
  url(r'^home/$', views.HomeView.as_view(), name='lms_home'),
  url(r'^add_books/$',  views.CreateBook.as_view(), name='book_add'),
  url(r'^manage_books/$', views.ListBook.as_view(), name='book_manage'),
  url(r'^add_category/$', views.CreateCategory.as_view(), name='category_add'),
  url(r'^manage_category/$', views.ListCategory.as_view(), name='category_manage'),
  url(r'^add_student/$', views.CreateStudent.as_view(), name='student_add'),
  url(r'^manage_student/$',views.ListStudent.as_view(), name='student_manage'),
  url(r'^edit_book/(?P<book_id>\d+)/$', views.EditBook.as_view(), name='book_edit'),
  url(r'^edit_student/(?P<student_id>\d+)/$', views.EditStudent.as_view(), name='student_edit'),
  url(r'^edit_category/(?P<category_id>\d+)/$', views.EditCategory.as_view(), name='category_edit'),
  url(r'^delete_book/(?P<book_id>\d+)/$', views.DeleteBook.as_view(), name='book_delete'),
  url(r'^delete_student/(?P<student_id>\d+)/$', views.DeleteStudent.as_view(), name='student_delete'),
  url(r'^delete_category/(?P<category_id>\d+)/$', views.DeleteCategory.as_view(), name='category_delete'),
  url(r'^issue_book/$', views.CreateIssue.as_view(), name='book_issue'),
  url(r'^return_book/(?P<issue_id>\d+)/$', views.CreateReturn.as_view(), name='book_return'),
  url(r'^view_book/(?P<student_id>\d+)/$', views.ListBookinHand.as_view(), name='book_view'),
  url(r'^view_booklist/(?P<category_id>\d+)/$', views.ListBookinCategory.as_view(), name='book_view_category'),
  url(r'^search_book/$', views.SearchBook.as_view(), name='book_search'),
  url(r'^search_student/$', views.SearchStudent.as_view(), name='student_search'),
)