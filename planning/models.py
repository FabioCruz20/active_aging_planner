from django.db import models

# Create your models here.
class Level(models.Model):
    """
    
    """
    level_number = models.IntegerField()
    name = models.CharField(max_length=500)

    def __str__(self):
        return f'Nível {self.level_number}: {self.name}'


class Axis(models.Model):
    """"""
    name = models.CharField(max_length=500)
    

class Action(models.Model):
    """
    
    """
    name = models.CharField(max_length=500)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    axis = models.ForeignKey(Axis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    """"""
    title = models.CharField(max_length=500)
    done = models.BooleanField()
    action = models.ForeignKey(Action, on_delete=models.CASCADE, null=True)


class Project(models.Model):
    """
    
    """
    name = models.CharField(max_length=500)
    description = models.TextField()
    levels = models.ManyToManyField(Level, through='ProjectLevelAxis')
    axes = models.ManyToManyField(Axis, through='ProjectLevelAxis')

    def __str__(self):
        return self.name


class ProjectLevelAxis(models.Model):
    """
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    axis = models.ForeignKey(Axis, on_delete=models.CASCADE)    
    progress_percentage = models.FloatField()
