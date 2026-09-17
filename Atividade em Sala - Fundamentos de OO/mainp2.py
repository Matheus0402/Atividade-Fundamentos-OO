
# PASSO 1: PLANO
# Domínio: Loja de Pokémon TCG (Trading Card Game) -> Testar meu Nicho em POO
# Classes e Atributos:
#   - CartaPokemon: _nome , _preco, _estoque 
#   - LojaPokemon: _nome_loja, _catalogo (list de objetos CartaPokemon)
# Validações Pretendidas:
#   1. Nome da Carta não pode ser vazio ("").
#   2. Preço da Carta não pode ser negativo ou nulo (<= 0).
# Tempo Previsto:
#   - Planejamento e esboço UML: 35 min -> Aprender a fazer
#   - Implementação das classes com properties e validações: 15 min
#   - Demonstração no console: 5 min
#   - Autoavaliação: 5 min
# ==============================================================================

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
            print("Erro de Validacao: O nome da carta não pode ser vazio.")
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
            print(f"Erro de Validacao: Preço R${novo_preco:.2f} invalido. Deve ser maior que zero.")
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


class LojaPokemon:
    def __init__(self, nome_loja):
        self.nome_loja = nome_loja
        self._catalogo = []

    @property
    def nome_loja(self):
        return self._nome_loja

    @nome_loja.setter
    def nome_loja(self, novo_nome):
        if not novo_nome or novo_nome.strip() == "":
            print("Erro de Validacao: Nome da loja nao pode ser vazio.")
            self._nome_loja = "Loja TCG Sem Nome" #caso nao adicione, marmanjo ja fica taggado sem nome
        else:
            self._nome_loja = novo_nome

    @property
    def catalogo(self):
        return self._catalogo

    def adicionar_carta(self, carta):
        # aqui a magica faz com que que apenas objetos da classe CartaPokemon sejam adicionados
        if isinstance(carta, CartaPokemon):
            self._catalogo.append(carta)
            print(f"-> '{carta.nome}' adicionada ao catalogo da {self.nome_loja}.")
        else:
            print("Erro: Apenas objetos da classe CartaPokemon podem ser adicionados.")

    def exibir_vitrine(self):
        print(f"\n============= VITRINE: {self.nome_loja} =============")
        if not self._catalogo:
            print("nenhuma carta disponivel no catalogo.")
        else:
            for carta in self._catalogo:
                print(f"- {carta.ficha()}")
        print("============================================================\n")


# DEMONSTRAÇÃO (Critério 6)


print("- 1. Duas formas de criação de objeto (Parametro Padrao) -")
# v1: usa estoque padrao (1 unidade)
c1 = CartaPokemon("Pikachu Illustrator", 150000.0)
# v2: informa estoque de ponta a ponta
c2 = CartaPokemon("Charizard Base Set", 4500.0, estoque=3)
print(f"Carta 1 (Estoque padrao): {c1.nome} | R${c1.preco:.2f} | Qtd: {c1.estoque}")
print(f"Carta 2 (Estoque customizado): {c2.nome} | R${c2.preco:.2f} | Qtd: {c2.estoque}\n")

print("- 2. Testando recusa de valores invalidos -")
c_invalida_preco = CartaPokemon("Mewtwo EX", -250.0)  # preco negativo
c_invalida_nome = CartaPokemon("", 80.0)              # nome em branco
print(f"Resultado c_invalida_preco -> {c_invalida_preco.ficha()}")
print(f"Resultado c_invalida_nome  -> {c_invalida_nome.ficha()}\n")

print("- 3. Associacao entre classes (LojaPokemon contendo Cartas) -")
loja = LojaPokemon("Pallet Town Card Shop")
loja.adicionar_carta(c1)
loja.adicionar_carta(c2)
loja.exibir_vitrine()



# PASSO 3: AUTOAVALIAÇÃO

# - Trecho que deu mais trabalho: Fazer o alinhamento das properties e garantir
#   que o construtor da loja também passasse pela validação do setter.
# - Em que a IA ajudou: Auxiliou na formulação do domínio temático de Pokémon TCG
#   e na geração do diagrama de classes UML em sintaxe Mermaid e texto.
# - Em que a IA atrapalhou: A IA inicialmente sugeriu colocar cálculos de dano
#   e combate de Pokémon, o que descaracterizaria o modelo de loja/comércio e
#   tornaria o escopo desnecessariamente complexo para a entrega em 60 min.
