import json
import math
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db.models import Count, Sum, Q
from .models import Operacao, SetorRota, PontoSinalizacao


def get_default_user():
    """Retorna o usuário administrador padrão ou o primeiro usuário cadastrado."""
    user = User.objects.filter(is_superuser=True).first()
    if not user:
        user = User.objects.first()
    if not user:
        user = User.objects.create_superuser('admin', 'admin@buscasmart.com', 'admin123')
    return user


def seed_dados_exemplo():
    """Popula a base com operações de exemplo caso não exista nenhuma cadastrada."""
    if Operacao.objects.exists():
        return

    user = get_default_user()

    # Operação 1: Em Andamento
    op1 = Operacao.objects.create(
        nome="Operação Serra dos Brandões — Busca Rural",
        descricao="Busca por trabalhador rural desaparecido nas imediações da Serra dos Brandões. Terreno pedregoso e mata densa de caatinga.",
        coordenador=user,
        area_total_km2=0.48,
        status="ANDAMENTO",
        versao=2,
        area_delimitada_geojson={
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-36.3550, -6.5080],
                    [-36.3400, -6.5080],
                    [-36.3400, -6.5200],
                    [-36.3550, -6.5200],
                    [-36.3550, -6.5080]
                ]]
            }
        }
    )

    # Setores da Op 1
    SetorRota.objects.create(
        operacao=op1,
        identificacao="Setor 01 — Trilha Norte",
        responsavel=user,
        cor_hex="#ef4444",
        instrucoes_especificas="Varredura em linha ao longo da crista da serra. Cuidado com despenhadeiros.",
        concluido=True
    )
    SetorRota.objects.create(
        operacao=op1,
        identificacao="Setor 02 — Encosta Leste",
        responsavel=None,
        cor_hex="#3b82f6",
        instrucoes_especificas="Avanço em leque próximo à grota do riacho seco.",
        concluido=False
    )
    SetorRota.objects.create(
        operacao=op1,
        identificacao="Setor 03 — Córrego do Meio",
        responsavel=None,
        cor_hex="#10b981",
        instrucoes_especificas="Área de vegetação fechada. Busca com cães e bastões de apoio.",
        concluido=False
    )
    SetorRota.objects.create(
        operacao=op1,
        identificacao="Setor 04 — Vale Sul",
        responsavel=None,
        cor_hex="#f59e0b",
        instrucoes_especificas="Acesso por estrada vicinal. Manter contato de rádio na frequência VHF 148.5.",
        concluido=False
    )

    # Pontos de Sinalização Op 1
    PontoSinalizacao.objects.create(
        operacao=op1,
        criado_por=user,
        titulo="Posto de Comando (ICP)",
        tipo="BASE",
        descricao="Base operacional com tenda de comando, comunicações e apoio médico.",
        latitude=-6.5122,
        longitude=-36.3469
    )
    PontoSinalizacao.objects.create(
        operacao=op1,
        criado_por=user,
        titulo="Último Ponto Visto (LKP)",
        tipo="ULTIMO_PONTO",
        descricao="Local onde a testemunha avistou o indivíduo pela última vez às 16h30.",
        latitude=-6.5155,
        longitude=-36.3430
    )
    PontoSinalizacao.objects.create(
        operacao=op1,
        criado_por=user,
        titulo="Pegada Recente no Riacho",
        tipo="EVIDENCIA",
        descricao="Marca de bota nº 40 compatível com o calçado da vítima, sentido Sul.",
        latitude=-6.5140,
        longitude=-36.3450
    )
    PontoSinalizacao.objects.create(
        operacao=op1,
        criado_por=user,
        titulo="Fenda Profunda / Risco de Queda",
        tipo="OBSTACULO",
        descricao="Abismo oculto por galhos. Evitar avanço noturno sem iluminação forte.",
        latitude=-6.5175,
        longitude=-36.3480
    )

    # Operação 2: Em Planejamento
    op2 = Operacao.objects.create(
        nome="Varredura Mata do Açude — Setor Oeste",
        descricao="Planejamento preliminar para delimitação de busca de jovem extraviado em trilha ecológica.",
        coordenador=user,
        area_total_km2=0.22,
        status="PLANEJAMENTO",
        versao=1,
        area_delimitada_geojson={
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-36.3650, -6.5250],
                    [-36.3550, -6.5250],
                    [-36.3550, -6.5350],
                    [-36.3650, -6.5350],
                    [-36.3650, -6.5250]
                ]]
            }
        }
    )
    SetorRota.objects.create(
        operacao=op2,
        identificacao="Setor 01 — Margem do Reservatório",
        cor_hex="#06b6d4",
        instrucoes_especificas="Inspeção da margem do reservatório de água.",
        concluido=False
    )

    # Operação 3: Concluída
    op3 = Operacao.objects.create(
        nome="Resgate Vale do Curimataú",
        descricao="Missão de resgate de ciclistas perdidos na serra. Vítimas localizadas com sucesso em menos de 4 horas de varredura.",
        coordenador=user,
        area_total_km2=0.85,
        status="CONCLUIDA",
        versao=3,
    )
    SetorRota.objects.create(
        operacao=op3,
        identificacao="Setor A — Trilha Principal",
        responsavel=user,
        cor_hex="#10b981",
        concluido=True
    )
    SetorRota.objects.create(
        operacao=op3,
        identificacao="Setor B — Mirante Alto",
        responsavel=user,
        cor_hex="#8b5cf6",
        concluido=True
    )


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# ==========================================
# VIEWS DE PÁGINAS (TEMPLATES)
# ==========================================

