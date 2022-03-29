from django.db import models

class Donut(models.Model):
  name = models.CharField(max_length=255, default=None)
  info = models.TextField()
  cost = models.IntegerField(default=0)
  picture = models.ImageField(upload_to='donuts/', default="donut-default.jpg")

  def __str__(self):
      return self.name

  class Meta:
    db_table = 'Donuts'
    managed = True
    verbose_name = 'Car'
    verbose_name_plural = 'Cars'

class DonutsSet(models.Model):
  class Meta:
    db_table = 'DonutsSets'
    managed = True
    verbose_name = 'Car Set'
    verbose_name_plural = 'Car Sets'

  name = models.CharField(max_length=255, default=None)
  info = models.TextField()
  picture = models.ImageField(upload_to='donuts/', default="donut-default.jpg")
  fk_donuts = models.ManyToManyField(Donut)

  @property
  def donuts_count(self):
    d_count = self.fk_donuts.all().count()
    return d_count

  @property
  def cost(self):
    donuts = self.fk_donuts.all()

    cost = 0
    for donut in donuts:
      cost += donut.cost

    return cost


  def __str__(self):
    return self.name