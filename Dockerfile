FROM redis:6.2.3-alpine

# Copia o arquivo push.py para dentro do contêiner
COPY push.py /opt/push.py

# Instala as bibliotecas Python necessárias
RUN apk add --no-cache python3

# Configura o script de inicialização padrão com a execução do push.py
CMD ["sh", "-c", "redis-server --appendonly yes & python3 /opt/push.py"]