def login_view(request):
    """Tela de Autenticação Tática para Coordenadores e Administradores."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    erro = None
    if request.method == 'POST':
        usuario = request.POST.get('username', '').strip()
        senha = request.POST.get('password', '').strip()

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            erro = "Usuário ou senha inválidos. Verifique suas credenciais de comando."

    context = {
        'erro': erro,
        'pagina_ativa': 'login'
    }
    return render(request, 'operacoes/login.html', context)


def cadastro_view(request):
    """Tela de Cadastro de Novos Usuários (Coordenadores ou Voluntários)."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    erro = None
    sucesso = None
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        usuario = request.POST.get('username', '').strip().lower()
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('password', '').strip()
        confirmar_senha = request.POST.get('confirm_password', '').strip()

        if not usuario or not senha:
            erro = "Preencha todos os campos obrigatórios."
        elif senha != confirmar_senha:
            erro = "As senhas digitadas não coincidem."
        elif len(senha) < 4:
            erro = "A senha deve ter pelo menos 4 caracteres."
        elif User.objects.filter(username=usuario).exists():
            erro = f"O nome de usuário '{usuario}' já está cadastrado. Escolha outro."
        else:
            partes_nome = nome.split(' ', 1)
            primeiro_nome = partes_nome[0] if partes_nome else usuario
            sobrenome = partes_nome[1] if len(partes_nome) > 1 else ''

            novo_user = User.objects.create_user(
                username=usuario,
                email=email,
                password=senha,
                first_name=primeiro_nome,
                last_name=sobrenome
            )
            login(request, novo_user)
            return redirect('dashboard')

    context = {
        'erro': erro,
        'sucesso': sucesso,
        'pagina_ativa': 'cadastro'
    }
    return render(request, 'operacoes/cadastro.html', context)


def logout_view(request):
    """Encerra a sessão do Coordenador e redireciona para o login."""
    logout(request)
    return redirect('login')


def pagina_inicial_view(request):
    """Página Inicial Comercial / Institucional de Apresentação do BuscaSmart."""
    seed_dados_exemplo()
    operacoes_recentes = Operacao.objects.all().order_by('-criado_em')[:4]
    total_operacoes = Operacao.objects.count()
    total_setores = SetorRota.objects.count()
    area_total_km2 = Operacao.objects.aggregate(total=Sum('area_total_km2'))['total'] or 0.0

    context = {
        'operacoes_recentes': operacoes_recentes,
        'total_operacoes': total_operacoes,
        'total_setores': total_setores,
        'area_total_km2': round(area_total_km2, 2),
        'pagina_ativa': 'inicio'
    }
    return render(request, 'operacoes/pagina_inicial.html', context)


