# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.is_available'
        db.add_column(u'lms_app_book', 'is_available',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.is_available'
        db.delete_column(u'lms_app_book', 'is_available')


    models = {
        u'lms_app.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lms_app.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'lms_app.category': {
            'Meta': {'object_name': 'Category'},
            'cat_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lms_app.issue': {
            'Meta': {'object_name': 'Issue'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lms_app.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 8, 0, 0)'}),
            'return_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 15, 0, 0)'}),
            'return_status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lms_app.Student']"})
        },
        u'lms_app.student': {
            'Meta': {'object_name': 'Student'},
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'division': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rollno': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'lms_app.student_issue_detail': {
            'Meta': {'object_name': 'Student_Issue_Detail'},
            'block': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'book_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fine_amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lms_app.Student']"})
        }
    }

    complete_apps = ['lms_app']