# Sistema de Gestão de Peças e Qualidade

pecas_aprovadas = []
pecas_reprovadas = []
capacidade_caixa = 10

def cadastrar_peca():
    print("\n--- Cadastro de Nova Peça ---")
    try:
        id_peca = input("ID da Peça: ")
        peso = float(input("Peso (g): "))
        cor = input("Cor (azul/verde): ").lower().strip()
        comprimento = float(input("Comprimento (cm): "))
        
        motivos = []
        if not (95 <= peso <= 105):
            motivos.append(f"Peso fora da faixa ({peso}g)")
        if cor not in ['azul', 'verde']:
            motivos.append(f"Cor inválida ({cor})")
        if not (10 <= comprimento <= 20):
            motivos.append(f"Comprimento fora da faixa ({comprimento}cm)")
            
        peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento}
        
        if not motivos:
            pecas_aprovadas.append(peca)
            print(f"✅ Peça {id_peca} APROVADA e enviada para linha de embalagem.")
        else:
            peca["motivo"] = ", ".join(motivos)
            pecas_reprovadas.append(peca)
            print(f"❌ Peça {id_peca} REPROVADA. Motivo: {peca['motivo']}")
    except ValueError:
        print("Erro: Insira valores numéricos válidos para peso e comprimento.")

def listar_pecas():
    print("\n--- Peças Aprovadas ---")
    for p in pecas_aprovadas:
        print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']}")
    
    print("\n--- Peças Reprovadas ---")
    for p in pecas_reprovadas:
        print(f"ID: {p['id']} | Motivo: {p['motivo']}")

def remover_peca():
    id_rem = input("Digite o ID da peça que deseja remover: ")
    global pecas_aprovadas, pecas_reprovadas
    original_len = len(pecas_aprovadas) + len(pecas_reprovadas)
    
    pecas_aprovadas = [p for p in pecas_aprovadas if p['id'] != id_rem]
    pecas_reprovadas = [p for p in pecas_reprovadas if p['id'] != id_rem]
    
    if (len(pecas_aprovadas) + len(pecas_reprovadas)) < original_len:
        print(f"Peça {id_rem} removida com sucesso.")
    else:
        print("ID não encontrado.")

def listar_caixas():
    total_aprovadas = len(pecas_aprovadas)
    caixas_fechadas = total_aprovadas // capacidade_caixa
    pecas_na_ultima = total_aprovadas % capacidade_caixa
    
    print(f"\n--- Status de Armazenamento ---")
    print(f"Caixas fechadas (10 peças cada): {caixas_fechadas}")
    print(f"Peças na caixa atual (em processamento): {pecas_na_ultima}/10")

def gerar_relatorio():
    print("\n================================")
    print("      RELATÓRIO CONSOLIDADO     ")
    print("================================")
    print(f"Total Aprovadas: {len(pecas_aprovadas)}")
    print(f"Total Reprovadas: {len(pecas_reprovadas)}")
    print(f"Caixas Utilizadas (Total): {(len(pecas_aprovadas) + 9) // 10}")
    print("\nDetalhes de Reprovação:")
    for p in pecas_reprovadas:
        print(f"- Peça {p['id']}: {p['motivo']}")
    print("================================\n")

while True:
    print("\n--- MENU INDUSTRIAL ---")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1': cadastrar_peca()
    elif opcao == '2': listar_pecas()
    elif opcao == '3': remover_peca()
    elif opcao == '4': listar_caixas()
    elif opcao == '5': gerar_relatorio()
    elif opcao == '0': break
    else: print("Opção inválida.")