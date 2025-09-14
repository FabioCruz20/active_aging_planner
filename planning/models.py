from django.db import models


class Level(models.Model):
    """Modelo para representar níveis do projeto"""
    level_number = models.IntegerField()
    name = models.CharField(max_length=500)

    def __str__(self):
        return f'Nível {self.level_number}: {self.name}'


class Axis(models.Model):
    """Modelo para representar eixos do projeto"""
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class ProjectLevelAxis(models.Model):
    """Modelo para representar a relação entre nível e eixo"""
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    axis = models.ForeignKey(Axis, on_delete=models.CASCADE)
    progress_percentage = models.FloatField(default=0)

    class Meta:
        db_table = 'planning_project_level_axis'

    def __str__(self):
        return f'{self.level.name} - {self.axis.name}'


class Action(models.Model):
    """Modelo para representar ações do projeto"""
    name = models.CharField(max_length=500)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    axis = models.ForeignKey(Axis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ProjectAction(models.Model):
    """Modelo para representar uma ação"""
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    axis = models.ForeignKey(Axis, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('action', 'axis', 'level')
        db_table = 'planning_project_action'

    def __str__(self):
        return f'{self.action.name} ({self.axis.name}, {self.level.name})'

    def count_finished_tasks(self):
        return self.tasks.filter(status='DONE').count()

class Task(models.Model):
    """Modelo para representar tarefas específicas de uma ação do projeto"""
    STATUS_CHOICES = [
        ('TODO', 'A fazer'),
        ('DOING', 'Fazendo'),
        ('PENDING', 'Pendente'),
        ('DONE', 'Concluída')
    ]

    title = models.CharField('Título', max_length=500)
    description = models.TextField('Descrição', blank=True, null=True)
    status = models.CharField('Status', max_length=10, choices=STATUS_CHOICES, default='TODO')
    project_action = models.ForeignKey('ProjectAction', on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)
    completed_at = models.DateTimeField('Data de conclusão', null=True, blank=True)

    class Meta:
        db_table = 'planning_task'

    def save(self, *args, **kwargs):
        if self.status == 'DONE' and not self.completed_at:
            from django.utils import timezone
            self.completed_at = timezone.now()
        elif self.status != 'DONE':
            self.completed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Paper(models.Model):
    """Modelo para representar artigos científicos"""
    title = models.CharField('Título', max_length=500)
    url = models.URLField('URL')
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    class Meta:
        db_table = 'planning_paper'

    def __str__(self):
        return self.title
