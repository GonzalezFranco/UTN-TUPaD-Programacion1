#Ejercicio1
with open("productos.txt","w") as archivo:
    
        archivo.write("Calabaza,180,2 \n")
        archivo.write("Salamin,246,1 \n")
        archivo.write("Limon,180,2 \n")
        archivo.close()
#------------------------------------------------------
#Ejercicio2
with open("productos.txt","r") as archivo:
    formato = archivo.readlines()
    for linea in formato:
        print(linea.strip().split(","), )
 
    archivo.close()    
#------------------------------------------------------
#------------------------------------------------------
#------------------------------------------------------
#------------------------------------------------------
#------------------------------------------------------    

