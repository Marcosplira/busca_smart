# Guia do Usuário — BuscaSmart

## Situação do sistema

Este é um protótipo web. Ele ajuda a visualizar um perímetro e a dividi-lo em setores geométricos; não é um sistema operacional certificado para coordenar buscas reais. Confirme o planejamento com a coordenação responsável e com os protocolos oficiais.

## Iniciar o sistema

1. Instale e inicie o Docker Desktop.
2. No terminal, abra a pasta do projeto.
3. Execute `docker compose up --build`.
4. No navegador, acesse http://localhost:8000/mapa/.
5. Para encerrar, pressione `Ctrl+C` no terminal.

## Delimitar e dividir uma área

1. Informe o nome da operação.
2. Use a ferramenta de polígono ou retângulo no mapa e marque o perímetro.
3. Confira a área aproximada exibida no topo.
4. Informe a quantidade de participantes (de 1 a 50).
5. Clique em **Dividir Setores Automaticamente**.
6. Clique em um setor no mapa para conferir sua identificação.

O botão limpa setores gerados anteriormente, mas mantém os desenhos do mapa. A divisão atual utiliza faixas verticais dentro dos limites do polígono; isso pode produzir setores de tamanhos diferentes ou menos setores que participantes em perímetros irregulares. Revise a cobertura manualmente.

## Limitações conhecidas

- O mapa de base e bibliotecas externas dependem de internet; não há mapas baixáveis nem operação offline.
- Os setores gerados são uma divisão geométrica, não uma rota caminhável, otimizada ou verificada contra terreno, rios, cercas e riscos.
- A atribuição de pessoas a setores, criação de rotas manuais, compartilhamento e sincronização não estão implementados.
- O botão **Salvar Área** ainda depende de uma API que não está implementada.
- O chatbot/IA está descrito como proposta, mas não integra o protótipo atual.

Não use este protótipo como única fonte de orientação em uma busca real.
