from django.urls import path
from . import views

urlpatterns = [
    # Autenticação (Login, Cadastro e Logout de Coordenadores)
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),

    # Página Inicial (Landing Page Comercial de Apresentação)
    path('', views.pagina_inicial_view, name='pagina_inicial'),
    
    # Painel Geral do Coordenador (Dashboard)
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Mapa Tático e Operações
    path('mapa/', views.painel_mapa, name='painel_mapa'),
    path('mapa/<int:operacao_id>/', views.painel_mapa, name='painel_mapa_operacao'),
    
    # Gestão de Equipe e Rotas
    path('equipe/', views.gerenciar_equipe_view, name='gerenciar_equipe'),
    path('equipe/<int:operacao_id>/', views.gerenciar_equipe_view, name='gerenciar_equipe_operacao'),
    path('rota/', views.minha_rota_view, name='minha_rota'),
    path('rota/<int:setor_id>/', views.minha_rota_view, name='minha_rota_setor'),
    
    # Ficha Técnica e Relatórios
    path('detalhes/<int:operacao_id>/', views.detalhes_operacao_view, name='detalhes_operacao'),
    path('relatorio/<int:operacao_id>/', views.relatorio_oficial_view, name='relatorio_oficial'),
    
    # Inteligência Artificial e Institucional
    path('ia/chat/', views.chat_ia_view, name='chat_ia'),
    path('sobre/', views.sobre_view, name='sobre_projeto'),

    # Endpoints de API e IA
    path('api/ia/resumo/', views.api_gerar_resumo_ia, name='api_gerar_resumo_ia'),
    path('api/ia/chat/', views.api_chat_ia, name='api_chat_ia'),
    path('api/operacoes/salvar/', views.api_salvar_operacao, name='api_salvar_operacao'),
    path('api/setores/<int:setor_id>/atualizar/', views.api_atualizar_setor, name='api_atualizar_setor'),
    path('api/operacoes/<int:operacao_id>/adicionar-ponto/', views.api_adicionar_ponto, name='api_adicionar_ponto'),
]
