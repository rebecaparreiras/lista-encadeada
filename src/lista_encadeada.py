from .nodo import Nodo

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.num_verde = 1
        self.num_amarelo = 201

    def inserirSemPrioridade(self, novo):
        if self.head is None:
            self.head = novo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo

    def inserirComPrioridade(self, novo):
        if self.head is None or self.head.cor == 'V':
            novo.proximo = self.head
            self.head = novo
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == 'A':
                atual = atual.proximo
            novo.proximo = atual.proximo
            atual.proximo = novo

    def inserir(self):
        cor = input("Informe a cor do cartão (A/V): ").upper()
        while cor not in ('A', 'V'):
            print("Cor inválida. Digite A ou V.")
            cor = input("Informe a cor do cartão (A/V): ").upper()

        if cor == 'V':
            numero = self.num_verde
            self.num_verde += 1
        else:
            numero = self.num_amarelo
            self.num_amarelo += 1

        print(f"Informe o número do cartão: {numero}")
        novo = Nodo(numero, cor)

        if self.head is None:
            self.head = novo
        elif cor == 'A':
            self.inserirComPrioridade(novo)
        else:
            self.inserirSemPrioridade(novo)

    def imprimirListaEspera(self):
        atual = self.head
        print("Lista -> ", end="")
        while atual is not None:
            print(f"[{atual.cor},{atual.numero}]", end=" ")
            atual = atual.proximo
        print()

    def atenderPaciente(self):
        if self.head is None:
            print("Nenhum paciente na fila.")
        else:
            print(f"Atendendo o paciente cartão cor {self.head.cor} e número {self.head.numero}")
            self.head = self.head.proximo
