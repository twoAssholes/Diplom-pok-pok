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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('choice_text', models.CharField(verbose_name='текст вопроса', max_length=200)),
                ('choice_cost_positive', models.IntegerField()),
                ('choice_cost_negative', models.IntegerField()),
                ('choice_is_true', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('question_type', models.IntegerField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('pub_author', models.CharField(max_length=200)),
                ('question_cost_positive', models.IntegerField()),
                ('question_cost_negative', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=200)),
                ('login', models.CharField(blank=True, verbose_name='логин', max_length=200)),
                ('pswd', models.CharField(blank=True, verbose_name='пароль', max_length=200)),
                ('rating', models.IntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('test_date', models.DateTimeField(verbose_name='date published')),
                ('selected_quest', models.CharField(max_length=200)),
                ('selected_choice', models.CharField(max_length=200)),
                ('selected_student', models.CharField(max_length=200)),
                ('balls', models.IntegerField()),
                ('student', models.ForeignKey(to='polls.User')),
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
