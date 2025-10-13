BEGIN TRANSACTION;

INSERT INTO planning_level(name, level_number) VALUES ('1', 1) ON CONFLICT DO NOTHING;

INSERT INTO planning_axis (name) VALUES ('Mobilidade urbana inclusiva');
INSERT INTO planning_project_level_axis (level_id, axis_id, progress_percentage) VALUES (1, 1, 0) ON CONFLICT DO NOTHING;

-- 1

INSERT INTO planning_action (level_id, axis_id, name) VALUES 
(1, 1, 'Integrar gratuidade no transporte com infraestrutura digital para reduzir exclusão social urbana - Marè et al.'),
(1, 1, 'Ajustar infraestrutura urbana para segurança de idosos melhorando semáforos faixas e travessias - GÁLVEZ-PÉREZ'),
(1, 1, 'Adaptar pontos de acesso ao transporte público garantindo acessibilidade física e informacional - AZEVEDO'),
(1, 1, 'Centralizar necessidades dos idosos na política de mobilidade priorizando decisões baseadas em dados - Aguiar'),
(1, 1, 'Garantir acessibilidade em deslocamentos urbanos removendo barreiras físicas e sociais - Bernardo'),
(1, 1, 'Integrar tecnologia inteligente para travessias seguras usando sensores e sinalização adaptiva - Liz'),
(1, 1, 'Criar sistema de mobilidade regional integrado conectando diferentes modais e territórios - Baltazar'),
(1, 1, 'Manter infraestrutura urbana com regras específicas estabelecendo padrões permanentes de acessibilidade - Kuo'),
(1, 1, 'Analisar dados de cartões inteligentes do transporte identificando padrões de uso por idosos - CHEN'),
(1, 1, 'Incentivar mudança modal com políticas específicas promovendo alternativas ao transporte individual - LEE'),
(1, 1, 'Aplicar análise de dados para políticas inclusivas usando big data para decisões - Sheikh & van Ameijde'),
(1, 1, 'Aplicar framework de caminhabilidade urbana avaliando qualidade das rotas pedestres - HE & HE'),
(1, 1, 'Subsidiar serviços de transporte personalizado oferecendo modalidades adaptadas e acompanhamento - Latiff & Mohd'),
(1, 1, 'Requalificar infraestrutura urbana periférica focando áreas com menor acessibilidade - ULLOA-LEON'),
(1, 1, 'Criar políticas de mobilidade microdirecionadas por bairro adaptando soluções às especificidades locais - Burlano')
ON CONFLICT DO NOTHING;

-- 2

INSERT INTO planning_axis (name) VALUES ('Inclusão digital e capacitação');
INSERT INTO planning_project_level_axis (level_id, axis_id, progress_percentage) VALUES (1, 2, 0) ON CONFLICT DO NOTHING;

INSERT INTO planning_action (level_id, axis_id, name) VALUES 
(1, 2, 'Promover cursos de alfabetização digital para mulheres idosas focando especificamente no público feminino - Silva et al.'),
(1, 2, 'Oferecer serviços públicos via aplicativos smartphone digitalizando atendimento e processos municipais - Duque'),
(1, 2, 'Garantir apoio público permanente para inclusão digital estabelecendo programas contínuos de suporte - Alexopoulou'),
(1, 2, 'Desenvolver robôs sociais para mitigar solidão usando tecnologia para companhia virtual - TSCHIDA'),
(1, 2, 'Treinar usuários de PMDs e condutores capacitando para uso seguro de verículos - Kuo'),
(1, 2, 'Realizar campanhas de capacitação digital promovendo eventos pontuais de educação - RAZALI'),
(1, 2, 'Criar ecossistema digital inclusivo via IoT integrando dispositivos para facilitar acesso - Alexandre'),
(1, 2, 'Personalizar rotas de caminhada por aplicativo adaptando trajetos às capacidades individuais - Queirós'),
(1, 2, 'Reduzir exclusão digital em áreas rurais levando conectividade para regiões remotas - HE A'),
(1, 2, 'Promover capacitação com apoio familiar envolvendo parentes no processo educativo - Shi'),
(1, 2, 'Investir em infraestrutura digital para economia fortalecendo base tecnológica para inclusão - HE B'),
(1, 2, 'Implementar formação digital contínua oferecendo educação permanente em tecnologia - Lu Wanjun'),
(1, 2, 'Adaptar interfaces digitais culturais ao idoso considerando aspectos regionais e tradicionais - Hu et al'),
(1, 2, 'Implementar previsão de exclusão digital com ML usando inteligência artificial para identificar idosos vulneráveis - PARK JR'),
(1, 2, 'Adaptar interfaces governamentais para idosos simplificando sistemas públicos digitais existentes - Papí‐Gálvez'),
(1, 2, 'Priorizar inclusão digital para mulheres viúvas atendendo grupo específico em vulnerabilidade - Silva B'),
(1, 2, 'Implementar educação digital continuada urbana oferecendo aprendizado permanente nas cidades - Liu'),
(1, 2, 'Oferecer treinamento digital com suporte social combinando educação tecnológica e apoio - Tsai')
ON CONFLICT DO NOTHING;

