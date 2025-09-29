from django.shortcuts import render, redirect
from django.db.models import Count
from planning.models import ProjectLevelAxis, ProjectAction, Axis, Level

def index_view(request):
    """View para o dashboard principal que mostra a contagem de ações por par eixo-nível"""
    # Obter todos os níveis
    levels = Level.objects.all().order_by('level_number')

    level_axis_actions = {}
    for level in levels:
        level_axis_actions[level.name] = {
            'axes': [],
            'actions': []
        }

        for axis in Axis.objects.all():
            level_axis_actions[level.name]['axes'].append(
                axis.name
            )
            level_axis_actions[level.name]['actions'].append(
                ProjectAction.objects.filter(
                    axis=axis,
                    level=level
                ).count()
            )

    print(level_axis_actions)

    # Obter todos os pares eixo-nível
    project_level_axes = ProjectLevelAxis.objects.all()
    
    # Contar ações adicionadas por par eixo-nível
    action_counts = ProjectAction.objects.values('axis', 'level').annotate(
        count=Count('id')
    )
    
    # Criar um dicionário para facilitar o acesso às contagens
    action_count_dict = {}
    for item in action_counts:
        key = (item['axis'], item['level'])
        action_count_dict[key] = item['count']
    
    # Adicionar contagem a cada par eixo-nível
    for pla in project_level_axes:
        key = (pla.axis.id, pla.level.id)
        pla.action_count = action_count_dict.get(key, 0)
    
    # Obter todos os eixos e níveis para construir a matriz
    axes = Axis.objects.all().order_by('id')
    levels = Level.objects.all().order_by('level_number')
    
    # Construir matriz de contagens
    matrix = []
    for level in levels:
        row = []
        for axis in axes:
            key = (axis.id, level.id)
            count = action_count_dict.get(key, 0)
            row.append({
                'axis': axis,
                'level': level,
                'count': count
            })
        matrix.append({
            'level': level,
            'cells': row
        })
    
    context = {
        'project_level_axes': project_level_axes,
        'axes': axes,
        'levels': levels,
        'matrix': matrix,
        'level_axis_actions': level_axis_actions
    }
    
    return render(request, 'dashboard/index.html', context)
