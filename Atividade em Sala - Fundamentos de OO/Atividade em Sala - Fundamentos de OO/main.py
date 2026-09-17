# Classes:
#   - Pessoa: atributos _nome, _vida (com validação de nome não vazio e vida >= 0)
#   - Time: atributos _nome, _membros (lista de objetos Pessoa)
# Validacoes Pretendidas:
#   1. Nome da Pessoa nao pode ser vazio.
#   2. Vida da Pessoa nao pode ser menor que zero.
# Validações Pretendidas:
#   1. Nome da Pessoa não pode ser vazio ("").
#   2. Vida da Pessoa não pode ser menor que zero (< 0).
# Uso de IA: Utilizada para revisão de sintaxe

class Pessoa:  
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida
 
    @property
    def nome(self):
        return self._nome
 
    @nome.setter
    def nome(self, novo_nome):
        # Nao Aceitar nome vazio
        if novo_nome == "":
            print("Erro: Nome nao pode ser vazio")
            self._nome = "Desconhecido"
        else: 
            self._nome = novo_nome
         
    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, nova_vida):
        # Nao aceitar vida menor que zero
        if nova_vida < 0:
            print("Erro: Vida nao pode ser negativa")
            self._vida = 0
        else:
            self._vida = nova_vida
        

class Time:
    def __init__(self, nome):
        self._nome = nome
        self._membros = []
        
    def adicionar_pessoa(self, pessoa):
        if isinstance(pessoa, Pessoa):
            self._membros.append(pessoa)
            print(f"{pessoa.nome} adicionado ao time {self._nome}.")

    def mostrar_time(self):
        print(f"\n Integrantes do time {self._nome}:")
        for membro in self._membros:
            print(f"- Nome: {membro.nome} | Vida: {membro.vida}")
    
    
# Demonstração

print(" 1. Duas formas de criação de objeto ")
p1 = Pessoa("Tião")                  # p1: usa valor padrão de vida (100)
p2 = Pessoa("Gandalf", vida=150)     # p2: passa nome e vida direta
print(f"Pessoa 1: {p1.nome}, Vida: {p1.vida}")
print(f"Pessoa 2: {p2.nome}, Vida: {p2.vida}\n")

print(" 2. Testando as duas validações (Recusa de valores inválidos) ")
p3 = Pessoa("Jorge", vida=-80)       # p3 recusa vida negativa
p4 = Pessoa("", vida=50)             # p4 recusa nome vazio
print(f"Pessoa 3: {p3.nome}, Vida: {p3.vida}")
print(f"Pessoa 4: {p4.nome}, Vida: {p4.vida}\n")

print(" 3. Associação entre classes ")
meu_time = Time("Sociedade do POO")
meu_time.adicionar_pessoa(p1)
meu_time.adicionar_pessoa(p2)
meu_time.mostrar_time()



# AUTOAVALIACAO

# dificuldade em pensar como reagrupar ambas classes
# IA usada pra acessar como associar a classe