-- 3

INSERT INTO planning_axis (name) VALUES ('Saúde conectada e monitoramento');
INSERT INTO planning_project_level_axis (level_id, axis_id, progress_percentage) VALUES (1, 3, 0) ON CONFLICT DO NOTHING;

INSERT INTO planning_action (level_id, axis_id, name) VALUES
(1, 3, 'Implementar soluções de saúde conectada seguras garantindo privacidade e proteção de dados pessoais - SOJA'),
(1, 3, 'Adotar sistemas IoT-AAL para monitoramento usando dispositivos inteligentes para cuidado - Almeida'),
(1, 3, 'Criar ecossistema colaborativo para cuidados personalizados integrando múltiplos atores em saúde - Baldissera'),
(1, 3, 'Desenvolver sistemas híbridos com tecnologia de avaliação geriátrica combinando presencial e remoto  - Urusevic'),
(1, 3, 'Monitorar preditivamente demência com IA urbana identificando precocemente sinais de declínio - Zhang'),
(1, 3, 'Implementar tecnologia 6G para ecossistema de saúde usando conectividade avançada para cuidados - Mucchi'),
(1, 3, 'Coletar dados de caminhada via aplicativo registrando atividade física para análise - Rodriguez'),
(1, 3, 'Integrar monitoramento com sensores móveis usando dispositivos portáteis para acompanhamento - BERTINI'),
(1, 3, 'Ativar monitoramento automatizado via sensores vestíveis implementando supervisão contínua da saúde - SU'),
(1, 3, 'Identificar atividades de idosos por áreas urbanas mapeando comportamentos e necessidades locais - CHEN'),
(1, 3, 'Implantar infraestrutura IoT na saúde rural levando tecnologia para áreas remotas - RAZALI'),
(1, 3, 'Integrar sensores via ontologias de saúde padronizando comunicação entre dispositivos médicos - BELANI'),
(1, 3, 'Co-criar soluções de eHealth em cidades inteligentes desenvolvendo tecnologia com participação cidadã - QVARFORDT'),
(1, 3, 'Implementar monitoramento remoto e telereabilitação oferecendo cuidados à distância especializados - Gaspar et al.'),
(1, 3, 'Treinar habilidades digitais em e-saúde capacitando idosos para autogestão digital - AUNG'),
(1, 3, 'Integrar telemedicina e sistemas digitais conectando consultas remotas com prontuários - KOWALSKA'),
(1, 3, 'Implantar centros de saúde comunitários conectados criando pontos físicos com tecnologia - KOWALSKA'),
(1, 3, 'Adotar infraestrutura interoperável IoT e IA permitindo comunicação entre sistemas diversos - Valero'),
(1, 3, 'Aplicar Persuasive System Design em aplicativos usando psicologia para adesão terapêutica - CABRITA'),
(1, 3, 'Registrar atividades físicas e sono via dispositivos vestíveis apoiando cuidados remotos - Bryant'),
(1, 3, 'Disponibilizar painel web para profissionais definirem intervenções personalizadas por idoso - Rodriguez')
ON CONFLICT DO NOTHING;

-- 4

INSERT INTO planning_axis (name) VALUES ('Habitação adaptada e espaço urbano');
INSERT INTO planning_project_level_axis (level_id, axis_id, progress_percentage) VALUES (1, 4, 0) ON CONFLICT DO NOTHING;

