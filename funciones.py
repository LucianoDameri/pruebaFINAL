import random,os,time

trabajadores = ["Juan Pérez","María García",
            "Carlos López","Ana Martínez",
            "Pedro Rodríguez","Laura Hernández",
            "MiguelSánchez","Isabel Gómez",
            "Francisco Díaz","Elena Fernández"]

sueldos=[]
menor=[]
entre=[]
superior=[]
Reporte=[]







def menu():
    print("Bienvenido")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

def opt1():
    
    for x in range(len(trabajadores)):
        aleatorio=random.randint(300000,2500000)
        print(trabajadores[x]," : ","$",aleatorio)
        sueldos.append(aleatorio)
        
        a=(trabajadores[x]   ,   aleatorio)
        if aleatorio < 800000:
            menor.append(a)
        elif aleatorio >= 800000 and aleatorio <= 2000000:
            entre.append(a)
        else:
            superior.append(a)
    

    
            
def opt2():
    menorc=0
    entrec=0
    superiorc=0
    print("Sueldos menores a $800.000")
    for x in range(len(menor)):
        menorc=menorc+1

    print("TOTAL: ",menorc)
    print("Nombre empleado    Sueldo")
    for x in range(len(menor)):
        print(menor[x])

    print("Sueldos entre $800.000 y $2.000.000")
    for x in range(len(entre)):
        entrec=entrec+1

    print("TOTAL: ",entrec)
    print("Nombre empleado    Sueldo")
    for x in range(len(entre)):
        print(entre[x])

    print("Sueldos superiores a $2.000.000")
    for x in range(len(superior)):
        superiorc=superiorc+1

    print("TOTAL: ",superiorc)
    for x in range(len(superior)):
        print(superior[x])

    total=0
    for x in range(len(sueldos)):
        total=total+sueldos[x]
        

    print("TOTAL SUELDOS: $",total)

def opt3():
    print("sueldo mas alto")
   


    print("sueldo mas bajo")

    print("Promedio de sueldos")
    promedio=(sueldos[0]+sueldos[1]+sueldos[2]+sueldos[3]+sueldos[4]+sueldos[5]+sueldos[6]+sueldos[7]+sueldos[8]+sueldos[9])/10
    print("$",promedio)

    print("media geométrica")
    mg=(sueldos[0]*sueldos[1]*sueldos[2]*sueldos[3]*sueldos[4]*sueldos[5]*sueldos[6]*sueldos[7]*sueldos[8]*sueldos[9])**(1/10)
    print(mg)
    
    
            
        
    
    
            

    
            
        
        
def opt4():
    print("Nombre empleado    Sueldo base      Descuento saluda    Descuento AFP     Sueldo liquido")
    salud=100/7
    afp=100/12
    final=100/19
    

    for x in range(10):

        print(trabajadores[x],"  $",sueldos[x],"  $",sueldos[x]*salud,"  $",sueldos[x]*afp,"  $",sueldos[x]- sueldos[x]*final)
        Reporte.append(trabajadores[x],"  $",sueldos[x],"  $",sueldos[x]*salud,"  $",sueldos[x]*afp,"  $",sueldos[x]- sueldos[x]*final)

    

def opt5():
    print("Finalizando programa...")
    print("Desarrollado por Luciano Castelli")
    print("RUT 21.884.525-8")
    exit()