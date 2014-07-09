# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Student.fine_amount'
        db.delete_column(u'lms_app_student', 'fine_amount')


    def backwards(self, orm):
        # Adding field 'Student.fine_amount'
        db.add_column(u'lms_app_student', 'fine_amount',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


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
            'issue_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 9, 0, 0)'}),
            'return_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 16, 0, 0)'}),
            'return_status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lms_app.Student']"})
        },
        u'lms_app.student': {
            'Meta': {'object_name': 'Student'},
            'block': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'book_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'division': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rollno': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['lms_app']