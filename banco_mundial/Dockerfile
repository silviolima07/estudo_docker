# worldbank_docker_project/Dockerfile

# Usa uma imagem base Python oficial (versão slim para menor tamanho).
FROM python:alpine3.9

# Define o diretório de trabalho dentro do contêiner.
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho.
COPY requirements.txt .

# Instala as dependências Python.
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o restante do código da aplicação para o diretório de trabalho.
COPY . .

# Comando para executar a aplicação quando o contêiner for iniciado.
CMD ["python", "app.py"]