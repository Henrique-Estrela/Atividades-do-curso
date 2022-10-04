def calcular():
        if x > 0 and y > 0 :
            return print(("-"*30)+"\nPrimeiro quadrante\n"+("-"*30)+"\n")
        elif x < 0 and y > 0:
            return print(("-"*30)+"\nSegundo quadrante \n"+("-"*30)+"\n")
        elif x < 0 and y < 0:
            return print(("-"*30)+"\nTerceiro quadrante \n"+("-"*30)+"\n")
        elif x > 0 and y < 0:
            return print(("-"*30)+"\nQuarto quadrante \n"+("-"*30)+"\n")
            
        else:
            return None





    
while  True:
        try:
            x = int(input("Digite um numero do X \n>>>>"))
            y = int(input("Digite um numero do Y \n>>>>"))
            if x == 0 or y == 0:
                
                break 
            else:
                calcular() 
        except:
            print("Tá vazia...preenchhe de novo ai")
            continue
        

         

    
    
