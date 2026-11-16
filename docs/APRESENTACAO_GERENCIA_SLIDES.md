# 🎤 Roteiro de Apresentação Executiva — BuscaSmart SAR
## Estrutura de Slides com Notas de Discurso (Speech Notes)

Este roteiro foi elaborado para guiar a apresentação do **Marcos Paulo** ou de qualquer membro da equipe diante da Gerência, Diretoria, Clientes, Comandantes de Bombeiros ou Secretários Municipais.

> 💡 **Dica Prática:** Você pode abrir o arquivo interativo [`SLIDE_APRESENTACAO.html`](./SLIDE_APRESENTACAO.html) no navegador para projetar os slides visuais enquanto consulta este roteiro.

---

### Slide 1: Capa & Identidade
- **Título:** BuscaSmart — Sistema de Gestão Inteligente de Buscas e Salvamento (SAR)
- **Subtítulo:** Plataforma Tática para Delimitação de Áreas, Divisão Automática de Setores e Coordenação de Resgate em Campo (Online e Offline)
- **Notas de Discurso (O que falar):**
  > *"Bom dia / Boa tarde a todos. Hoje apresentamos o BuscaSmart, uma plataforma desenvolvida para resolver uma dor crítica da segurança pública e do voluntariado de resgate: como transformar operações de busca em áreas rurais e matas em processos organizados, rápidos, orientados por dados e capazes de operar mesmo onde não existe sinal de celular."*

---

### Slide 2: O Problema Real
- **Título:** Como as buscas são feitas hoje: o gargalo do papel e do improviso
- **Pontos-Chave:**
  - Mapas de papel com croquis manuais imprecisos.
  - Comunicação caótica via WhatsApp que dispersa a atenção.
  - Sobreposição de equipes: resgatistas andando no mesmo lugar enquanto outros setores ficam vazios.
  - Perda da "Janela Crítica de Sobrevivência" (24 a 48h).
- **Notas de Discurso (O que falar):**
  > *"Hoje, quando alguém desaparece em uma zona rural, o coordenador precisa pegar um mapa em papel ou mandar fotos no WhatsApp. Metade dos voluntários anda no mesmo lugar e áreas inteiras ficam sem vasculhar. No resgate, tempo é vida: as primeiras 24 horas determinam se a pessoa será encontrada com vida ou não. O BuscaSmart elimina esse improviso em minutos."*

---

### Slide 3: O Caso Prático de Picuí - PB
- **Título:** Cenário Piloto: 10 km² e 20 Voluntários
- **Pontos-Chave:**
  - Idoso desaparecido na caatinga em relevo rochoso.
  - Coordenador abre o BuscaSmart no computador ou tablet.
  - Clica 4 pontos no satélite e fecha a área da ocorrência.
  - O sistema calcula 1.000 hectares instantaneamente via Turf.js.
  - Informa 20 voluntários: o sistema fatia o terreno em 20 setores balanceados (*Setor 01 — Júnior*, *Setor 02 — Marcos Paulo*, etc.).
- **Notas de Discurso (O que falar):**
  > *"Nós modelamos o sistema pensando na realidade do semiárido e do interior brasileiro, como em Picuí na Paraíba. Uma área de 10 km² na caatinga com 20 voluntários. Em vez de gastar duas horas desenhando à mão, o coordenador abre o BuscaSmart, marca o polígono e o algoritmo divide os 20 setores em 3 segundos, já com o nome de cada responsável."*

---

### Slide 4: Os 8 Módulos Funcionais
- **Título:** Uma Solução Completa de Ponta a Ponta
- **Módulos:**
  1. **Mapa Inteligente:** Satélite de alta precisão e delimitação poligonal.
  2. **Divisão Automática:** Algoritmo matemático geoespacial de partição.
  3. **Rotas Manuais:** Desenho livre de trilhas e acessos vicinais.
  4. **Rotas Automáticas:** Varreduras em zigue-zague e patrulhamento de borda.
  5. **Inteligência Artificial:** Resumo tático situacional e chatbot de apoio SAR.
  6. **Identificação & Efetivo:** Controle nominal de quem está em cada setor.
  7. **Compartilhamento Ágil:** Código alfanumérico rápido e QR Code para celular.
  8. **Modo Offline & GPS:** Telemetria por satélite sem necessidade de internet.
- **Notas de Discurso (O que falar):**
  > *"O software foi planejado em 8 módulos integrados. Cada módulo atende a uma etapa da operação: do planejamento cartográfico até a ida do voluntário para a mata com o GPS ligado no celular."*

