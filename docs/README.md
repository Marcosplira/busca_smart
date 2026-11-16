# 📚 Central de Documentação Executiva e Técnica — BuscaSmart

Bem-vindo à central oficial de documentação do **BuscaSmart** (*Sistema de Gestão Inteligente de Buscas e Salvamento Territorial - SAR*).

Esta pasta foi estruturada especialmente para apresentação à **Gerência, Clientes, Comandos de Bombeiros, Defesa Civil e Secretarias de Segurança Pública**, reunindo tanto a visão de negócios e impacto operacional quanto os detalhes técnicos de implementação e uso.

---

## 🗂️ Mapa dos Documentos Disponíveis

| Documento | Público-Alvo | O que contém |
| :--- | :--- | :--- |
| **[`SLIDE_APRESENTACAO.html`](./SLIDE_APRESENTACAO.html)** | 🎯 **Gerente / Diretoria / Clientes** | **Apresentação visual interativa em slides**. Pode ser aberta em qualquer navegador (Chrome, Edge) para apresentação ao vivo com teclado/mouse. |
| **[`ENTREGAVEL_GERENTE.md`](./ENTREGAVEL_GERENTE.md)** | 👔 **Gerente / Coordenador Geral** | **Dossiê Executivo Completo**. Visão estratégica, dor de mercado, cenário rural de Picuí, 8 módulos implementados e impacto real. |
| **[`APRESENTACAO_GERENCIA_SLIDES.md`](./APRESENTACAO_GERENCIA_SLIDES.md)** | 🎤 **Apresentador / Equipe** | Roteiro estruturado de slides com notas de discurso (*speech notes*) para reuniões executivas e demonstrações. |
| **[`PROPOSTA_COMERCIAL_BUSCASMART.md`](./PROPOSTA_COMERCIAL_BUSCASMART.md)** | 💼 **Comercial / Compras / Licitações** | Modelo de negócio SaaS, venda institucional para Prefeituras e Corpos de Bombeiros, ROI e diferenciais de mercado. |
| **[`PLANOS_PRECOS.md`](./PLANOS_PRECOS.md)** | 🏷️ **Clientes / Financeiro** | Tabela detalhada de planos de assinatura (*Básico Voluntário*, *Profissional SAR*, *Institucional Governo*). |
| **[`GUIA_DO_USUARIO_COMPLETO.md`](./GUIA_DO_USUARIO_COMPLETO.md)** | 🧭 **Coordenadores e Voluntários** | Manual passo a passo de operação: desde o login, desenho do polígono no satélite, divisão por Turf.js até GPS mobile e relatório PDF. |
| **[`DOCUMENTACAO_TECNICA_COMPLETA.md`](./DOCUMENTACAO_TECNICA_COMPLETA.md)** | 💻 **Desenvolvedores / TI** | Arquitetura técnica detalhada (Django 5, Leaflet, Turf.js, GPS Geolocation API, SQLite/PostGIS, empacotamento Capacitor Android). |
| **[`ROADMAP_PROFISSIONAL.md`](./ROADMAP_PROFISSIONAL.md)** | 🚀 **Gerência de Produto / Devs** | Cronograma de evolução: do MVP atual até a publicação na Google Play Store, suporte a mapas vetoriais offline e rádio LoRa. |
| **[`FAQ_CLIENTES.md`](./FAQ_CLIENTES.md)** | ❓ **Clientes / Voluntários** | Perguntas frequentes sobre funcionamento sem internet, autonomia de bateria, precisão do GPS e segurança de dados (LGPD). |

---

## 🚀 Como Iniciar a Apresentação para o Gerente

1. **Demonstração Visual (Slides):**
   - Dê um duplo clique no arquivo [`SLIDE_APRESENTACAO.html`](./SLIDE_APRESENTACAO.html) para abrir no navegador. Use as teclas `←` e `→` ou os botões para navegar.
2. **Demonstração do Sistema ao Vivo:**
   - Acesse **`http://127.0.0.1:8080/`** no navegador.
   - Navegue pela Página Inicial Comercial, faça login com `marcos` / `marcos123`, mostre o Dashboard com Briefing de IA, desenhe um setor no Mapa de Satélite, mostre a Gestão de Equipe e a tela Mobile do Voluntário (`/rota/`).
3. **Entrega de Relatórios:**
   - Mostre o Relatório Oficial de Missão SAR pronto para impressão/PDF (`/relatorio/1/`).
