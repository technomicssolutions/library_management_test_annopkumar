# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student_Issue_Detail'
        db.create_table(u'lms_app_student_issue_detail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lms_app.Student'])),
            ('book_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fine_amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('block', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'lms_app', ['Student_Issue_Detail'])

        # Adding model 'Issue'
        db.create_table(u'lms_app_issue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lms_app.Student'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lms_app.Book'])),
            ('issue_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 8, 0, 0))),
            ('return_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 15, 0, 0))),
            ('return_status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'lms_app', ['Issue'])


    def backwards(self, orm):
        # Deleting model 'Student_Issue_Detail'
        db.delete_table(u'lms_app_student_issue_detail')

        # Deleting model 'Issue'
        db.delete_table(u'lms_app_issue')


    models = {
        u'lms_app.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lms_app.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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