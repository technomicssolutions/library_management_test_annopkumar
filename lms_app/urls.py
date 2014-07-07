from django.conf.urls import patterns, url

from lms_app import views


from django.conf.urls import patterns, url


urlpatterns = patterns('',
  url(r'^$', views.lms_home, name='lms_home'),
  url(r'^add_books$', views.book_create, name='book_add'),
  url(r'^manage_books$', views.book_manage, name='book_manage'),
  url(r'^add_category$', views.category_create, name='category_add'),
  url(r'^manage_category$', views.category_manage, name='category_manage'),
  url(r'^add_student$', views.student_create, name='student_add'),
  url(r'^manage_student$', views.student_manage, name='student_manage'),
  url(r'^edit_book/(?P<pk>\d+)$', views.book_edit, name='book_edit'),
  url(r'^edit_student/(?P<pk>\d+)$', views.student_edit, name='student_edit'),
  url(r'^edit_category/(?P<pk>\d+)$', views.category_edit, name='category_edit'),
  url(r'^delete_book/(?P<pk>\d+)$', views.book_delete, name='book_delete'),
  url(r'^delete_student/(?P<pk>\d+)$', views.student_delete, name='student_delete'),
  url(r'^delete_category/(?P<pk>\d+)$', views.category_delete, name='category_delete'),
)