def dashboard_view(request):
    """Painel Geral do Coordenador (Inspirado nas Imagens 1 e 3)."""
    # Popula dados de demonstração se banco estiver vazio
    seed_dados_exemplo()

    operacoes = Operacao.objects.all().order_by('-criado_em')

    # Métricas Principais
    total_operacoes = operacoes.count()
    em_andamento = operacoes.filter(status='ANDAMENTO').count()
    planejamento = operacoes.filter(status='PLANEJAMENTO').count()
    concluidas = operacoes.filter(status='CONCLUIDA').count()

    # Cálculo da Área Total Mapeada
    area_total_km2 = operacoes.aggregate(total=Sum('area_total_km2'))['total'] or 0.0
    area_total_ha = area_total_km2 * 100

    # Eficiência Operacional e Varredura
    total_setores = SetorRota.objects.count()
    setores_concluidos = SetorRota.objects.filter(concluido=True).count()
    taxa_cobertura = round((setores_concluidos / total_setores * 100), 1) if total_setores > 0 else 0

    total_pontos = PontoSinalizacao.objects.count()
    total_evidencias = PontoSinalizacao.objects.filter(tipo='EVIDENCIA').count()

    context = {
        'operacoes': operacoes,
        'total_operacoes': total_operacoes,
        'em_andamento': em_andamento,
        'planejamento': planejamento,
        'concluidas': concluidas,
        'area_total_km2': round(area_total_km2, 2),
        'area_total_ha': round(area_total_ha, 1),
        'total_setores': total_setores,
        'setores_concluidos': setores_concluidos,
        'taxa_cobertura': taxa_cobertura,
        'total_pontos': total_pontos,
        'total_evidencias': total_evidencias,
        'agora': datetime.now(),
        'pagina_ativa': 'dashboard'
    }
    return render(request, 'operacoes/dashboard.html', context)


def painel_mapa(request, operacao_id=None):
    """Tela do Mapa Tático de Delimitação e Setores (Leaflet + Turf.js)."""
    operacao = None
    if operacao_id:
        operacao = get_object_or_404(Operacao, id=operacao_id)

    operacoes_recentes = Operacao.objects.all().order_by('-criado_em')[:10]

    context = {
        'operacao_atual': operacao,
        'operacoes_recentes': operacoes_recentes,
        'pagina_ativa': 'mapa'
    }
    return render(request, 'operacoes/mapa_operacao.html', context)


def gerenciar_equipe_view(request, operacao_id=None):
    """Gestão de Voluntários, Setores e Rotas de Busca."""
    operacoes = Operacao.objects.all().order_by('-criado_em')
    if operacao_id:
        operacao_selecionada = get_object_or_404(Operacao, id=operacao_id)
    else:
        operacao_selecionada = operacoes.filter(status='ANDAMENTO').first() or operacoes.first()

    setores = []
    if operacao_selecionada:
        setores = operacao_selecionada.setores.all().order_by('id')

    usuarios = User.objects.all().order_by('first_name', 'username')

    context = {
        'operacoes': operacoes,
        'operacao': operacao_selecionada,
        'setores': setores,
        'usuarios': usuarios,
        'pagina_ativa': 'equipe'
    }
    return render(request, 'operacoes/gerenciar_equipe.html', context)


def minha_rota_view(request, setor_id=None):
    """Tela do Voluntário em Campo: Minha Rota Individual, GPS e Modo Offline."""
    seed_dados_exemplo()
    if setor_id:
        setor = get_object_or_404(SetorRota, id=setor_id)
        operacao = setor.operacao
    else:
        setor = SetorRota.objects.filter(concluido=False).first() or SetorRota.objects.first()
        operacao = setor.operacao if setor else Operacao.objects.first()

    todos_setores = operacao.setores.all() if operacao else []
    pontos = operacao.pontos.all() if operacao else []

    context = {
        'setor': setor,
        'operacao': operacao,
        'todos_setores': todos_setores,
        'pontos': pontos,
        'pagina_ativa': 'minha_rota'
    }
    return render(request, 'operacoes/minha_rota.html', context)


