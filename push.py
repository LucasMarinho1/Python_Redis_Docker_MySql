import redis
import mysql.connector
import time



while True:
     
    # Conexão Redis
    redis_host = 'localhost'
    redis_port = 6379
    redis_db = 0

    r = redis.Redis(
        host="127.0.0.1", 
        port=6379, 
        password="Redis2019!",
        charset="utf-8")

    # Conexão MySQL
    mysql_host = '127.0.0.1'
    mysql_user = 'root'
    mysql_password = 'root'
    mysql_database = 'DB_ACESSO'

    conn = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database
    )
    cursor = conn.cursor()

    # Copiar os dados do Redis e inserir no MySQL
    keys = r.keys("user:*")  # Obtém todas as chaves do Redis

    for key in keys:
        name = r.hget(key, "name")
        email = r.hget(key, "email")
        print(key, name.decode('utf-8'), email.decode('utf-8'))

        query1 = "SELECT nome, email FROM user WHERE nome = %s AND email = %s"
        cursor.execute(query1, (name, email))
        row = cursor.fetchone()
        if row is None:
            # Insere os dados no MySQL
            query = "INSERT INTO user (nome, email) VALUES (%s, %s)"
            cursor.execute(query, (name, email))

            # Confirma as alterações no banco de dados
            conn.commit()
            
            r.expire(key, 60)

    # Fecha as conexões
    cursor.close()
    conn.close()
    time.sleep(1)