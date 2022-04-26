def juurdekasv(pindala, kasv):
    tulemus = round(pindala * 0.4047 * kasv, 2)
    return tulemus

avatav_file = input('Sisestage failinimi: ')
f = open(avatav_file, 'r')


juurde_kasv = float(input('Sisestage aastane juurdekasv hektari kohta tihumeetrites: '))

alam_piir = float(input('Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võetakse: '))

arvutatud_metsad = 0

for rida in f:
    rida = float(rida)
    if rida > alam_piir:
        print ('Metsatüki aastane juurdekasv on', juurdekasv(rida, juurde_kasv))
        arvutatud_metsad += 1
    else:
        print ('Metsatükki ei võeta arvesse')

print ('Arvutati', arvutatud_metsad, 'metsatüki juurdekasv')