def detalhes_operacao_view(request, operacao_id):
    """Relatório Operacional, Ficha de Missão e Pontos de Sinalização."""
    operacao = get_object_or_404(Operacao, id=operacao_id)
    setores = operacao.setores.all().order_by('id')
    pontos = operacao.pontos.all().order_by('-criado_em')

    setores_concluidos = setores.filter(concluido=True).count()
    total_setores = setores.count()
    taxa_conclusao = round((setores_concluidos / total_setores * 100), 1) if total_setores > 0 else 0

    context = {
        'operacao': operacao,
        'setores': setores,
        'pontos': pontos,
        'setores_concluidos': setores_concluidos,
        'total_setores': total_setores,
        'taxa_conclusao': taxa_conclusao,
        'pagina_ativa': 'detalhes'
    }
    return render(request, 'operacoes/detalhes_operacao.html', context)


def relatorio_oficial_view(request, operacao_id):
    """Visualização especial formatada para impressão/PDF de missão SAR."""
    operacao = get_object_or_404(Operacao, id=operacao_id)
    setores = operacao.setores.all().order_by('id')
    pontos = operacao.pontos.all().order_by('-criado_em')

    context = {
        'operacao': operacao,
        'setores': setores,
        'pontos': pontos,
        'data_emissao': datetime.now(),
        'pagina_ativa': 'relatorio'
    }
    return render(request, 'operacoes/relatorio_impressao.html', context)


def chat_ia_view(request):
    """Página de Chat Dedicado com a IA Tática BuscaSmart (Inspirado na Imagem 2)."""
    operacoes = Operacao.objects.all().order_by('-criado_em')[:5]
    context = {
        'operacoes': operacoes,
        'pagina_ativa': 'ia_chat'
    }
    return render(request, 'operacoes/chat_ia.html', context)


def sobre_view(request):
    """Página Institucional e Tecnologias (Inspirado nas Imagens 6, 7 e 8)."""
    context = {
        'pagina_ativa': 'sobre'
    }
    return render(request, 'operacoes/sobre.html', context)


# ==========================================
# ENDPOINTS DE API (JSON & IA)
# ==========================================

@csrf_exempt
def api_gerar_resumo_ia(request):
    """Gera um briefing tático executivo com IA para o Dashboard do Coordenador."""
    operacoes = Operacao.objects.all()
    total_op = operacoes.count()
    ativas = operacoes.filter(status='ANDAMENTO')
    planejando = operacoes.filter(status='PLANEJAMENTO')
    concluidas = operacoes.filter(status='CONCLUIDA')

    setores = SetorRota.objects.all()
    setores_pendentes = setores.filter(concluido=False).count()
    setores_concluidos = setores.filter(concluido=True).count()
    pontos_criticos = PontoSinalizacao.objects.filter(tipo__in=['EVIDENCIA', 'OBSTACULO'])

    nomes_ativas = ", ".join([op.nome for op in ativas]) if ativas.exists() else "Nenhuma no momento"

    resumo_html = f"""
    <div class="space-y-3 text-slate-200">
        <div class="flex items-center gap-2 text-emerald-400 font-semibold text-sm">
            <span>🛡️</span>
            <span>DIAGNÓSTICO OPERACIONAL EM TEMPO REAL — BUSCASMART IA</span>
        </div>
        <p class="text-sm leading-relaxed text-slate-300">
            Atualmente o sistema monitora <strong>{total_op} operações</strong> cadastradas, com 
            <span class="text-amber-400 font-medium">{ativas.count()} operação(ões) ativa(s) em campo</span> ({nomes_ativas}).
            Foram delimitados <strong>{setores.count()} setores operacionais</strong>, dos quais 
            <span class="text-emerald-400 font-medium">{setores_concluidos} já foram varridos</span> e 
            <span class="text-rose-400 font-medium">{setores_pendentes} permanecem abertos para cobertura</span>.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-2">
            <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-700/60">
                <span class="text-xs font-semibold text-orange-400 uppercase tracking-wider block mb-1">🚨 Ações Prioritárias Recomendadas:</span>
                <ul class="text-xs space-y-1 text-slate-300 list-disc list-inside">
                    <li>Alocar equipes nos setores com frentes abertas antes do crepúsculo.</li>
                    <li>Verificar vestígios cadastrados próximos ao Último Ponto Visto (LKP).</li>
                    <li>Sincronizar rotas GPS dos voluntários com o código de convite.</li>
                </ul>
            </div>
            <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-700/60">
                <span class="text-xs font-semibold text-cyan-400 uppercase tracking-wider block mb-1">🧭 Indicadores de Segurança SAR:</span>
                <p class="text-xs text-slate-300">
                    Existem <strong>{pontos_criticos.count()} pontos de interesse/evidência</strong> mapeados. 
                    Recomenda-se manter comunicação rádio VHF em canal aberto com as duplas de varredura.
                </p>
            </div>
        </div>
    </div>
    """

    return JsonResponse({
        'status': 'sucesso',
        'resumo_html': resumo_html,
        'total_ativas': ativas.count(),
        'gerado_em': datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
    })


