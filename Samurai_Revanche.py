#comecanso jogo numbers modo revanche


jogos_jogados = 0
vitorias = 0

def jogar_multiplayer():
    global jogos_jogados, vitorias
    
    print("++++++++MODO MULTIPLAYER ATIVADO REVANCHE")
    
    player1 = input("Digite seu nome player 1: ")
    player2 = input("Digite seu nome player2: ")
    
    vez_de_escolher = player1
    vez_de_adivinhar = player2
    
    jogando_revanche = True
    while jogando_revanche:
        
        print(f"\n-_--_-RODADA: {vez_de_escolher} | ESCOLHE | {vez_de_adivinhar} | ADIVINHA-_--_-")
        
        numero_secreto = int(input(f"Digite o numero secreto {vez_de_escolher}: "))
        
        print("\n" + "="*40)
        print(f"{vez_de_adivinhar} NAO OLHA A TELA HONRA DO SAMURAI!")
        print("="*40)
        input("Aperta Enter quando o outro jogador tiver Longe...")
        print("\n" * 200)
        print(f"NUMERO SECRETO GUARDADO!! Agora é a vez : {vez_de_adivinhar}")
        
        tentativas = []
        chute = 0
        
        while chute != numero_secreto:
            chute = int(input(f"{vez_de_adivinhar}: Chuta um Numero "))
            tentativas.append(chute)
            
            if chute < numero_secreto:
                print(f"Erro fei erro rude tenta um numero mas alto tartaruga ninja")
            elif chute > numero_secreto:
                print(f"Chuto Chuto mas alto dms bateu na trave tenta de novo ")
            else:
                print(f"AEEEE REI DO CANGACO ACERTOOU NUMERO ERA: {numero_secreto}")
                
        total = len(tentativas)
        jogos_jogados =+ 1
        vitorias =+ 1
        
        print(f"\n{vez_de_adivinhar} usou {total} tentativas")
        print(f"Chutes do {vez_de_adivinhar}: {tentativas}")
        
        if total == 1:
            print(f"{vez_de_adivinhar} é o monstro dos monstros ")
        elif total <= 3:
            print(f"{vez_de_adivinhar} É ESMAGADORRR")
        elif total <= 10:
            print(f"{vez_de_adivinhar} É PRO NINJA DOS NINJA")
        else:
            print(f"{vez_de_adivinhar} É NOOB TEM QUE MELHORARRR")
            
        print("\n" + "-"*30)
        quer_revanche = input(f"{vez_de_adivinhar} QUER REVANCHE? s/n: ").lower().strip()
        
        if quer_revanche == 's':
            vez_de_escolher, vez_de_adivinhar = vez_de_adivinhar, vez_de_escolher
            
            print("\nREVANCHE ACEITA INVERTENDO PAPEIS...")
        else:
            jogando_revanche = False
            print("\nREVANCHE NEGADA Voltando pro menu...")
            
while True:
    print("SAMURAI REVANCHEE")
    print("1- Jogar Multiplayer com REVANCHE")
    print("2- Ver Estatisticas.")
    print("3- Sair!")
    
    escolha = input("Escolha a opcao desejada...")
    
    if escolha == '1':
        jogar_multiplayer()
    elif escolha == '2':
        print("ESTATISTICAS....")
        print(f"Jogos Jogados: {jogos_jogados} ")
        print(f"Vitorias: {vitorias}")
        
        if jogos_jogados > 0:
            taxa = (vitorias / jogos_jogados)
            print(f"Taxa de acerto: {taxa:1.f}%")
    elif escolha == '3':
        print("VALEU SAMURAIS DO NORDESTE!!!")
        break
    else:
        print("Opcao Invalida: Digite 1, 2, ou 3 ")
        
        
        
    

