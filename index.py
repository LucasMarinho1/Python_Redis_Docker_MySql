import redis

def menu():
            
    menu = ("\n\n\n\n##--Teste Estrutura de Menu--##\n"+
            "|-----------------------------|\n"+
            "| Opção 1 - Create User       |\n"+
            "| Opção 2 - List All Users    |\n"+
            "|-----------------------------|\n\n")
    print(menu)


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
    def CreateUser(self):
        conexao = ConexaoRedis()
        redis = conexao.openConection()
        
        last_id = redis.get("last_id")
        if last_id is None:
            redis.set("last_id", 1)
            next_id = 1
        else:
            next_id = redis.incr("last_id")

        new_key = "user:" + str(next_id)   
        redis.hset(new_key, "name", nome)
        redis.hset(new_key, "email", email)
        redis.expire(new_key, 60)
        
        conexao.closeConection(redis)
        pass
    
    def GetAllUser(self):
        # Implementação do método 2
        pass   
    
class ConexaoRedis:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 6379
        self.password = "Redis2019!"
        self.charset = "utf-8"
        pass
    
    def openConection(self):
        r = redis.StrictRedis(
        host=self.host, 
        port=self.port, 
        password=self.password,
        charset=self.charset)
        return r
    
    def closeConection(self, conexao):
        conexao.close
        pass
    
#-------------------------------------------
menu()
opcao = int(input("Digite uma opcao acima:"))

if opcao == 1:
    
    nome = input("nome:")
    email = input("email:")
    usuario = Usuario(nome, email)
    usuario.CreateUser()

else:
    print("Opção inválida")