@csrf_exempt
def api_chat_ia(request):
    """Processa perguntas do Coordenador e devolve respostas inteligentes e contextuais."""
    if request.method != 'POST':
        return JsonResponse({'erro': 'Método inválido'}, status=405)

    try:
        dados = json.loads(request.body)
        mensagem = dados.get('mensagem', '').strip().lower()
    except Exception:
        mensagem = request.POST.get('mensagem', '').strip().lower()

    if not mensagem:
        return JsonResponse({'resposta': 'Por favor, escreva uma mensagem ou selecione uma opção.'})

    operacoes = Operacao.objects.all()
    ativas = operacoes.filter(status='ANDAMENTO')
    total_setores = SetorRota.objects.count()
    setores_concluidos = SetorRota.objects.filter(concluido=True).count()
    pontos = PontoSinalizacao.objects.all()

    # Lógica de resposta inteligente contextual
    if any(s in mensagem for s in ['bom dia', 'boa tarde', 'boa noite', 'olá', 'ola', 'oi', 'e ai', 'opa']):
        if 'boa tarde' in mensagem:
            saudacao = "**Boa tarde, Coordenador!** 👋"
        elif 'boa noite' in mensagem:
            saudacao = "**Boa noite, Coordenador!** 👋"
        elif 'bom dia' in mensagem:
            saudacao = "**Bom dia, Coordenador!** 👋"
        else:
            hora = datetime.now().hour
            saudacao = "**Bom dia, Coordenador!** 👋" if hora < 12 else ("**Boa tarde, Coordenador!** 👋" if hora < 18 else "**Boa noite, Coordenador!** 👋")

        resposta = (
            f"{saudacao}\n\n"
            f"Sou o assistente tático do **BuscaSmart**.\n\n"
            f"Posso te ajudar de forma simples e direta com:\n"
            f"• **Status das buscas:** ver quais frentes e voluntários estão em andamento;\n"
            f"• **Divisão de setores:** orientar como distribuir as equipes no terreno de Picuí;\n"
            f"• **Rotas e LKP:** como delimitar a área a partir do último ponto visto;\n"
            f"• **Resumo geral:** conferir hectares varridos, pontos críticos e pendências.\n\n"
            f"Como posso ajudar a sua operação agora?"
        )

    elif any(s in mensagem for s in ['status', 'operacoes', 'operações', 'ativas', 'andamento']):
        if ativas.exists():
            lista = "\n".join([f"• **{op.nome}** (Código `{op.codigo_convite}`) — Área: {op.area_total_km2} km² ({round(op.area_total_km2 * 100, 1)} ha)" for op in ativas])
            resposta = (
                f"🚨 **Situação Atual das Operações:**\n\n"
                f"Temos **{ativas.count()} operação(ões) ativa(s)** no momento:\n{lista}\n\n"
                f"📊 **Progresso Geral dos Setores:**\n"
                f"• Setores concluídos: **{setores_concluidos} de {total_setores}** "
                f"({round((setores_concluidos/total_setores*100) if total_setores else 0, 1)}% varrido).\n\n"
                f"Quer ver os detalhes de alguma operação específica?"
            )
        else:
            resposta = (
                "No momento não há operações em status **ANDAMENTO**. Há missões em planejamento ou concluídas. "
                "Você pode ativar uma operação diretamente pelo **Painel de Operações** ou criar uma nova no **Mapa Tático**."
            )

    elif any(s in mensagem for s in ['equipe', 'equipes', 'voluntario', 'voluntário', 'participante', 'alocacao', 'alocação']):
        resposta = (
            "👥 **Diretrizes de Alocação de Equipes (Protocolo SAR):**\n\n"
            "1. **Tamanho das Equipes:** Nunca envie voluntários sozinhos. O ideal são duplas ou trios com ao menos um socorrista experiente.\n"
            "2. **Divisão por Setores:** Cada equipe deve cobrir faixas paralelas com espaçamento visual de 5 a 15 metros, dependendo da densidade da vegetação.\n"
            "3. **Código de Convite:** Para novos integrantes, compartilhe o código de convite da missão. Eles podem escanear o QR Code direto no celular para receber suas rotas delimitadas."
        )

    elif any(s in mensagem for s in ['perimetro', 'perímetro', 'setor', 'setores', 'mapa', 'raio', 'lkp']):
        resposta = (
            "🗺️ **Análise de Perímetro e Delimitação Geográfica:**\n\n"
            "• **LKP (Último Ponto Visto):** Estabeleça um raio concêntrico inicial de 1 a 2 km a partir do LKP como 'Área de Alta Probabilidade'.\n"
            "• **Uso de Barreiras Naturais:** Aproveite riachos, estradas vicinais e cercas para delimitar os limites externos dos polígonos no Leaflet.\n"
            "• **Divisão Automática:** Use o algoritmo do BuscaSmart no mapa para dividir polígonos complexos em faixas verticais balanceadas conforme o número de duplas disponíveis."
        )

    elif any(s in mensagem for s in ['resumo', 'completo', 'relatorio', 'relatório', 'geral']):
        area_total = operacoes.aggregate(total=Sum('area_total_km2'))['total'] or 0.0
        resposta = (
            f"📋 **Resumo Executivo Consolidado — BuscaSmart:**\n\n"
            f"• **Total de Operações:** {operacoes.count()}\n"
            f"• **Missões Ativas:** {ativas.count()}\n"
            f"• **Área Total Mapeada:** {round(area_total, 2)} km² ({round(area_total * 100, 1)} hectares)\n"
            f"• **Setores Operacionais:** {total_setores} cadastrados ({setores_concluidos} concluídos)\n"
            f"• **Pontos de Evidência & Risco:** {pontos.count()} marcadores registrados\n\n"
            f"💡 **Recomendação Tática:** Concentre o efetivo nos setores pendentes com maior proximidade de fontes de água e trilhas conhecidas."
        )

    elif any(s in mensagem for s in ['ajuda', 'socorro', 'comando', 'oque voce faz', 'funcionalidade']):
        resposta = (
            "🧭 **Como posso te ajudar no comando da busca:**\n\n"
            "• Diga **'Status'** para ver as buscas ativas no terreno.\n"
            "• Diga **'Equipe'** para orientações de segurança e alocação de voluntários.\n"
            "• Diga **'Perímetro'** para dicas de raio de busca e delimitação de setores.\n"
            "• Diga **'Resumo'** para um panorama completo de todas as missões cadastradas."
        )

    else:
        # Resposta inteligente padrão
        resposta = (
            f"Entendi sua solicitação sobre *'{mensagem}'*.\n\n"
            f"Como assistente tático do BuscaSmart, posso cruzar os dados dos polígonos geográficos e das equipes cadastradas "
            f"para otimizar sua tomada de decisão. Deseja verificar o **status das missões ativas**, "
            f"revisar a **alocação de equipes** ou consultar o **resumo do terreno**?"
        )

    return JsonResponse({
        'resposta': resposta,
        'timestamp': datetime.now().strftime("%H:%M:%S")
    })


