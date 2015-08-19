from django.db import models

# Create your models here.
class Unit(models.Model) :
	FACTORY = "FA"
	COMMAND_CENTRE = "CC"
	BARRACKS = "BA"
	STARPORT = "SA"
	BUILT_FROM_CHOICES = (
		(FACTORY, "Factory"),
		(COMMAND_CENTRE, "Command Centre"),
		(BARRACKS, "Barracks"),
		(STARPORT, "Starport"),
	)
	
	name = models.TextField()
	built_from = models.CharField(max_length=2,
									choices=BUILT_FROM_CHOICES,
									default=COMMAND_CENTRE)
	supply_cost = models.IntegerField(default=1)
	mineral_cost = models.IntegerField(default=0)
	vespene_cost = models.IntegerField(default=0)
	build_time = models.IntegerField()
	life = models.IntegerField()
	armor = models.IntegerField(default=0)
	
	def __str__(self) :
		return self.name