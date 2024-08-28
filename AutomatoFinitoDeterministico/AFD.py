class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_atual = estado_inicial
        self.estados_aceitacao = estados_aceitacao

    def transitar(self, simbolo):
        # Verifica a transição com base no estado atual e símbolo
        if (self.estado_atual, simbolo) in self.transicoes:
            proximo_estado = self.transicoes[(self.estado_atual, simbolo)]
            print(f"Transição: ({self.estado_atual}, '{simbolo}') -> {proximo_estado}")
            self.estado_atual = proximo_estado
        else:
            raise ValueError(f"Transição não definida para estado {self.estado_atual} com símbolo '{simbolo}'")

    def processar_entrada(self, cadeia):
        print(f"Estado inicial: {self.estado_atual}")
        for simbolo in cadeia:
            if simbolo not in self.alfabeto:
                raise ValueError(f"Símbolo '{simbolo}' não pertence ao alfabeto!")
            self.transitar(simbolo)
        
        # Verifica se o estado final é de aceitação
        if self.estado_atual in self.estados_aceitacao:
            print(f"Estado final: {self.estado_atual} (Aceito)")
        else:
            print(f"Estado final: {self.estado_atual} (Rejeitado)")
        print('-' * 30)
        return self.estado_atual in self.estados_aceitacao


# Definir estados e transições do autômato
estados = {"R", "S", "T", "U"}
estado_inicial = "R"
estados_aceitacao = {"R"}  # Estado de aceitação conforme a imagem

# Função de transição (tabela)
transicoes = {
    ("R", "a"): "S",
    ("R", "b"): "U",
    ("S", "a"): "R",
    ("S", "b"): "T",
    ("T", "a"): "U",
    ("T", "b"): "S",
    ("U", "a"): "T",
    ("U", "b"): "R",
}

# Input do alfabeto pelo usuário
alfabeto_input = input("Insira os símbolos do alfabeto separados por espaço: ")
alfabeto = set(alfabeto_input.strip())

# Criar o AFD
afd = AFD(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)

# Teste de cadeias de exemplo
cadeias = ["aabb", "abba", "aa", "bb", "abab", "baab", ""]

for cadeia in cadeias:
    afd.estado_atual = estado_inicial  # Reinicia o estado atual
    print(f"Processando a cadeia: '{cadeia}'")
    aceita = afd.processar_entrada(cadeia)