INSERT INTO planning_action (level_id, axis_id, name) VALUES 
(1, 4, 'Implantar pequenas áreas verdes urbanas acessíveis criando espaços naturais adaptados aos idosos com conforto e orientação espacial - Caronte'),
(1, 4, 'Criar espaços públicos que promovam autonomia desenhando ambientes que favorecem independência - Jorge'),
(1, 4, 'Adaptar espaços públicos para segurança de idosos modificando ambientes para prevenir acidentes - Sarlo'),
(1, 4, 'Avaliar espaços urbanos vulneráveis com acessibilidade diagnosticando locais que precisam melhorias - AGOST-FELIP'),
(1, 4, 'Monitorar padrões domiciliares com sensores inteligentes acompanhando rotinas residenciais para segurança - SU'),
(1, 4, 'Implantar moradias modulares com tecnologia assistiva construindo residências adaptáveis e inteligentes - Gibilisco'),
(1, 4, 'Promover políticas urbanas para moradia adaptada estabelecendo regulamentações para habitação inclusiva - PREDA'),
(1, 4, 'Implementar transporte multimodal com tecnologias digitais integrando diferentes modalidades via tecnologia - Labus')
ON CONFLICT DO NOTHING;

-- 5

INSERT INTO planning_axis (name) VALUES ('Participação social e governança');
INSERT INTO planning_project_level_axis (level_id, axis_id, progress_percentage) VALUES (1, 5, 0) ON CONFLICT DO NOTHING;

INSERT INTO planning_action (level_id, axis_id, name) VALUES 
(1, 5, 'Implantar canais digitais para participação de idosos criando plataformas online para engajamento - ZRAŁEK'),
(1, 5, 'Engajar idosos no planejamento de iniciativas locais incluindo população sênior em decisões - NAPIER'),
(1, 5, 'Implementar plataforma digital integrada para idosos centralizando serviços e informações urbanas - Wroclaw'),
(1, 5, 'Promover comunicação direta entre moradores e profissionais facilitando diálogo entre cidadãos e gestores urbanos - Rodriguez'),
(1, 5, 'Adotar avatar robô para participação social remota usando tecnologia para presença virtual - SU'),
(1, 5, 'Incentivar interação intergeracional por aplicativo conectando diferentes faixas etárias digitalmente - GOMES'),
(1, 5, 'Realizar co-design de soluções urbanas com idosos desenvolvendo projetos com participação ativa - Woolrych'),
(1, 5, 'Promover treinamento comunitário para tecnologia capacitando grupos locais em ferramentas - Shi'),
(1, 5, 'Promover políticas age-friendly com co-produção criando regulamentações com participação cidadã - Buffel & Phillipson'),
(1, 5, 'Incluir idosos no planejamento urbano universal, garantindo representação em todos os projetos e implementando princípios de justiça espacia - DRILLING '),
(1, 5, 'Desenvolver plataforma colaborativa com IoT e IA criando sistema inteligente para participação - Nápoles'),
(1, 5, 'Criar plataforma colaborativa com validação participativa estabelecendo sistema de aprovação comunitária - Van Hoof')
ON CONFLICT DO NOTHING;

-- 6

INSERT INTO planning_axis (name) VALUES ('Planejamento urbano sustentável');
INSERT INTO planning_project_level_axis (level_id, axis_id, progress_percentage) VALUES (1, 6, 0) ON CONFLICT DO NOTHING;

INSERT INTO planning_action (level_id, axis_id, name) VALUES 
(1, 6, 'Criar índices de mobilidade para avaliar acessibilidade desenvolvendo métricas para medir qualidade - RIBEIRO'),
(1, 6, 'Implementar gêmeos digitais para políticas urbanas usando simulação virtual para planejamento - Zhou'),
(1, 6, 'Integrar plataforma digital com sensores urbanos conectando dados da cidade em sistema unificado - Bryant'),
(1, 6, 'Implementar zonas exclusivas de estacionamento PMDs criando áreas específicas para dispositivos - Kuo'),
(1, 6, 'Coletar dados contextuais urbanos para rotas registrando informações ambientais para navegação - Bertini'),
(1, 6, 'Realizar diagnóstico participativo das necessidades mapeando demandas com envolvimento comunitário - ZHANG'),
(1, 6, 'Utilizar gêmeos digitais locais para planejamento urbano aplicando modelagem virtual para bairros - Villanueva-Merino')
ON CONFLICT DO NOTHING;

COMMIT;