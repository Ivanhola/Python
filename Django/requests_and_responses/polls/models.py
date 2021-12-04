from django.db import models
from django.utils import timezone
import datetime
#Each variable represents a database field in the model
#THe field class tells Django what kind of data is submitted to the database field
#The database will use the variable names as the column names in the database
class Question(models.Model):

    
    
    question_text = models.CharField(max_length=200)
    #We defined a human readable name by using "Date published"
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    #Each choice is associated with the Question class hence Question below
    #Foreign key database term, meaning each choice is related to a single question
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



    def __str__(self):
        return self.choice_text