@csrf_exempt
def api_salvar_operacao(request):
    """Salva uma nova operação com GeoJSON e setores no banco de dados."""
    if request.method != 'POST':
        return JsonResponse({'erro': 'Método POST obrigatório'}, status=405)

    try:
        dados = json.loads(request.body)
        nome = dados.get('nome', '').strip()
        descricao = dados.get('descricao', 'Operação criada via painel tático.')
        area_geojson = dados.get('area_delimitada_geojson')
        area_total_km2 = float(dados.get('area_total_km2', 0.0))
        setores_dados = dados.get('setores', [])

        if not nome:
            return JsonResponse({'erro': 'Nome da operação é obrigatório'}, status=400)

        user = get_default_user()

        operacao = Operacao.objects.create(
            nome=nome,
            descricao=descricao,
            coordenador=user,
            area_delimitada_geojson=area_geojson,
            area_total_km2=area_total_km2,
            status='ANDAMENTO'
        )

        # Salva os setores se fornecidos
        for s in setores_dados:
            props = s.get('properties', {})
            identificacao = props.get('identificacao', f"Setor {s.get('id', 'N/A')}")
            cor = props.get('cor_hex', '#3B82F6')
            SetorRota.objects.create(
                operacao=operacao,
                identificacao=identificacao,
                cor_hex=cor,
                poligono_setor_geojson=s,
                concluido=False
            )

        return JsonResponse({
            'status': 'sucesso',
            'id': operacao.id,
            'nome': operacao.nome,
            'codigo_convite': operacao.codigo_convite,
            'area_total_km2': operacao.area_total_km2,
            'mensagem': 'Operação e setores salvos com sucesso no banco de dados!'
        })

    except Exception as e:
        return JsonResponse({'erro': str(e)}, status=500)


