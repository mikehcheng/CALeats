from django.db import models

class Entree(models.Model):
	name = models.CharField(max_length=100)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return "{0}; Votes: {1}".format(self.name, self.votes)

class MealOption(models.Model):
	entree = models.ForeignKey(Entree)
	meal = models.CharField(max_length=20)
	day = models.DateTimeField()