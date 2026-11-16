# 📋 Dossiê Executivo do Projeto BuscaSmart
## Sistema de Gestão Inteligente de Buscas e Salvamento Territorial (SAR)

**Data de Emissão:** Novembro de 2026  
**Status do Projeto:** MVP 1.0 Totalmente Funcional, Testado e Pronto para Demonstração  
**Responsável Técnico / Coordenação:** Marcos Paulo Santos Lira  
**Ambiente de Demonstração Local:** `http://127.0.0.1:8080/`

---

## 1. 🎯 Resumo Executivo

O **BuscaSmart** é uma plataforma tecnológica de nível profissional projetada para modernizar, acelerar e profissionalizar operações de **Busca e Salvamento (SAR — Search and Rescue)**, Defesa Civil e forças voluntárias em áreas rurais, de mata e terreno acidentado.

Tradicionalmente, operações de busca em municípios do interior dependem de mapas impressos em papel, instruções verbais imprecisas e comunicação fragmentada por WhatsApp, gerando sobreposição de esforços, áreas esquecidas e perda do precioso tempo da "Janela de Sobrevivência" (as primeiras 24 a 48 horas).

O **BuscaSmart** resolve esse gargalo através de uma solução digital que permite:
1. **Delimitar a área de busca** sobre satélite de alta resolução com cálculo automático de extensão territorial (km² e hectares).
2. **Dividir o terreno instantaneamente em setores balanceados** de acordo com a quantidade de resgatistas disponíveis utilizando algoritmos geoespaciais (`Turf.js`).
3. **Atribuir nominalmente cada rota** ao voluntário ou equipe correspondente.
4. **Distribuir as rotas aos celulares dos voluntários** via código de convite rápido ou QR Code.
5. **Acompanhar o voluntário em campo via GPS telemétrico**, mesmo em locais **sem sinal de internet**.
6. **Registrar pontos críticos, evidências e obstáculos** georreferenciados.
7. **Emitir Relatórios Oficiais de Missão SAR** prontos para impressão e arquivamento pericial.
8. **Assistência de Inteligência Artificial Especializada** para briefing tático e suporte operacional ao coordenador.

---

## 2. 🌵 O Cenário Real de Aplicação: Região de Picuí - PB

O sistema foi modelado a partir de demandas operacionais concretas do semiárido e zonas rurais brasileiras:

> **Cenário de Teste Operacional:**  
> Uma pessoa idosa ou turista se perde em uma região de caatinga e relevo rochoso no município de **Picuí - PB**, abrangendo uma área de aproximadamente **10 km²**.  
> O coordenador do resgate abre o **BuscaSmart**, delimita o polígono da ocorrência no mapa de satélite e informa a presença de **20 voluntários**.  
> Em menos de **5 segundos**, o sistema calcula o perímetro, particiona a área em 20 setores etiquetados (*Setor 01 — Júnior*, *Setor 02 — Marcos Paulo*, etc.) e disponibiliza as rotas para sincronização nos aparelhos dos voluntários.

---

## 3. 🧩 Os 8 Módulos Implementados

| Nº | Módulo | Funcionalidade Principal | Tecnologia Utilizada |
| :---: | :--- | :--- | :--- |
| **01** | **Mapa Inteligente** | Seleção, pesquisa e delimitação de polígonos sobre camadas de satélite Esri e OpenStreetMap com cálculo em tempo real de hectares e km². | Leaflet, Esri World Imagery, Turf.js |
| **02** | **Divisão Automática** | Particionamento matemático e territorial do polígono em quadrantes equivalentes para qualquer número de voluntários. | Turf.js Bounding Box & Grid Slicing |
| **03** | **Rotas Manuais** | Desenho livre e edição de trajetos táticos e trilhas de acesso no mapa. | Leaflet Draw API |
| **04** | **Rotas Automáticas** | Traçado automatizado de varreduras em zigue-zague e patrulhamento de borda. | Algoritmos Geoespaciais |
| **05** | **Inteligência Artificial SAR** | Briefing tático situacional em tempo real no dashboard e chatbot conversacional de apoio à tomada de decisão operacional. | Engine Heurística SAR + LLM Ready API |
| **06** | **Identificação & Efetivo** | Gestão nominal de equipes, distribuição de setores por resgatista e controle de status de conclusão (concluído/pendente). | Django ORM + Auth System |
| **07** | **Compartilhamento Ágil** | Distribuição instantânea de missões por código alfanumérico (`BUSCA-XXXXXX`) e QR Code dinâmico escaneável pela câmera do celular. | QR Server API + URL Deep Linking |
| **08** | **Modo Offline & GPS de Campo** | Visualização de mapas cacheados, telemetria contínua por satélite GNSS/GPS do celular e registro de evidências sem conexão. | HTML5 Geolocation + LocalStorage Cache |

