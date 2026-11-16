# 📖 Guia do Usuário Completo — BuscaSmart
## Manual Prático de Operação para Coordenadores e Voluntários de Campo

---

## 🧭 1. Primeiros Passos e Acesso ao Sistema

### Como Acessar:
1. Abra o navegador web no computador, tablet ou celular.
2. Acesse o endereço do sistema (ex: `http://127.0.0.1:8080/` ou o domínio oficial do município).
3. Na tela de login:
   - Se você for o Coordenador: insira seu usuário (`marcos`) e senha (`marcos123`).
   - Se for um novo voluntário: clique no link **"Cadastre-se para participar de buscas"** em `/cadastro/`.

---

## 👨‍✈️ 2. Guia do Coordenador de Operações

### Passo 2.1: Criando uma Nova Missão
1. No menu superior, clique em **"Nova Operação"** ou vá direto para `/mapa/`.
2. No painel de controle lateral:
   - Digite o **Nome da Operação** (ex: *Varredura Serra dos Brandões — Picuí*).
   - Insira a descrição sumária da vítima (ex: *Homem, 68 anos, trajes escuros, desaparecido há 18h*).

### Passo 2.2: Delimitando a Região no Mapa de Satélite
1. Localize a região no mapa arrastando ou usando a ferramenta de zoom.
2. Clique na ferramenta de desenho poligonal na barra lateral do mapa (ícone de pentágono).
3. Clique sobre o mapa para marcar os vértices (cantos) da área de busca.
4. Dê um clique duplo para fechar o polígono.
5. O sistema exibirá instantaneamente a **Área Total em Hectares e Km²** e o **Perímetro em Metros**.

### Passo 2.3: Dividindo os Setores Automaticamente
1. No campo **"Número de Participantes / Equipes"**, informe a quantidade de voluntários disponíveis (ex: `20`).
2. Clique no botão **"Dividir Área Automaticamente"**.
3. O algoritmo particiona o território em 20 quadrantes coloridos, cada um identificado por um código (Setor 01, Setor 02, etc.).
4. Clique em **"Salvar Operação e Setores no Banco"**.

### Passo 2.4: Gerenciando a Equipe e Atribuindo Setores
1. Acesse o menu **"Equipe"** (`/equipe/`).
2. O sistema exibe o **Código de Convite** (ex: `BUSCA-PICUI1`) e o **QR Code**.
3. Para cada setor gerado:
   - Selecione o nome do voluntário responsável no menu suspenso.
   - Conforme o voluntário reportar que completou a rota, ative a chave **"Concluído"**.
4. No painel lateral, consulte a lista de todos os voluntários cadastrados e o canal de rádio VHF designado.

### Passo 2.5: Acompanhando o Dashboard com IA
1. Acesse o **"Dashboard"** (`/dashboard/`).
2. Observe o card **"Resumo Tático com Inteligência Artificial"**: ele analisa os setores concluídos, calcula a eficiência da busca e emite alertas sobre escuridão iminente e setores atrasados.

### Passo 2.6: Emitindo o Relatório Oficial de Missão SAR
1. Acesse **"Detalhes da Missão"** (`/detalhes/<id>/`).
2. Clique em **"Gerar Relatório Oficial (PDF)"** para abrir `/relatorio/<id>/`.
3. O documento carrega a folha de missão formatada para papel A4, com histórico de setores, coordenadas de evidências e campos para assinatura da Coordenação e do Comandante de Operações.
4. Pressione `Ctrl + P` para imprimir ou salvar como PDF.

---

## 🏃 3. Guia do Voluntário em Campo (Celular)

### Passo 3.1: Acessando a Sua Rota
1. Pelo celular, escaneie o QR Code fornecido pelo coordenador ou acesse `/rota/<id_setor>/`.
2. A tela **"Minha Rota — Modo Voluntário"** será aberta com foco exclusivo no seu setor.

### Passo 3.2: Ativando o Modo Offline
1. Antes de se afastar do Posto de Comando (onde ainda há Wi-Fi ou sinal de celular), clique no botão **"Baixar Mapa e Setores (Modo Offline)"**.
2. O sistema armazena a geometria da sua rota, as instruções e os pontos de sinalização na memória do aparelho.
3. Ative a chave **"Modo Offline"**: a interface confirma que você está operando de forma 100% autônoma.

### Passo 3.3: Navegando com o GPS de Satélite
1. O círculo azul pulsante no mapa indica a sua posição exata em tempo real.
2. A barra superior informa:
   - Sua latitude e longitude atuais.
   - A precisão do sinal de satélite (ex: *Precisão: ± 4 metros*).
   - O rumo estimado em graus (°).
3. Caminhe cobrindo toda a faixa do seu setor designado (em zigue-zague ou varredura linear conforme orientado).

### Passo 3.4: Registrando um Vestígio ou Evidência
1. Caso encontre um calçado, pegada, peça de roupa ou obstáculo perigoso:
2. Clique no botão **"Registrar Ponto / Evidência"**.
3. Selecione o tipo (*Evidência*, *Obstáculo*, *Área Inacessível*).
4. Insira uma breve descrição (ex: *Marca de sola tamanho 40 no barro seco, sentido riacho*).
5. O sistema captura a coordenada GPS instantânea daquele local e grava no histórico da missão.

### Passo 3.5: Comunicação e Emergência
1. Caso sofra uma torção, encontre um obstáculo intransponível ou localize a vítima:
2. Toque no botão **"Emergência / Contato ICP"**.
3. O sistema exibe na tela o canal de rádio VHF principal da base (ex: *VHF 148.500 MHz*) e a coordenada atual para você ditar ao rádio.

---

## 🌲 4. Protocolo de Segurança em Terreno Rural e Caatinga

1. **Regra dos Pares:** Nunca avance sozinho na vegetação; forme duplas ou trios para cada setor.
2. **Hidratação:** No semiárido, consuma pelo menos 500 ml de água por hora de caminhada sob sol forte.
3. **Preservação:** Não toque em vestígios suspeitos para não alterar a cena ou espalhar odores que possam atrapalhar cães de busca (K9).
