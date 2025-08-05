from .lista_encadeada import ListaEncadeada

def menu():
    fila = ListaEncadeada()

    while True:
        print("\nMENU")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = input(">> ")

        if opcao == '1':
            fila.inserir()
        elif opcao == '2':
            fila.imprimirListaEspera()
        elif opcao == '3':
            fila.atenderPaciente()
        elif opcao == '4':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente de novo.")
