from django.shortcuts import render


def help_topics(request):
    help_sections = {
        'Visão Geral do Sistema': {
            'O que é o Sistema?': {
                'icon': 'information-circle',
                'icon_variant': 'solid',
                'content': '''O Sistema de Planejamento de Envelhecimento Ativo é uma ferramenta projetada para auxiliar no desenvolvimento e acompanhamento de ações que promovem o envelhecimento ativo e saudável. Ele permite organizar e gerenciar ações em diferentes eixos temáticos e níveis de maturidade, facilitando o planejamento e a execução de iniciativas.
                '''
            },
            'O que o Sistema não é?': {
                'icon': 'x-circle',
                'icon_variant': 'solid',
                'content': '''O sistema não é uma solução completa de gestão de projetos, nem uma ferramenta de monitoramento em tempo real. Ele não substitui a necessidade de planejamento estratégico ou a expertise profissional na área de envelhecimento ativo.
                '''
            }
        },
        'Conceitos Fundamentais': {
            'O que é um Eixo Temático?': {
                'icon': 'cube',
                'icon_variant': 'solid',
                'content': '''Um Eixo Temático representa uma área específica de atuação no contexto do envelhecimento ativo, como saúde, participação social, segurança ou aprendizagem ao longo da vida. Os eixos ajudam a categorizar e organizar as ações de acordo com seus objetivos principais.
                '''
            },
        },
        'Guia Prático': {
            'Como gerenciar Ações?': {
                'icon': 'clipboard',
                'icon_variant': 'solid',
                'content': '''As Ações são iniciativas específicas que contribuem para o envelhecimento ativo. Para gerenciar ações, você pode:
                1. Entrar em um eixo temático
                2. Adicionar uma ação existente ou criar uma ação
                3. Adicionar tarefas específicas para implementação
                4. Acompanhar o progresso através da matriz de ações
                '''
            },
            'Como gerenciar Tarefas?': {
                'icon': 'check-circle',
                'icon_variant': 'solid',
                'content': '''As Tarefas são atividades específicas que compõem uma ação. Para gerenciar tarefas:
                1. Selecione a ação desejada
                2. Adicione novas tarefas com descrições claras
                3. Marque as tarefas como concluídas quando finalizadas
                4. Mantenha as tarefas atualizadas para refletir o progresso real
                '''
            }
        },
        'Recursos de Conhecimento': {
            'Para que servem os Artigos Científicos?': {
                'icon': 'document-text',
                'icon_variant': 'solid',
                'content': '''Os Artigos Científicos são uma biblioteca de referências acadêmicas e profissionais que fundamentam as práticas de envelhecimento ativo. Eles servem como base de conhecimento para:
                1. Embasar decisões e estratégias
                2. Manter-se atualizado com as pesquisas mais recentes
                3. Compartilhar evidências científicas relevantes
                4. Promover práticas baseadas em evidências
                '''
            },
            'Boas Práticas': {
                'icon': 'light-bulb',
                'icon_variant': 'solid',
                'content': '''Para melhor utilização do sistema:
                1. Mantenha as informações atualizadas e precisas
                2. Use descrições claras e objetivas
                3. Organize as ações de forma lógica e estruturada
                4. Documente as decisões e seus fundamentos
                5. Compartilhe conhecimentos e aprendizados
                '''
            }
        }
    }
    
    return render(request, 'help/index.html', {'help_sections': help_sections})