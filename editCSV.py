def CambiarLugarCSV(csv):
    csv_edit = open(csv,'r')
    lista_main = []
    for x in csv_edit:
        
        if(x != 0):
            atributos = x.strip().split(',')
            lista_main.append(atributos)
    return lista_main
def generarCSV(lista):
    nuevoCSV = open('C:/Users/thoma/Desktop/covidFinal.csv','w')
    c = 0
    instancia = ""
    
    for x in range(len(lista)):
        for y in range(len(lista[x])):
            if(y != 66):
                nuevoCSV.write(str(lista[x][y])+",")
            
        if(y == 66):
            
            nuevoCSV.write(str(lista[x][y])+"\n")
            
                  
def eliminarAtributo(lista):
    for x in range(len(lista)):
        del lista[x][2]
    return lista
def cambiarPosAtributo(lista):
    
    for x in range(len(lista)):
        
        lista[x].append(lista[x][2])
           
    lista = eliminarAtributo(lista)
    generarCSV(lista) 
    

        
            
            
cambiarPosAtributo(CambiarLugarCSV('C:/Users/thoma/Desktop/covid.csv'))