---

### Slide 5: Modo Offline & Resiliência em Campo
- **Título:** Funcionando Onde Não Há Sinal de Celular
- **Pontos-Chave:**
  - O GPS do aparelho celular conecta aos satélites da órbita terrestre, sem precisar de 4G/5G.
  - Download prévio dos setores e mapa no Posto de Comando antes de entrar na mata.
  - Registro de evidências (pegadas, peças de roupa) georreferenciadas na memória local.
  - Sincronização automática assim que houver conexão.
- **Notas de Discurso (O que falar):**
  > *"Uma das principais dúvidas de clientes e comandantes é: 'Mas na mata não pega internet, como funciona?'. Explicamos que o chip de GPS do celular se comunica diretamente com satélites no espaço, independente de chip de operadora. O voluntário baixa a missão na base com 1 clique e caminha com o pontinho azul na tela dentro da rota atribuída a ele."*

---

### Slide 6: Inteligência Artificial Especializada
- **Título:** Apoio Tático à Tomada de Decisão do Comandante
- **Pontos-Chave:**
  - Resumo de briefing executivo em tempo real no Dashboard.
  - Análise preditiva de atrasos e riscos de relevo (fendas, riachos secos).
  - Chatbot tático contextual que orienta protocolos de caatinga e preservação de vestígios.
- **Notas de Discurso (O que falar):**
  > *"A nossa Inteligência Artificial não substitui a decisão humana do coordenador, ela atua como um assistente tático de Estado-Maior: ela avisa se um setor está atrasado, lembra das frentes prioritárias antes do anoitecer e fornece respostas rápidas sobre procedimentos SAR."*

---

### Slide 7: Demonstração da Plataforma ao Vivo
- **Título:** Tour Completo pelas Telas do Sistema
- **Ações:**
  - Abrir `http://127.0.0.1:8080/` no navegador.
  - Mostrar a Página Inicial com o cenário de Picuí.
  - Fazer login com `marcos` / `marcos123`.
  - Navegar pelo Dashboard com o Card da IA.
  - Abrir o Mapa e demonstrar a divisão dos setores.
  - Mostrar a tela de Minha Rota com o GPS telemétrico.
  - Exibir o Relatório Oficial de Missão SAR pronto para impressão.
- **Notas de Discurso (O que falar):**
  > *"Não estamos apresentando apenas uma ideia ou um slide bonito. O sistema já está 100% desenvolvido, com banco de dados real, mapa interativo e telas prontas para teste prático."*

---

### Slide 8: Modelo Comercial & Monetização
- **Título:** Potencial de Negócio e Sustentabilidade Financeira
- **Modelos:**
  - **SaaS para Órgãos Públicos:** Licenciamento anual para Prefeituras e Corpos de Bombeiros.
  - **Plano Profissional:** ONGs de busca, equipes de resgate K9 (cães), brigadas florestais e mineradoras.
  - **Plano Comunitário:** Gratuito para voluntários civis que ingressam em operações ativas.
- **Notas de Discurso (O que falar):**
  > *"O BuscaSmart tem alto valor comercial. Prefeituras e secretarias de segurança investem milhões em viaturas e combustível, mas não têm um software de coordenação de busca. O custo de uma licença anual do BuscaSmart se paga na economia de horas de helicóptero e no resgate mais rápido das vítimas."*

---

### Slide 9: Próximos Passos & Publicação na Play Store
- **Título:** Roadmap Tecnológico
- **Fases:**
  1. **MVP Atual:** Web responsiva, Leaflet, Turf.js e Django testados.
  2. **Empacotamento com Capacitor:** Geração do APK Android com acesso nativo aos sensores e disco.
  3. **Publicação Google Play:** Submissão formal com pacote .AAB nas diretrizes da Play Store.
- **Notas de Discurso (O que falar):**
  > *"Nossa arquitetura foi construída de forma modular. Com a base web validada, o próximo passo imediato é empacotar a aplicação via Capacitor para gerar o APK Android instalável e disponibilizá-lo na Google Play Store para download oficial."*

---

### Slide 10: Encerramento & Convite ao Teste
- **Título:** Conclusão e Teste Prático
- **Notas de Discurso (O que falar):**
  > *"Agradeço a atenção de todos. Convido agora o gerente e a equipe para testarmos juntos a ferramenta e colocarmos à prova qualquer cenário de resgate. Estamos prontos para responder perguntas."*