---

## 4. 🖥️ Catálogo Completo de Telas do Sistema

Todas as telas foram desenhadas seguindo a identidade visual **Tactical Dark** (fundo escuro de alto contraste para operações noturnas e de campo, com paleta verde esmeralda, ciano e âmbar):

1. **`Página Inicial Comercial (/`):** Apresentação institucional de alto impacto para clientes e autoridades, apresentando o caso de uso de Picuí, os 8 módulos, galeria de fotos de operações SAR e métricas de eficiência.
2. **`Autenticação e Login (/login/`):** Tela tática com proteção por senha, botão de visualização e preenchimento rápido para demonstração.
3. **`Cadastro de Voluntários (/cadastro/`):** Formulário para novos voluntários e coordenadores se registrarem e acessarem o sistema.
4. **`Dashboard do Coordenador (/dashboard/`):** Visão geral de missões ativas, KPIs operacionais (hectares varridos, resgatistas mobilizados), barra de eficiência e card dinâmico de **Resumo Tático com Inteligência Artificial**.
5. **`Painel do Mapa & Satélite (/mapa/`):** Interface principal de comando cartográfico com desenho poligonal, divisão automática por número de participantes, medição métrica e botão de salvamento no banco de dados.
6. **`Gestão de Equipes & Setores (/equipe/`):** Listagem de todos os voluntários cadastrados, atribuição nominal de setores, alternadores de status em tempo real e emissor de QR Code de acesso.
7. **`Minha Rota — Mobile Voluntário (/rota/`):** Interface otimizada para smartphones com telemetria GPS, bússola de rumo, alternador de Modo Offline, botão de pânico VHF e registro de evidências.
8. **`Dossiê da Operação (/detalhes/<id>/`):** Relatório detalhado com mini-mapa interativo, log de evidências com coordenadas e dados da vítima.
9. **`Relatório Oficial de Impressão (/relatorio/<id>/`):** Documento formal A4 pronto para geração de PDF com campos de assinatura do Coordenador de Operações e Delegado/Comandante.
10. **`Chatbot de Inteligência Artificial SAR (/ia/chat/`):** Painel de conversa tática para tirar dúvidas de busca, cálculo de janelas de sobrevivência, protocolos de caatinga e coordenação.
11. **`Página Institucional Sobre (/sobre/`):** Apresentação dos pilares do BuscaSmart (Organização, Visibilidade e Gestão) com QR Code institucional.
12. **`Painel Administrativo Django (/admin/`):** Gestão corporativa de usuários, permissões, setores e pontos de sinalização.

---

## 5. 👥 Usuários e Credenciais do Sistema de Demonstração

Para fins de teste e apresentação, o sistema conta com perfis pré-configurados:

| Usuário | Senha | Nome Completo | Perfil |
| :--- | :--- | :--- | :--- |
| **`marcos`** | **`marcos123`** | Marcos Paulo Santos Lira | Coordenador SAR (Superusuário) |
| **`admin`** | **`admin123`** | Administrador do Sistema | Gestor Geral |
| **`junior`** | `voluntario123` | Júnior Silva | Voluntário de Campo |
| **`pedro`** | `voluntario123` | Pedro Alcantara | Voluntário de Campo |
| **`joao`** | `voluntario123` | João Victor | Voluntário de Campo |
| **`carlos`** | `voluntario123` | Carlos Eduardo | Voluntário de Campo |
| **`maria`** | `voluntario123` | Maria Helena | Socorrista de Resgate |

---

## 6. 📱 Estratégia de Transformação em Aplicativo Android (Play Store)

O projeto foi concebido sob a arquitetura **Mobile-First Responsive Web + PWA**, permitindo uma transição direta para aplicativo nativo Android através de **Capacitor (Ionic)**:

1. **Camada Web:** Django + Tailwind CSS + Leaflet (já 100% desenvolvida e responsiva).
2. **Camada Nativa (Capacitor):** Empacota a interface em um webview otimizado de altíssimo desempenho, integrando diretamente os plugins de GPS nativo (`@capacitor/geolocation`), sistema de arquivos offline (`@capacitor/filesystem`) e notificações push.
3. **Publicação:** Geração de arquivo `.aab` (Android App Bundle) assinado conforme as diretrizes atuais da Google Play Store (Target SDK 34/35).

---

## 7. 💡 Parecer de Prontidão

O software encontra-se em estado **completamente operacional**, com servidor rodando localmente na porta `8080`, banco de dados populado com missões de exemplo representativas e documentação estruturada.

Recomenda-se a utilização do arquivo [`SLIDE_APRESENTACAO.html`](./SLIDE_APRESENTACAO.html) para conduzir a reunião executiva com o gerente, seguida de uma demonstração prática no navegador em `http://127.0.0.1:8080/`.
