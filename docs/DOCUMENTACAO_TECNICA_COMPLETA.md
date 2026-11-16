# 🛠️ Documentação Técnica Completa da Arquitetura — BuscaSmart
## Especificação de Engenharia de Software, Modelagem Geoespacial e Deploy

---

## 1. 🏗️ Arquitetura do Sistema

O BuscaSmart foi desenvolvido seguindo o padrão arquitetural **MVT (Model-View-Template)** do framework **Django 5**, enriquecido com uma suíte de processamento geoespacial em **JavaScript (Leaflet + Turf.js)** e preparado para empacotamento móvel via **Capacitor (Ionic)**.

```
+-------------------------------------------------------------------------+
|                              BUSCASMART                                 |
+------------------------------------+------------------------------------+
|         PAINEL WEB COORDENAÇÃO     |        APP MOBILE VOLUNTÁRIO       |
|  - Django Templates                |  - HTML5 Responsive View           |
|  - Tailwind CSS Tactical Dark      |  - GPS Geolocation API (Satélite)  |
|  - Leaflet Map & Esri Satélite     |  - LocalStorage Offline Cache      |
|  - Turf.js Geo-Partitioning        |  - Sincronização Assíncrona        |
+------------------------------------+------------------------------------+
                                      |
                      HTTP REST / AJAX JSON APIs
                                      |
+-------------------------------------------------------------------------+
|                          BACKEND (DJANGO 5)                             |
|  - Auth & Permission Engine (Coordenadores vs Voluntários)             |
|  - Geo-Data REST Endpoints (/api/operacoes/salvar/, etc.)              |
|  - Engine Heurística de IA SAR (Briefing & Chatbot Situacional)        |
+-------------------------------------------------------------------------+
                                      |
+-------------------------------------------------------------------------+
|                        BANCO DE DADOS (ORM)                             |
|  - SQLite3 (Desenvolvimento e Teste de Campo)                           |
|  - PostgreSQL + PostGIS (Produção e Alta Escala Geográfica)             |
+-------------------------------------------------------------------------+
```

---

## 2. 💻 Stack Tecnológica

| Camada | Tecnologia | Versão / Biblioteca | Finalidade |
| :--- | :--- | :--- | :--- |
| **Backend Core** | Python | 3.12+ | Linguagem base de processamento e lógica |
| **Web Framework** | Django | 5.x | ORM, autenticação, roteamento, templates e APIs |
| **Frontend Styling** | Tailwind CSS | 3.x CDN | Design responsivo tático de alto contraste (*Tactical Dark*) |
| **Visualização GIS** | Leaflet | 1.9.4 | Renderização de camadas cartográficas e polígonos |
| **Provedor de Satélite** | Esri World Imagery | ArcGIS Online | Imagens de satélite globais de alta resolução |
| **Cálculo Geoespacial** | Turf.js | 6.5.0 | Particionamento poligonal, cálculo de área e perímetro |
| **Telemetria Mobile** | Geolocation API | W3C Standard | Captura contínua de satélites GNSS (GPS, Glonass) |
| **Banco de Dados** | SQLite3 / PostGIS | Padrão Django | Armazenamento de missões, setores GeoJSON e pontos |
| **Mobile Bridge** | Capacitor | 6.x | Empacotamento para Android Nativo (APK / AAB) |

---

## 3. 📂 Estrutura de Diretórios do Projeto

```
c:\Users\Marcos Paulo\Desktop\busca_smart\busca_smart\
│
├── buscasmart_core/          # Configurações globais do projeto Django
│   ├── settings.py           # Configuração de apps, templates, banco e segurança
│   ├── urls.py               # Roteamento raiz (/admin/ e rotas de operacoes)
│   ├── wsgi.py / asgi.py     # Pontos de entrada de servidores HTTP e assíncronos
│
├── operacoes/                # Aplicação principal de SAR e Defesa Civil
│   ├── models.py             # Modelagem de Operacao, SetorRota, PontoSinalizacao
│   ├── views.py              # Controladores de tela e APIs JSON de IA e Mapa
│   ├── urls.py               # Rotas (/dashboard/, /mapa/, /equipe/, /rota/, etc.)
│   ├── admin.py              # Django Admin customizado com inlines e badges
│   ├── static/operacoes/     # Imagens de resgate, CSS e scripts
│   └── templates/operacoes/  # Templates HTML Django
│       ├── base.html         # Template pai com navegação tática e relógio
│       ├── pagina_inicial.html # Landing page de alto impacto comercial
│       ├── login.html        # Autenticação com preenchimento tático
│       ├── cadastro.html     # Cadastro de novos voluntários
│       ├── dashboard.html    # Painel geral com KPIs e Card de IA
│       ├── mapa_operacao.html# Mapa satélite com desenho e auto-divisão
│       ├── gerenciar_equipe.html # Efetivo, atribuição e QR Code
│       ├── minha_rota.html   # Tela mobile do voluntário com GPS e offline
│       ├── detalhes_operacao.html # Dossiê com mini-mapa e evidências
│       ├── relatorio_impressao.html # Relatório oficial pronto para PDF
│       ├── chat_ia.html      # Chatbot conversacional com IA SAR
│       └── sobre.html        # Página institucional dos pilares do BuscaSmart
│
├── docs/                     # Central de Documentação Executiva e Técnica
│   ├── README.md
│   ├── ENTREGAVEL_GERENTE.md
│   ├── SLIDE_APRESENTACAO.html
│   ├── APRESENTACAO_GERENCIA_SLIDES.md
│   ├── PROPOSTA_COMERCIAL_BUSCASMART.md
│   ├── PLANOS_PRECOS.md
│   ├── GUIA_DO_USUARIO_COMPLETO.md
│   ├── DOCUMENTACAO_TECNICA_COMPLETA.md
│   ├── ROADMAP_PROFISSIONAL.md
│   └── FAQ_CLIENTES.md
│
├── db.sqlite3                # Banco de dados com dados de teste de Picuí - PB
├── manage.py                 # Utilitário de comando Django
└── requirements.txt          # Dependências Python
```

