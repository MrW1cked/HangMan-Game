import os

palabra = ""
pista = ""

ayuda = 0
tamanho_palabra = 0


def intentos(vidas):
    if vidas == 23:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       	               |")
        print("|	       	               |")
        print("|	                       |")
        print("|	                       |")
        print("|	    	               |")
        print("|__________________________|")
    elif vidas == 22:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       	               |")
        print("|	       	               |")
        print("|	                       |")
        print("|	                       |")
        print("|	    _     		       |")
        print("|__________________________|")
    elif vidas == 21:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       	               |")
        print("|	       	               |")
        print("|	                       |")
        print("|	                       |")
        print("|	    __    		       |")
        print("|__________________________|")
    elif vidas == 20:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       	               |")
        print("|	       	               |")
        print("|	                       |")
        print("|	                       |")
        print("|	    ___    		       |")
        print("|__________________________|")
    elif vidas == 19:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       	               |")
        print("|	       	               |")
        print("|	                       |")
        print("|	                       |")
        print("|	    ___|    		   |")
        print("|__________________________|")
    elif vidas == 18:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       	               |")
        print("|	       	               |")
        print("|	                       |")
        print("|	                       |")
        print("|	    ___|_    		   |")
        print("|__________________________|")
    elif vidas == 17:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       	               |")
        print("|	       	               |")
        print("|	                       |")
        print("|	                       |")
        print("|	    ___|__    		   |")
        print("|__________________________|")
    elif vidas == 16:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       	               |")
        print("|	       	               |")
        print("|	                       |")
        print("|	                       |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 15:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       	               |")
        print("|	       	               |")
        print("|	                       |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 14:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       	               |")
        print("|	       	               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 13:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       	               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 12:
        print(" __________________________")
        print("|     	         	       |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 11:
        print(" __________________________")
        print("|     	    _     	       |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 10:
        print(" __________________________")
        print("|     	    __     	       |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 9:
        print(" __________________________")
        print("|     	    ___    	       |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 8:
        print(" __________________________")
        print("|     	    ____   	       |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 7:
        print(" __________________________")
        print("|     	    _____  	       |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 6:
        print(" __________________________")
        print("|     	    _____  	       |")
        print("|	       |     |         |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 5:
        print(" __________________________")
        print("|     	    _____  	       |")
        print("|	       |     |         |")
        print("|	       |     O         |")
        print("|	       |               |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 4:
        print(" __________________________")
        print("|     	    _____  	       |")
        print("|	       |     |         |")
        print("|	       |     O         |")
        print("|	       |     |         |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 3:
        print(" __________________________")
        print("|     	    _____  	       |")
        print("|	       |     |         |")
        print("|	       |     O         |")
        print("|	       |    /|         |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 2:
        print(" __________________________")
        print("|     	    _____  	       |")
        print("|	       |     |         |")
        print("|	       |     O         |")
        print("|	       |    /|\        |")
        print("|	       |               |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 1:
        print(" __________________________")
        print("|     	    _____  	       |")
        print("|	       |     |         |")
        print("|	       |     O         |")
        print("|	       |    /|\        |")
        print("|	       |    /          |")
        print("|	    ___|___    		   |")
        print("|__________________________|")
    elif vidas == 0:
        print(" __________________________")
        print("|     	   _____  	       |")
        print("| GAME     |     |         |")
        print("|    OVER  |     O         |")
        print("|	       |    /|\        |")
        print("|	       |    / \        |")
        print("|	    ___|___    		   |")
        print("|__________________________|")


def juego():
    print("\nBienvenido al Juego del ahorcado")

    print(" __________________________")
    print("|     	    _____	       |")
    print("|	       |     |	       |")
    print("|	       |     O	       |")
    print("|	       |	/|\	       |")
    print("|	       |    / \	       |")
    print("|	    ___|___		       |")
    print("|__________________________|")

    palabra = input("Inserta tu palabra para empezar: ").upper()
    if palabra == "":
        print("ERROR! Escribe otra palabra")
        juego()
    else:
        tamanho_palabra = len(palabra) - 1
        palabra_oculta = ""
        ayuda = 0
        vida = 23
        while ayuda <= tamanho_palabra:
            palabra_oculta = palabra_oculta + "_"
            ayuda += 1
        print("\nTU PALABRA ES: \n" + palabra_oculta)
        print("\nVamos a jugar!")

        while vida > 0:
            intentos(vida)
            pista = input("Inserta una letra: ").upper()
            if len(pista) >= 2:
                print("Solo puedes escribir una letra de cada vez!! Dale carinho vamos...")
            else:
                i = 0
                mudanza = palabra_oculta
                while i <= tamanho_palabra:
                    if palabra[i] == pista:
                        palabra_oculta = palabra_oculta[:i] + pista + palabra_oculta[i + 1:]
                        if palabra_oculta == palabra:
                            print("\n\nHAS GANADO!!!")
                            print("********************************")
                            juego()
                    i += 1
                if mudanza == palabra_oculta:
                    vida = vida - 1
                    intentos(vida)
                    print("Intenta de Nuevo:")
                    print("\n\nTu palabra es: \n" + palabra_oculta)
                else: print("\n\nTu palabra es: \n" + palabra_oculta)
            if vida == 0:
                print("\n\nHas Perdido! Tu palabra era: " + palabra)
                juego()


#unica instrucion del terminal:

juego()