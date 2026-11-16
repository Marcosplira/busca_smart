# BuscaSmart — Sistema Integrado de Busca e Salvamento Territorial (SAR)

Sistema web profissional para planejamento, delimitação e coordenação tática de operações de busca e resgate em áreas rurais, de mata e terreno acidentado. O projeto utiliza **Python 3.12**, **Django 6.1**, **Django REST Framework**, **Leaflet**, **Turf.js**, **Tailwind CSS** e **Inteligência Artificial Tática Integrada**.

---

## 📁 Estrutura do Projeto

```text
busca_smart/
├── buscasmart_core/
│   ├── settings.py           # Configurações do projeto Django
│   ├── urls.py               # Roteamento global de URLs
│   ├── wsgi.py               # Ponto de entrada WSGI
│   └── asgi.py               # Ponto de entrada ASGI
├── operacoes/
│   ├── migrations/           # Migrações do banco de dados SQLite/PostgreSQL
│   ├── templates/operacoes/
│   │   ├── base.html         # Layout tático principal com sidebar e relógio
│   │   ├── dashboard.html    # Painel geral com KPIs e Resumo com IA
│   │   ├── mapa_operacao.html# Delimitação de área, Turf.js e divisão de setores
│   │   ├── chat_ia.html      # Assistente de IA para suporte ao coordenador
│   │   ├── gerenciar_equipe.html # Gestão de voluntários, rotas e QR Code
│   │   ├── detalhes_operacao.html # Ficha técnica, mini-mapa e evidências
│   │   ├── relatorio_impressao.html # Relatório oficial pronto para PDF/Impressão
│   │   └── sobre.html        # Apresentação institucional e tecnologias
│   ├── admin.py              # Interface administrativa do Django
│   ├── models.py             # Modelos Operacao, SetorRota, PontoSinalizacao
│   ├── serializers.py        # Serializadores Django REST Framework
│   ├── tests.py              # Testes automatizados do sistema
│   ├── views.py              # Views completas, APIs e Motor de IA
│   └── urls.py               # Rotas e endpoints REST da aplicação
├── .dockerignore
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📋 Templates HTML do Projeto

1. **`base.html`** *(Template Pai / Layout Base Tático)*
   - Barra lateral retrátil com navegação unificada, perfil do coordenador e badge SAR.
   - Topbar com relógio digital em tempo real (`Sexta-feira, 13 de novembro...`) e saudação personalizada.

2. **`dashboard.html`** *(Painel Geral do Coordenador)*
   - KPIs no topo: Operações Ativas, Planejamento, Concluídas e Área Mapeada (km² / ha).
   - **Card "Resumo com IA"**: Botão para geração de briefing tático em 1 clique via API assíncrona.
   - Painel de Eficiência Operacional SAR (% de varredura concluída com barra de progresso).
   - Lista filtrável de operações em tempo real (todas, andamento, planejamento, concluídas).
   - Ações rápidas com atalhos para mapa, equipe, QR Code e assistente.

3. **`mapa_operacao.html`** *(Painel de Delimitação e Setores)*
   - Camadas de satélite de alta resolução (Esri) e mapa de ruas (OSM).
   - Ferramenta de desenho de polígonos e retângulos com cálculo em tempo real de hectares e km² via Turf.js.
   - Algoritmo de divisão automática em faixas verticais balanceadas conforme o número de duplas disponíveis.
   - Salvamento direto no banco de dados SQLite via API `/api/operacoes/salvar/`.

4. **`chat_ia.html`** *(Assistente de IA BuscaSmart)*
   - Interface conversacional moderna em dark theme inspirada em assistentes executivos.
   - Respostas inteligentes para saudações ("Bom dia!"), consultas de status das missões e protocolos SAR.
   - Atalhos rápidos em chips: `👋 Bom dia!`, `📊 Status das Operações`, `🗺️ Análise de Perímetro`, `👥 Alocação de Equipes` e `📄 Resumo Completo`.

5. **`gerenciar_equipe.html`** *(Gestão de Participantes e Rotas)*
   - Código de convite exclusivo da missão (`BUSCA-XXXXXX`) com botão de cópia e gerador de QR Code.
   - Atribuição de voluntários aos setores identificados no mapa.
   - Controle de status individual de varredura com alternador visual imediato.

6. **`detalhes_operacao.html`** *(Ficha de Missão e Evidências)*
   - Telemetria consolidada, mini-mapa com polígonos renderizados e pontos georreferenciados.
   - Cadastro e histórico de pontos de interesse: Base ICP, Último Ponto Visto (LKP), Evidências e Obstáculos.

7. **`relatorio_impressao.html`** *(Relatório Oficial SAR)*
   - Formatado especialmente para impressão em papel e exportação limpa em PDF (`@media print`).
   - Tabelas formais de parâmetros geográficos, setores, evidências com coordenadas e campos para assinaturas.

8. **`sobre.html`** *(Institucional, Objetivos e Tecnologias)*
   - Apresentação dos 3 pilares: **Organização**, **Visibilidade** e **Gestão**.
   - Seção de tecnologias e créditos ao desenvolvedor **Marcos Paulo Santos Lira**.
   - QR Code de acesso mobile.

---

## 🚀 Como Executar

### Execução Direta (Local)

1. Ative o ambiente virtual:
   ```powershell
   .\venv\Scripts\activate
   ```
2. Aplique as migrações (se necessário):
   ```powershell
   python manage.py migrate
   ```
3. Inicie o servidor Django:
   ```powershell
   python manage.py runserver
   ```
4. Acesse no navegador:
   - **Dashboard Principal:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - **Mapa Tático:** [http://127.0.0.1:8000/mapa/](http://127.0.0.1:8000/mapa/)
   - **Chat com IA:** [http://127.0.0.1:8000/ia/chat/](http://127.0.0.1:8000/ia/chat/)
   - **Sobre o Projeto:** [http://127.0.0.1:8000/sobre/](http://127.0.0.1:8000/sobre/)

---

## 👨‍💻 Desenvolvedor

**Marcos Paulo Santos Lira**  
Projeto desenvolvido para contribuir com a coordenação, agilidade e segurança das operações de busca e salvamento territorial através da tecnologia.