---

## 4. 🗄️ Modelagem de Dados Relacional

### `Operacao` (Missão Principal SAR)
- `nome` (CharField): Identificação da ocorrência.
- `descricao` (TextField): Histórico da vítima e circunstâncias do sumiço.
- `coordenador` (ForeignKey -> User): Oficial ou líder responsável.
- `area_total_km2` (FloatField): Área delimitada calculada via Turf.js.
- `status` (CharField: `PLANEJAMENTO`, `ANDAMENTO`, `CONCLUIDA`, `CANCELADA`).
- `codigo_convite` (CharField, único): Código alfanumérico rápido (ex: `BUSCA-8X92K`).
- `area_delimitada_geojson` (JSONField): Polígono GeoJSON completo da missão.
- `versao` (IntegerField): Controle de versão para sincronização offline.

### `SetorRota` (Quadrante Atribuído)
- `operacao` (ForeignKey -> Operacao): Missão vinculada.
- `identificacao` (CharField): Nome do quadrante (ex: *Setor 01 — Trilha Norte*).
- `responsavel` (ForeignKey -> User, null=True): Voluntário designado.
- `cor_hex` (CharField): Identificador visual de cor no mapa (ex: `#10b981`).
- `geometria_geojson` (JSONField): Polígono recortado do quadrante individual.
- `instrucoes_especificas` (TextField): Diretrizes táticas específicas daquela rota.
- `concluido` (BooleanField): Indicador de varredura finalizada.

### `PontoSinalizacao` (Pontos Críticos e Evidências)
- `operacao` (ForeignKey -> Operacao): Missão vinculada.
- `criado_por` (ForeignKey -> User): Agente que cadastrou o ponto.
- `titulo` (CharField): Identificação do ponto (ex: *Pegada recente*, *Fenda*).
- `tipo` (CharField: `BASE`, `ULTIMO_PONTO`, `EVIDENCIA`, `OBSTACULO`, `OUTRO`).
- `descricao` (TextField): Detalhes periciais.
- `latitude` / `longitude` (FloatField): Coordenadas geográficas WGS84.

---

## 5. 🧮 Motor de Particionamento Territorial (Turf.js)

A divisão automática da área é executada no cliente através de geometria esférica computacional:
1. **Bounding Box Calculation:** O polígono desenhado tem seus limites extremos calculados (`turf.bbox(polygon)`).
2. **Eixo de Maior Extensão:** O algoritmo calcula a largura (Longitudinal) vs altura (Latitudinal). O eixo maior é escolhido para o corte tático.
3. **Fatiamento em Quadrantes:** O polígono mãe é intersectado com faixas proporcionais ao número $N$ de participantes informados pelo coordenador:
   $$\text{Largura da Faixa} = \frac{\text{Extensão Total do Eixo}}{N}$$
4. **Cálculo de Área Individual:** Cada sub-polígono resultante tem sua área calculada em tempo real com `turf.area()` e convertida para hectares e quilômetros quadrados.

---

## 6. 🤖 Motor de Inteligência Artificial Especializada (SAR)

A IA do BuscaSmart foi desenvolvida com arquitetura híbrida:
1. **Briefing Situacional Automatizado (`api_gerar_resumo_ia`):**
   - Agrega o percentual de setores concluídos, calcula a velocidade de avanço em hectares/hora, cruza com o horário do dia para alertar sobre o pôr do sol e emite recomendações táticas prioritárias.
2. **Chatbot Tático Contextual (`api_chat_ia`):**
   - Responde dinamicamente a saudações temporais (*Bom dia*, *Boa tarde*, *Boa noite*).
   - Reconhece intenções SAR: procedimentos para caatinga, cálculo de desidratação, preservação pericial de pegadas, frequências de rádio e suporte à redistribuição de voluntários ausentes.

---

## 7. 📲 Guia de Empacotamento Android Nativo (Capacitor)

Para gerar o arquivo executável APK e o pacote Google Play Store AAB:

```bash
# 1. Instalar dependências Capacitor
npm install @capacitor/core @capacitor/cli @capacitor/android @capacitor/geolocation

# 2. Inicializar o projeto Capacitor
npx cap init BuscaSmart app.buscasmart.sar

# 3. Adicionar a plataforma Android
npx cap add android

# 4. Compilar e sincronizar ativos
npx cap copy
npx cap sync

# 5. Abrir no Android Studio para gerar o APK assinado
npx cap open android
```
No Android Studio: **Build > Generate Signed Bundle / APK > Android App Bundle (.aab)**.
