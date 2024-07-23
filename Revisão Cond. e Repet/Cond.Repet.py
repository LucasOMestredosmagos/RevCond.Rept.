class Autenticacao:
    def __init__(self):
        self.email_cadastrado = "teste@email.com"
        self.senha_cadastrada = "777teste"
        
    def autenticar(self):
        while True:
            email_usuario = input("Digite seu email: ") 
            senha_usuario = input("Digite sua senha: ")
            
            if self.verificar_documentacao(email_usuario, senha_usuario):
                print("Login realizado com exito!")
                break
            else:
                print("Email ou senha incorretos. Tente novamente.")
    
    def verificar_documentacao(self, email, senha):
        return email == self.email_cadastrado and senha == self.senha_cadastrada 
    
if __name__ == "__main__":
    autenticacao = Autenticacao() 
    autenticacao.autenticar()            
                       
        
            