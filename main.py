import fonctionnalites

choix = 100
while True : 
    print("#"*10, "Calculatrice", "#"*10)
    print()
    print("1 - Addition \n2 - Soustraction \n3 - Division \n4 - Multiplication \n5 - Calcul personnalisé")
    choix = int(input("Saisissez un nombre (0 pour quitter) : "))
    if choix == 0 :
        print("Meric d'avoir utilisé notre calculatrice. Au revoir")
        print("#"*40)
        break
    print()
    a = float(input("premier nombre : "))
    b = float(input("second nombre : "))
    
    if choix == 1 : 
        print("résultat :", fonctionnalites.addition(a,b))
    
    elif choix == 2 : 
        print("résultat :", fonctionnalites.soustraction(a,b))
        
    elif choix == 3 : 
        print("résultat :", fonctionnalites.division(a,b))
        
    elif choix == 4 : 
        print("résultat :", fonctionnalites.multiplication(a,b))
        
    elif choix == 5 : 
        p = input()
        
            
    print("-"*30)









