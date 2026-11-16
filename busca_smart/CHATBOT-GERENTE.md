# Chatbot Gerente e Assistente Tático — BuscaSmart IA

## ✅ Status Atual da Implementação

Implementado com sucesso no projeto BuscaSmart! O sistema agora conta com **dois pontos de inteligência artificial operacional**:

1. **Resumo Executivo com IA no Dashboard** (`/api/ia/resumo/`):
   - Integrado ao painel do coordenador (`dashboard.html`).
   - Analisa em tempo real as operações ativas, quantidade de setores concluídos vs pendentes, pontos críticos de evidência cadastrados e sugere ações prioritárias de varredura.
   - Ativado pelo botão *"Gerar resumo"* no card de IA do Dashboard.

2. **Assistente de Chat com IA Dedicado** (`/ia/chat/`):
   - Tela exclusiva inspirada no assistente operacional corporativo (`chat_ia.html`).
   - Responde instantaneamente a saudações amigáveis (ex: *"Bom dia!"*).
   - Consulta o banco de dados em tempo real para informar status das missões, áreas em hectares e rotas.
   - Fornece orientações especializadas em diretrizes internacionais SAR (Search and Rescue) e IAMSAR.
   - Possui atalhos com botões rápidos (Quick Reply Chips) para 1 clique.

---

## 🎯 Capacidades Operacionais da IA

- **Análise Geográfica:** Resumo de área em hectares e km² delimitada no mapa com Turf.js.
- **Rastreabilidade de Evidências:** Alertas sobre LKP (Último Ponto Visto) e vestígios catalogados.
- **Alocação de Forças:** Recomendações de segurança para voluntários e divisão em duplas com comunicação rádio VHF.
- **Protocolo de Continuidade:** Sugestões para encerramento de varredura antes do pôr do sol ou apoio médico.

---

## 🔒 Diretrizes de Segurança Operacional

- A IA atua como **suporte à decisão tática** do Coordenador Geral; a autoridade final sobre o início, suspensão ou encerramento de missões permanece com o comando humano e órgãos competentes (Bombeiros e Defesa Civil).
- Os dados do banco SQLite local são processados de forma segura, garantindo confidencialidade e rastreabilidade total.
