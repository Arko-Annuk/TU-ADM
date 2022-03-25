f = open('parkla.txt', 'r')
parkla_nimed = {}

#Parking list
parkla= []
for line in f:
    stripped_line= line.strip()
    line_list = [str(i) for i in stripped_line]
    parkla.append(line_list)
print (parkla)

#uus parkimine
def uus_parkimine():
    nimi = input('Palun sisestage parkija nimi: ')
    kordinaadid = input('Palun sisesta parkimiskoha kordinaadid: ')
    
#Parking location return
    kord = [int(i) for i in kordinaadid]
    koht = parkla[kord[0]][kord[1]]
    
#Save available parking spot to dic
    if koht == 'P':
        parkla_nimed[nimi] = kord
        parkla[kord[0]][kord[1]] = 'X'
        return parkla
    else:
        print ('Sellele parkimiskohale parkida ei saa')

#parkija asukoha leidmine
def parkimis_koht():
    nimi = input('Palun sisestage parkija nimi: ')
    return (parkla_nimed[nimi])
    
#parkimise lõpetamine
def parkimis_lopp():
    nimi = input('Palun sisestage parkija nimi: ')
    park_in = parkla_nimed[nimi]
    parkla[park_in[0]][park_in[1]] = 'P'
    return parkla
    
def parkimis_seis():
    print (parkla)

def programm():
    action = int(input('Palun valige tegevus: '))
    if action == 1:
        uus_parkimine()
        return programm()
    elif action == 2:
        print (parkimis_koht())
        return programm()
    elif action == 3:
        parkimis_lopp()
        return programm()
    elif action == 4:
        parkimis_seis()
        return programm()
    elif action == 5:
        print (parkla)
        
        #Kirjutab faili uue seisu
        with open('parkla.txt', 'w') as file:
            file.seek(0)
            for item in parkla:
                file.write(''.join(map(str,item)))
                file.write('\n')
            file.truncate()
        
        
        print ('Programm kirjutas seisu faili ja lõpetas töö')

programm()
    
#parkla.txt
'''
PPPP-P
-----P
PPPP-P
'''