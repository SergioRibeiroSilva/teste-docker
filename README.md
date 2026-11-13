# Demo Docker

Projeto mínimo para entender containers: um servidor HTTP em Python que mostra o hostname do container.

## Arquivos

- `app.py` – servidor HTTP (só biblioteca padrão, sem dependências)
- `Dockerfile` – receita para construir a imagem
- `docker-compose.yml` – sobe o container com porta e variáveis já configuradas

## Como rodar

Na pasta do projeto:

```bash
# Constrói a imagem e sobe o container em segundo plano
docker compose up -d --build
```

Abra http://localhost:8080 no navegador.

## Comandos úteis para explorar

```bash
docker ps                      # containers em execução
docker images                  # imagens locais
docker logs -f demo-web       # logs ao vivo (Ctrl+C para sair)
docker exec -it demo-web sh   # abre um shell dentro do container (digite exit para sair)
docker stats demo-web          # uso de CPU e memória
docker stop demo-web           # para o container
docker start demo-web          # inicia de novo
docker compose down            # para e remove o container
```

## Experimentos sugeridos

1. Recarregue a página: o horário muda, mas o hostname continua o mesmo.
2. Rode `docker compose down` e depois `docker compose up -d`: o hostname muda, pois é um container novo.
3. Altere `MESSAGE` no `docker-compose.yml` e rode `docker compose up -d` de novo para ver a variável de ambiente em ação.
4. Altere o texto em `app.py`, rode `docker compose up -d --build` e veja a imagem sendo reconstruída.
5. Rode `docker run --rm -p 9000:8000 demo-docker-web` para subir outra instância sem compose.
