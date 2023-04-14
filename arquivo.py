visitantes = []

while True:
    nome = input("Digite o nome completo do visitante: ")
    if not nome.isalpha():
        print("O nome deve conter apenas letras. Tente novamente.")
        continue
        
    idade = input("Digite a idade do visitante: ")
    documento = input("Digite o número do documento de identificação do visitante: ")
    if len(documento) != 11:
        print("O número do documento de identificação deve conter 11 dígitos. Tente novamente.")
        continue
        
    motivo = input("Digite o motivo da visita: ")
    horario_entrada = input("Digite o horário de entrada do visitante (formato HH:MM): ")
    horario_saida = input("Digite o horário de saída do visitante (formato HH:MM): ")
    
    visitante = [nome, idade, documento, motivo, horario_entrada, horario_saida]
    visitantes.append(visitante)
    
    print("Registro concluído com sucesso.")
    
    continuar = input("Deseja registrar outro visitante? (S/N)")
    if continuar.upper() == "N":
        break
        
nome_pesquisa = input("Digite o nome do visitante que deseja pesquisar: ")
encontrado = False
for visitante in visitantes:
    if visitante[0] == nome_pesquisa:
        print(f"Nome: {visitante[0]}")
        print(f"Idade: {visitante[1]}")
        print(f"Documento: {visitante[2]}")
        print(f"Motivo da visita: {visitante[3]}")
        print(f"Horário de entrada: {visitante[4]}")
        print(f"Horário de saída: {visitante[5]}")
        encontrado = True
        break
        
if not encontrado:
    print("Visitante não encontrado.")
