# Imagem base pequena com Python 3.12
FROM python:3.12-alpine

# Pasta de trabalho dentro do container
WORKDIR /app

# Copia o código para dentro da imagem
COPY app.py .

# Porta que o app escuta (documentação; o mapeamento real é feito no docker run/compose)
EXPOSE 8000

# Comando executado quando o container inicia
CMD ["python", "app.py"]
