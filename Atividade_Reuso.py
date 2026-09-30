# Plano 1 ---> Estruturacao de DOMINIO | SUPERCLASSE | SUB1 | SUB2 | <---
# Retornando sobre o trabalho de Pokemon TCG, agora iremos compreender as subcartas ligadas a uma carta MAE.
#
# DOMINIO: LOJA POKEMON TCG
# 
# SUPERCLASSE: CartaPokemon (atraves dela que saira todas as demais cartas, alem de realizar o trabalho do "eh um") | _nome _preco _estoque
#
# SUB1: CartaEstagio (eh uma CartaPokemon? Sim | Atraves dela que os pokemons evolui para o seu proximo estagio)
#
# SUB2: CartaEnergia (eh uma CartaPokemon? Sim | Atraves dela que os pokemons adquirem a possibilidade de utilizar um ataque)

# Categorizacao SUBCLASSES:
# Cada subclasse adiciona atributos proprios: ps (Pontos de Saude) para a classe de estagio/batalha, e tipo_energia para a classe de energia
# Ambas as subclasses chamam super().__init__() para reaproveitar a validacao e criacao de nome, preco e estoque
# Metodo Sobrescrito: As subclasses chamarao super().ficha() para reaproveitar a formatacao base (nome, preco, estoque) e apenas concatenar os atributos proprios no final.




class CartaPokemon:
    def __init__(self, nome, preco, estoque=1):
        # o construtor reaproveita os setters para validar o estado inicial
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        # v1: Recusar nome vazio
        if not novo_nome or novo_nome.strip() == "":
            print("Erro de Validacao: O nome da carta nao pode ser vazio.")
            self._nome = "Carta Desconhecida"
        else:
            self._nome = novo_nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        # v2: Recusar preco menor ou igual a zero
        if novo_preco <= 0:
            print(f"Erro de Validacao: Preco R${novo_preco:.2f} invalido. Deve ser maior que zero.")
            self._preco = 1.0  # valor minimo
        else:
            self._preco = float(novo_preco)

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, novo_estoque):
        if novo_estoque < 0:
            print("Erro de Validacao: Estoque nao pode ser negativo.")
            self._estoque = 0
        else:
            self._estoque = int(novo_estoque)

    def ficha(self):
        return f"Carta: {self._nome:<18} | Preco: R${self._preco:>7.2f} | Estoque: {self._estoque} un"
    # eh daqui que iremos herdar a contextualizacao do sobrescrito
    
    # Subclasse 1: Teste do "eh um" ---> CartaPokemonEstagio EH UMA CartaPokemon
class CartaPokemonEstagio(CartaPokemon):
    """Subclasse para cartas de Pokemon de Batalha que possuem Pontos de Saude (PS)."""
    def __init__(self, nome, preco, ps, estoque=1):

    # Chama super() para inicializar a parte herdada
        super().__init__(nome, preco, estoque)
    # Atributo proprio
        self.ps = ps
        
    @property
    def ps(self):
        return self._ps

    @ps.setter
    def ps(self, novo_ps):
        if novo_ps <= 0:
            print("Erro de Validacao: PS deve ser um valor positivo.")
            self._ps = 30  # valor minimo padrao no TCG
        else:
            self._ps = int(novo_ps)
            
    def ficha(self):
        return f"{super().ficha()} | PS: {self.ps} HP"
    
    
    #Subclasse 2: Teste do "eh um" --> CartaEnergia EH UMA CartaPokemon
class CartaEnergia(CartaPokemon):
    """Subclasse para cartas de Energia usadas no jogo."""
    def __init__(self, nome, preco, tipo_energia, estoque=1):
        # Chama super() para inicializar a parte herdada
        super().__init__(nome, preco, estoque)
        # Atributo proprio
        self.tipo_energia = tipo_energia
        
        @property
        def tipo_energia(self):
            return self._tipo_energia

        @tipo_energia.setter
        def tipo_energia(self, novo_tipo):
            if not novo_tipo or novo_tipo.strip() == "":
                print("Erro de Validacao: Tipo de energia nao pode ser vazio.")
                self._tipo_energia = "Incolor" # Padrao do Jogo
            else:
                self._tipo_energia = novo_tipo.strip()

        # Criterio 4: Sobrescrita reaproveitando a versao herdada com super()
        def ficha(self):
            return f"{super().ficha()} | [Energia: {self._tipo_energia}]"
        
class LojaPokemon:
    """Classe agregadora que gerencia a vitrine/catalogo."""
    def __init__(self, nome_loja):
        self.nome_loja = nome_loja
        self._catalogo = []

    @property
    def nome_loja(self):
        return self._nome_loja

    @nome_loja.setter
    def nome_loja(self, novo_nome):
        if not novo_nome or novo_nome.strip() == "":
            self._nome_loja = "Loja TCG Sem Nome" 
        else:
            self._nome_loja = novo_nome.strip()
            
    def adicionar_carta(self, carta):
        if isinstance(carta, CartaPokemon):
            self._catalogo.append(carta)
            print(f"-> Cadastrada: '{carta.nome}' na loja {self.nome_loja}.")
        else:
            print("Erro: Apenas objetos herdados de CartaPokemon sao aceitos.")
            
# Trabalhar no Criterio 5
# Uma colecao do tipo da superclasse com objetos das duas subclasses,
# percorrida por um unico laco, sem instanceof ou isinstance     

    def exibir_vitrine(self):
            print(f"\n**** VITRINE: {self.nome_loja} ****")
            if not self._catalogo:
                print("Nenhuma carta disponivel no catalogo.")
            else:
                # UM UNICO LACO para ambas as subclasses, chamando apenas .ficha()
                for carta in self._catalogo:
                    print(f"- {carta.ficha()}")

print("--- 1. Instanciando Objetos das Subclasses ---")
c_estagio = CartaPokemonEstagio("Charizard Base Set ", 4500.0, ps=120, estoque=2)
c_energia1 = CartaEnergia("Energia de Fogo ", 15.0, tipo_energia="Fogo", estoque=10)
c_energia2 = CartaEnergia("Energia Eletrica ", 5.0, tipo_energia="Eletrica", estoque=20)

print("\n--- 2. Adicionando ao Catalogo da Loja ---")
loja = LojaPokemon("Pallet Town Card Shop")
loja.adicionar_carta(c_estagio)
loja.adicionar_carta(c_energia1)
loja.adicionar_carta(c_energia2)

print("\n--- 3. Demonstracao do Criterio 5 (Unico Laco Polimorfico) ---")
# A vitrine vai percorrer a lista mista usando um unico `for` sem isinstance!
loja.exibir_vitrine()



#AUTO AVALIACAO

# a coisa mais complexa foi entender esse isinstance para compreender e analisar dentro do codigo
# a ideia principal eh cada vez mais implementar uma atualizacao, e assim estamos seguindo com a construcao dessa loja com catalogos
# me travei bastante na ideia do laco, mas entendi a sua funcionalidade
