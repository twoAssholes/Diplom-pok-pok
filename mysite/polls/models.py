from django.db import models

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    question_type = models.IntegerField()
    # question_file = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    pub_author = models.CharField(max_length=200)
    question_cost = models.IntegerField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Question, self).save()


    def __str__(self):
       return self.question_text


class Choice(models.Model):

    choice_text = models.CharField(max_length=200)
    # your_choice_id = models.IntegerField()
    question = models.ForeignKey(Question)
    choice_cost_positive = models.IntegerField()
    choice_cost_negative = models.IntegerField()
    other_choice_data = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.choice_text

class Students(models.Model):

    id = models.IntegerField(primary_key=1)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Vote(models.Model):

    test_date = models.DateTimeField('date published')
    student = models.ForeignKey(Students)
    selected_quest = models.CharField(max_length=200)
    selected_choice = models.CharField(max_length=200)
    selected_student = models.CharField(max_length=200)
    balls = models.IntegerField()

    def __str__(self):
        return self.balls

