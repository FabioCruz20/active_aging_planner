from django.db import models

# Create your models here.

class Action(models.Model):
    """
    
    """
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name


class Level(models.Model):
    """
    
    """
    level_number = models.IntegerField()
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return f'Nível {self.level_number}: {self.name}'


class Project(models.Model):
    """
    
    """
    name = models.CharField(max_length=500)
    description = models.TextField()


class ProjectLevel(models.Model):
    """
    
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    progress_percentage = models.FloatField()


class ProjectLevelAction(models.Model):
    """
    
    """
    project_level = models.ForeignKey(ProjectLevel, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)

