edad = 58
genero = 'F'
semanas = 240

if genero == 'F':
    if edad >= 58:
        if semanas >= 250:
            print('Se puede pensionar')
        else:
            print('Le faltan '+str( 250 - semanas ) +' semanas')
    else:    
        print('Le faltan '+str( 58 - edad ) +' años')
elif genero == 'M':
    if edad >= 60:
        if semanas >= 255:
            print('Se puede pensionar')
        else:
            print('Le faltan '+str( 255 - semanas ) +' semanas')
    else:    
        print('Le faltan '+str( 60 - edad ) +' años')
else:
    print('Genero no valido')
#------------------------------------------------------------------
def verificar_mayor(edad1, edad2, edad3, edad4):
    if edad1 > edad2 and edad1 > edad3 and edad1 > edad4:
        print('1 '+ str(edad1))
    elif edad2 > edad3 > edad4:
        print('2 '+ str(edad2))
    elif edad3 > edad4:
        print('3 '+ str(edad3))
    else:
        print('4 '+ str(edad4))

# verificar_mayor(48, 48, 45, 45)
# verificar_mayor(65, 58, 45, 65)
verificar_mayor(12, 3, 4, 6)
#----------------------------------------
#Algebra booleana
persona_edad = 21
semanas_cotizadas = 250
genero = 'F'

print( persona_edad >= 58 and semanas_cotizadas >= 255 and genero == 'F' )
#----------------------------------------
edad = 12

if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')
#--------------------------------------
opcion = input('Escribe la opción: ')

if opcion == '1':
    print('Escogio la opción 1')
elif opcion == '2':
    print('Escogio la opción 2')
elif opcion == '3':
    print('Escogio la opción 3')
elif opcion == '4':
    print('Escogio la opción 4')
elif opcion == '5':
    print('Escogio la opción 5')
else:
    print('Opción invalida')
    
------------------------------------------

autos = {'autos':{
        1:{'marca':'Tesla',
           'modelos':{
               1:'Model S',
               2:'Model E',
               3:'Model X',
               4:'Model Y',
               }
           },
        2:{'marca':'Toyota',
           'modelos':{
               1:'Fortuner',
               2:'Prado',
               3:'Tundra',
               4:'Corola',
               }
           },
        3:{'marca':'Range Rover',
           'modelos':{
               1:'Evoque',
               2:'Defender',
               }
           },
        4:{'marca':'Mazda',
           'modelos':{
               1:'Mazda 3',
               2:'Mazda 2',
               3:'CX 30',
               }
           },
        5:{'marca':'Audi',
           'modelos':{
               1:'A7',
               2:'A5',
               3:'A3',
               }
           }
        }
        }
m1 = len(autos['autos'][1]['modelos'])
m2 = len(autos['autos'][2]['modelos'])
m3 = len(autos['autos'][3]['modelos'])
m4 = len(autos['autos'][4]['modelos'])
m5 = len(autos['autos'][5]['modelos'])


print(m1, m2, m3, m4, m5)
#-------------------------------------------
diccionario = {'nombre1':'Marco', 
               'edad1':31, 
               'lenguajes':{1:'Python',
                            2:'C++',
                            3:'Java',
                            4:'PHP',
                            5:'JavaScript',
                            6:'C#'}
               }
print(len(diccionario['lenguajes']))
#--------------------------------------
diccionario = {'clave':'valor'}
diccionario = {'nombre1':'Marco', 
               'edad1':31, 
               'lenguajes':{1:'Python',
                            2:'C++',
                            3:'Java',
                            4:'PHP',
                            5:'JavaScript',
                            6:'C#'}
               }
print(diccionario['lenguajes'])

#-------------------------------------------------------------------------------------------------------------------
edad = 58
genero = 'F'
semanas = 240

if genero == 'F':
    if edad >= 58:
        if semanas >= 250:
            print('Se puede pensionar')
        else:
            print('Le faltan '+str( 250 - semanas ) +' semanas')
    else:    
        print('Le faltan '+str( 58 - edad ) +' años')
elif genero == 'M':
    if edad >= 60:
        if semanas >= 255:
            print('Se puede pensionar')
        else:
            print('Le faltan '+str( 255 - semanas ) +' semanas')
    else:    
        print('Le faltan '+str( 60 - edad ) +' años')
else:
    print('Genero no valido')
#------------------------------------------------------------------
def verificar_mayor(edad1, edad2, edad3, edad4):
    if edad1 > edad2 and edad1 > edad3 and edad1 > edad4:
        print('1 '+ str(edad1))
    elif edad2 > edad3 > edad4:
        print('2 '+ str(edad2))
    elif edad3 > edad4:
        print('3 '+ str(edad3))
    else:
        print('4 '+ str(edad4))

# verificar_mayor(48, 48, 45, 45)
# verificar_mayor(65, 58, 45, 65)
verificar_mayor(12, 3, 4, 6)
#----------------------------------------
#Algebra booleana
persona_edad = 21
semanas_cotizadas = 250
genero = 'F'

print( persona_edad >= 58 and semanas_cotizadas >= 255 and genero == 'F' )
#----------------------------------------
edad = 12

if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')
#--------------------------------------
opcion = input('Escribe la opción: ')

if opcion == '1':
    print('Escogio la opción 1')
elif opcion == '2':
    print('Escogio la opción 2')
elif opcion == '3':
    print('Escogio la opción 3')
elif opcion == '4':
    print('Escogio la opción 4')
elif opcion == '5':
    print('Escogio la opción 5')
else:
    print('Opción invalida')
    
------------------------------------------
