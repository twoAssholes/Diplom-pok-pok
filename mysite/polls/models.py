from django.db import models

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    question_type = models.IntegerField()
    # question_file = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    pub_author = models.CharField(max_length=200)
    question_cost_positive = models.IntegerField()
    question_cost_negative = models.IntegerField()


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Question, self).save()


    def __str__(self):
       return self.question_text


class Choice(models.Model):

    choice_text = models.CharField(max_length=200, verbose_name='текст вопроса')
    # your_choice_id = models.IntegerField()
    question = models.ForeignKey(Question)
    choice_cost_positive = models.IntegerField()
    choice_cost_negative = models.IntegerField()
    choice_is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class User(models.Model):

    name = models.CharField(max_length=200, verbose_name='Имя')
    login = models.CharField(max_length=200, blank=True, verbose_name='логин')
    pswd = models.CharField(max_length=200, blank=True, verbose_name='пароль')
    rating = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Vote(models.Model):

    test_date = models.DateTimeField('date published')
    student = models.ForeignKey(User)
    selected_quest = models.CharField(max_length=200)
    selected_choice = models.CharField(max_length=200)
    selected_student = models.CharField(max_length=200)
    balls = models.IntegerField()

    def __str__(self):
        return self.balls

