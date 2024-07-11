import random,os,time

from funciones import *

sueldos=[]
menor=[]
entre=[]
superior=[]
Reporte=[]

menorc=0
entrec=0
superiorc=0

trabajadores = ["Juan Pérez","María García",
            "Carlos López","Ana Martínez",
            "Pedro Rodríguez","Laura Hernández",
            "MiguelSánchez","Isabel Gómez",
            "Francisco Díaz","Elena Fernández"]


while True:
    try:
        os.system('cls')




        menu()

        opt=int(input("Seleccione una opción: "))

        if opt in(1,2,3,4,5):
            pass
            
        else:
            print("ERROR debe de ser una de las opciones visibles")
            time.sleep(2)
    except:
        print("Error no puede ser una letra")
        time.sleep(2)

    if opt==1:
            os.system('cls')
            opt1()
            print("Sueldos Asignados correctamente")
            input("presione enter para volver al menú")
   
    elif opt==2:
        os.system('cls')    
        opt2()
        input("presione enter para volver al menú")
    elif opt==3:
        opt3()
    
    
    
    
    
    
    
    
    elif opt==4:
        pass
    else:
        opt5()
            
            
        
            
            

        



