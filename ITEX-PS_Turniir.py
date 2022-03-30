def loe_seis(fail):
    with open(fail) as f:
        next(f)
        seis = {}
        for line in f:
            line = line.split()
            seis[line[0]] = line[1:]
    return seis

seis = loe_seis('turniir.txt')

def lisa_tulemus(nimi, voor, sonastik, tulemus):
    
    skoorid = seis[nimi]
    
    if skoorid[voor] == '-':
        seis[nimi].pop(voor)
        seis[nimi].insert(voor, str(tulemus))
        print ('Tulemus lisatud')
    else:
        print ('Tulemus on juba varem lisatud!')
    
def leia_skoor(nimi, sonastik):
    skoorid = [a for a in seis[nimi] if a.isnumeric()]
    skoorid = sum([int(a) for a in skoorid])
    return skoorid
            
def leia_voitija(sonastik):
    skoorid_max = {}
    for key in seis.keys():
         #print (key, (leia_skoor(key, seis)))
        skoorid_max[key] = leia_skoor(key, seis)
        skoor_max = max(skoorid_max, key=skoorid_max.get)
    voitija_nimi = (skoor_max)
    voitija_punktid = (skoorid_max[skoor_max])
    print ('Suurima skooriga on', voitija_nimi, '('+ str(voitija_punktid)+' punkti).')
           
#leia_skoor('Mari', seis)
    
#lisa_tulemus('Mari', 4, seis, 0)
def play_code():
    tegevus = input('''Vali tegevus:
    1 - Vaata punktitabelit
    2 - Lisa tulemus
    3 - Vaata skoori
    4 - Leia voitja
    5 - Lopeta programmi too
    ''')
    if tegevus == '1':
        for key, value in seis.items():
            value=' '.join(map(str,value))
            print (key, value)
        return play_code()
    elif tegevus == '2':
        nimi = input('Sisesta nimi: ')
        voor = int(input('Sisesta voor: '))
        tulemus = input('Sisesta punktid: ')
        lisa_tulemus(nimi, voor, seis, tulemus)
        return play_code()
    elif tegevus == '3':
        nimi = input('Sisesta nimi: ')
        print(nimi, 'skoor oli', str(leia_skoor(nimi, seis))+'.')
        return play_code()
    elif tegevus == '4':
        leia_voitija(seis)
        return play_code()
    else:
        print ('Programm lõpetas töö.')

play_code()
        
'''Turniir.txt
     1 2 3 4 5 6
Mari 2 4 5 - 1 4
Juku 1 3 2 7 8 -
Malle - 2 - 3 2 5
Kalle 4 6 - - 2 -
'''