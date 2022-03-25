import random

#Kapid List
kapid = []

f = open('kapid.txt', 'r')
for line in f:
    stripped_line = line.strip()
    line_list = stripped_line.split(',')
    kapid.append(line_list)
print (kapid)

#Uksekoodid Dict
uksekoodid_list = []
for line in open('uksekoodid.txt', 'r'):
    uksekoodid_list.append(line.strip().split(','))
    
uksekoodid = {}

for line in uksekoodid_list:
    key = line[0]
    value = line[1:]
    uksekoodid[key] = value

#Saadetise kattesaamine
def saadetise_kattesaamine():
    kood = input('Palun sisestage uksekood ')
    if kood in uksekoodid:
        uksekood = [int(i) for i in uksekoodid[kood]]
        print ('Avaneb kapp '+ str(tuple(uksekood))+', milles on '+ kapid[uksekood[0]][uksekood[1]])
        kapid[uksekood[0]][uksekood[1]] = '-'
        del uksekoodid[kood]
        return uksekoodid

    else:
        print ('Sellist uksekoodi ei ole.')

#Tuhjad kapid
def tuhjad_kapid_arv():
    tuhi_kapp = 0
    for el in kapid:
        for i in el:
            if i == '-':
                tuhi_kapp+=1
    return tuhi_kapp
    #tuhi_kapp = 0
    
#Saadetise saatmine
def saadetise_saatmine():
    if tuhjad_kapid_arv() != 0:
        saadetis = input('Mida tahate saata? ')
        nimi = input('Kellel saata tahate? ')        
        
        #Kapi listi muudatus
        kiri_indexes = [(i, kapp.index('-')) for i, kapp in enumerate(kapid) if '-' in kapp]
        saad_index = kiri_indexes[0]
        kapid[saad_index[0]][saad_index[1]] = saadetis

        #Uksekoodi genereerimine

        kood = str(random.randint(1000,9999))
        while kood in uksekoodid.keys():
            kood = str(random.randint(1000,9999))
        else:
            uksekoodid[kood] = list(saad_index)

        print ('Sõnum postifirmale: Kapis '+ str(saad_index) +' on kiri, mis saadeti ' + nimi +'.')
        return (kapid)
           
    else:
        print ('Tuhje kappe ei ole')

#Programm kokku
def programmi_too():
    tegevus = input('Palun valige tegevus: ')
    if tegevus == '1':
        saadetise_kattesaamine()
        print (kapid)
        print (uksekoodid)
        return programmi_too()
    elif tegevus == '2':
        print ('Praegu on '+ str(tuhjad_kapid_arv()) +' tuhja kappi')
        return programmi_too()
    elif tegevus == '3':
        saadetise_saatmine()
        print (kapid)
        print (uksekoodid)
        return programmi_too()
    
programmi_too()

#uksekoodid.txt
'''
0132,0,1
9142,0,3
8112,0,4
4444,1,0
5131,1,4
0000,2,4
'''

#kapid.txt
'''
-,kiri,-,pakk,kiri
pakk,-,-,-,pakk
-,-,-,-,pakk
'''

