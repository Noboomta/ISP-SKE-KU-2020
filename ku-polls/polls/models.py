"""import."""
from django.db import models
import datetime
import django.contrib.auth.models
from django.utils import timezone

class Question(models.Model):
    """Question class for model."""

    search_fields = ['question_text']
    list_filter = ['pub_date', 'end_date']
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('data vote ended')

    def __str__(self):
        """Str method."""
        return self.question_text

    def was_published_recently(self):
        """Check if the Question is published recently."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """Check if the Question is published."""
        now = timezone.now()
        return self.pub_date <= now

    def can_vote(self):
        """Check if the Question can vote."""
        now = timezone.now()
        return self.pub_date <= now <= self.end_date

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    """Choice class for model."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return the choice text."""
        return self.choice_text

class Vote(models.Model):
    """Class Vote for store the choice selected, user, and question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(django.contrib.auth.models.User,null=True,blank=True,on_delete=models.CASCADE)