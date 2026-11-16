# Documentação Técnica e Deploy em VPS

## Arquitetura atual

- Aplicação web Django servida por Gunicorn.
- SQLite armazenado em volume Docker.
- WhiteNoise serve os arquivos estáticos coletados do Django.
- Interface HTML com Leaflet, Turf.js e Tailwind CSS carregados de CDNs.

O protótipo ainda não possui uma API funcional para salvar operações, nem autenticação/compartilhamento, mapas offline ou otimização de rotas. SQLite e a configuração Compose fornecida são adequados para avaliação inicial, não para operação de busca crítica ou carga concorrente.

## Executar localmente

Na pasta que contém `manage.py`:

```bash
docker compose up --build
```

A aplicação fica disponível em `http://localhost:8000/mapa/`. As migrações e a coleta de estáticos são executadas na inicialização. O Compose mantém o banco no volume `buscasmart_data`.

Para build e execução sem Compose:

```bash
docker build -t buscasmart .
docker run --rm -p 8000:8000 buscasmart
```

O comando `docker run` não configura volume persistente; os dados podem ser perdidos ao remover o container. Para preservar o banco, use Compose.

## Variáveis de ambiente

Copie `.env.example` para `.env` para configurar os valores usados pelo Compose. Não versionar `.env` nem publicar credenciais.

| Variável | Uso |
| --- | --- |
| `DJANGO_SECRET_KEY` | Chave secreta; gere uma exclusiva para cada ambiente. |
| `DJANGO_DEBUG` | `True` no teste local; use `False` em produção. |
| `ALLOWED_HOSTS` | Hosts permitidos separados por vírgula. |
| `CSRF_TRUSTED_ORIGINS` | Origens HTTPS confiáveis separadas por vírgula, por exemplo `https://busca.exemplo.com`. |
| `PORT` | Porta publicada no host (padrão `8000`). |
| `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS` | Configuração SMTP opcional. Sem `EMAIL_HOST`, Django usa o backend de console. |
| `DEFAULT_FROM_EMAIL` | Remetente padrão opcional. |
| `ADMIN_EMAIL` | Endereço de administrador usado pela configuração Django. |

O caminho do SQLite dentro do Compose é `/data/db.sqlite3`; o volume `buscasmart_data` persiste os dados.

Gere uma chave forte localmente, sem colocá-la no repositório:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

## Deploy em VPS (base para avaliação)

1. Use uma VPS atualizada com Docker Engine e Docker Compose.
2. Clone o repositório e crie `.env` a partir de `.env.example`.
3. Configure `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, `ALLOWED_HOSTS` com o domínio e `CSRF_TRUSTED_ORIGINS` com a origem HTTPS.
4. Restrinja as portas de entrada da VPS ao necessário e configure um proxy reverso HTTPS (por exemplo, Caddy ou Nginx) na frente da aplicação.
5. Inicie com `docker compose up --build -d` e valide os logs com `docker compose logs -f web`.
6. Faça backup e teste a restauração do volume `buscasmart_data`.

O Compose deste repositório não configura domínio, TLS, firewall, backups automáticos, monitoramento ou uma base PostgreSQL. Para operação pública ou institucional, planeje esses itens, política de privacidade, controle de acesso e recuperação de desastres antes de armazenar dados pessoais ou dados de uma ocorrência real. Não exponha o serviço publicamente sem uma revisão de segurança e operação.

## Verificações

```bash
docker compose config
docker compose up --build
docker compose logs -f web
```

O serviço é iniciado pelo Gunicorn; não use `runserver` como servidor de produção.
