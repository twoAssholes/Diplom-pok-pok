# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('choice_text', models.CharField(max_length=200)),
                ('choice_cost_positive', models.IntegerField()),
                ('choice_cost_negative', models.IntegerField()),
                ('other_choice_data', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('question_text', models.CharField(max_length=200)),
                ('question_type', models.IntegerField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('pub_author', models.CharField(max_length=200)),
                ('question_cost', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.IntegerField(primary_key=1, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('test_date', models.DateTimeField(verbose_name='date published')),
                ('selected_quest', models.CharField(max_length=200)),
                ('selected_choice', models.CharField(max_length=200)),
                ('selected_student', models.CharField(max_length=200)),
                ('balls', models.IntegerField()),
                ('student', models.ForeignKey(to='polls.Students')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='polls.Question'),
            preserve_default=True,
        ),
    ]