@csrf_exempt
def api_atualizar_setor(request, setor_id):
    """Atualiza o status de conclusão e responsável de um setor."""
    setor = get_object_or_404(SetorRota, id=setor_id)
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            if 'concluido' in dados:
                setor.concluido = bool(dados['concluido'])
            if 'responsavel_id' in dados:
                resp_id = dados['responsavel_id']
                setor.responsavel = User.objects.filter(id=resp_id).first() if resp_id else None
            if 'instrucoes_especificas' in dados:
                setor.instrucoes_especificas = dados['instrucoes_especificas']

            setor.save()
            return JsonResponse({
                'status': 'sucesso',
                'id': setor.id,
                'concluido': setor.concluido,
                'responsavel': setor.responsavel.username if setor.responsavel else 'Não atribuído'
            })
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)

    return JsonResponse({'erro': 'Método inválido'}, status=405)


@csrf_exempt
def api_adicionar_ponto(request, operacao_id):
    """Cadastra um novo ponto de sinalização na operação."""
    operacao = get_object_or_404(Operacao, id=operacao_id)
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            ponto = PontoSinalizacao.objects.create(
                operacao=operacao,
                criado_por=get_default_user(),
                titulo=dados.get('titulo', 'Ponto de Sinalização'),
                tipo=dados.get('tipo', 'REFERENCIA'),
                descricao=dados.get('descricao', ''),
                latitude=float(dados.get('latitude')),
                longitude=float(dados.get('longitude'))
            )
            return JsonResponse({
                'status': 'sucesso',
                'id': ponto.id,
                'titulo': ponto.titulo,
                'tipo': ponto.tipo,
                'latitude': ponto.latitude,
                'longitude': ponto.longitude
            })
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)

    return JsonResponse({'erro': 'Método inválido'}, status=405)
