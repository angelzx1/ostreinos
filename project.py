while True:
    user=(str(input("Digite seu nome, por favor: ")))
    resposta=input("Olá, "+user+" deseja uma lista sobre como ter uma namorada? (S/N) ")
    if(resposta == "s"):
        print("aqui está a lista abaixo:")
        print("1) Encontre uma mina ideal para você e os mesmos interesses;")
        print("2) Tente elogiar a personalidade dela e chame-a de linda, maravilhosa, e perfeita;")
        print("3) Chame ela para encontros e seja cavalheiro para pagar lanches para ela;")
        print("4) Dê a atenção à ela seja carinhoso e tenha um bom papo;")
        print("5) É claro respeite o espaço dela;")
    elif(resposta == "n"):
        print("Pois então seja feliz na vida solitária, mas não jogue League of Legends pois pode te fazer muito mal!!")

    else:
        print("Serviço Indisponível")
