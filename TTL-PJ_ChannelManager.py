'''
Autor:  Arko Annuk

Majutus teenust pakkuvad ettevõtted peavad maksimaalse käibe saavutamiseks turundama enda teenust mitmetes kanalites (AirBnB, Booking, jne).
Selleks, et järgida kõiki tehtavaid broneeringuid, on vaja nn. "channel manager"'i. 

Antud projekti raames loon primitiivse channel manageri, kus saab sisestada broneeringute infot ja vaadelda nende arvu.
Programmi toetab tkinteri põhjal loodud graafikaliides.

Programmi põhi funktsioonid:
* Uute broneeringute sisestamine
* Broneeringute arvu vaatlemine

Broneeringute arvu vaatlemiseks valitavad sätted:
1. Aasta
2. Kuu
3. Kanal
''' 

#Vajalikud moodulid
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
import tkinter.font as font


booking_count = 0
pay_total = 0
receive_total = 0
channel_cut = 0

'''------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------BRONEERINGUTE_LISAMIS_AKEN---------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------'''

def window_add_present():
#Broneeringu adndmete lisamis aken, selle tiitel ja mõõdud
    window_add = Tk()
    window_add.geometry('260x350')
    window_add.title("Bookings")

#Silt ja tekstiväli broneeringu teinud nime jaoks
    label_name = Label(window_add, text='\n Name')
    label_name.grid(column=0, row=0)
    name = Entry(window_add,width=30)
    name.grid(column=0, row=1)

#Silt ja valikvastusega lünk sooritatud broneeringu kanali jaoks
    label_channels = Label(window_add, text='Channel')
    label_channels.grid(column=0, row=2)

    channels_options = ['AirBnB', 'Booking', 'Other']
    channels = Combobox(window_add, values=channels_options, width=30)
    channels.grid(column=0, row=3)

#Silt ja tekstiväli check-in kuupäeva jaoks
    label_checkin = Label(window_add, text='\n Check-In (MM/DD/YYYY)')
    label_checkin.grid(column=0, row=4)
    checkin = Entry(window_add,width=30)
    checkin.grid(column=0, row=5)

#Silt ja tekstiväli check-out kuupäeva jaoks
    label_checkout = Label(window_add, text='Check-Out (MM/DD/YYYY)')
    label_checkout.grid(column=0, row=6)
    checkout = Entry(window_add,width=30)
    checkout.grid(column=0, row=7)

#Silt ja tekstiväli broneerija poolt makstud summa jaoks
    label_guestpay = Label(window_add, text='\n Amound Paid by Guest (€)')
    label_guestpay.grid(column=0, row=8)
    guestpay = Entry(window_add,width=30)
    guestpay.grid(column=0, row=9)

#Silt ja tekstiväli majutajale kättesaadud summa jaoks
    label_hostreceive = Label(window_add, text='Amound Received for Host (€)')
    label_hostreceive.grid(column=0, row=10)
    hostreceive = Entry(window_add,width=30)
    hostreceive.grid(column=0, row=11)

#Salvestus nupu funktsioon, mis kirjutab andmed faili ning küsib kas sisestada uued andmed või programm sulgeda
    def button_save_action():
        booking_file = open('bookingEntries.txt', 'a') #Andmeid hakatakse kirjutama ühte faili

    #Hakkan failile kirjutama lünkadesse lisatud teksti
        booking_text = ''
        booking_text += ((name.get())+',')
        booking_text += ((channels.get())+',')
        booking_text += ((checkin.get())+',')
        booking_text += ((checkout.get())+',')
        booking_text += ((guestpay.get())+',')
        booking_text += ((hostreceive.get())+',')
        booking_text += ('\n')
        booking_file.write(booking_text)
        booking_file.close()
        
    #Salvestus nupu järgne jah/ei küsimuse aken
        answer = messagebox.askyesno(title='Booking Saved', message='Submit another?')
        if answer == False:
            window_add.destroy()
        elif answer == True:
            window_add.destroy()
            return window_add_present()
        
#Salvestus nupp, mis salvestab sisestatud andmed faili ja toob esile akna
    label_emptyline = Label(window_add, text='')
    label_emptyline.grid(column=0, row=14)
    button_save = Button(window_add, text="Save", command=button_save_action)
    button_save.grid(column=0, row=15)

# kuvan akna ekraanile
    window_add.mainloop()
    
'''------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------VALIKUTE_VÄLI------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------'''
    
#Broneeringu programmi põhi aken, selle tiitel ja mõõdud
window_main = Tk()
window_main.geometry('330x300')
window_main.title("Bookings")

#Tühi rida kujundamaks sektsiooni algust
label_emptyline = Label(window_main, text='')
label_emptyline.grid(column=0, row=0)

#Silt ja valikvastusega lünk vaadeldava aasta jaoks
label_channel = Label(window_main, text='Channel')
label_channel.grid(column=0, row=3)

channels = ['All', 'AirBnB', 'Booking', 'Other']
select_channel = Combobox(window_main, values=channels, width=10)
select_channel.grid(column=0, row=4)

#Silt ja valikvastusega lünk vaadeldava kuu jaoks
label_month = Label(window_main, text='Month')
label_month.grid(column=1, row=3)

months = ['All','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
select_month = Combobox(window_main, values=months, width=10)
select_month.grid(column=1, row=4)

#Silt ja valikvastusega lünk vaadeldava aasta jaoks
label_year = Label(window_main, text='Year')
label_year.grid(column=2, row=3)

months = ['All', '2019', '2020', '2021', '2022']
select_year = Combobox(window_main, values=months, width=10)
select_year.grid(column=2, row=4)

'''--------------------------------------------BRONEERINGU_ARVU_FUNKTSIOONID-----------------------------------------------------'''

#Funktsioon kutsumaks read, mis vastavad valitud aastale

def return_year_lines():
    booking_file = open('bookingEntries.txt', 'r')
    year_lines = [line.strip('\n') for line in booking_file.readlines()]
    year_lines_selected = []
    if select_year.get() == 'All':
        year_lines_selected = [line for line in year_lines]
        return year_lines_selected
    elif len(select_year.get()) == 4:
        year_lines_selected = [line for line in year_lines if select_year.get() in line]
        return year_lines_selected
    elif select_year.get() == '':
        return year_lines_selected
    


#Funktsioon leidmaks kuud järiendi elementidest vastavalt aastale       
def find_months():
    month_lines = return_year_lines()
    if month_lines == []:
        return month_lines_cut
    else:
        checkin_lines = [string.split(',')[2] for string in month_lines]
        month_lines_cut = [checkin[0:2] for checkin in checkin_lines]
        return month_lines_cut

#Funktsioon kutsumaks read, mis vastavad valitud aastale ja kuule
def return_month_lines():
    month_lines = return_year_lines()
    month_lines_selected = []
    if month_lines == []:
        return month_lines_selected
    elif select_month.get() == 'All':
        month_lines_selected = [line for line in month_lines]
        return month_lines_selected
    elif len(select_month.get()) == 2:
        month_indices = [index for index, month in enumerate(find_months()) if month == select_month.get()]
        for index in month_indices:
            month_lines_selected.append(month_lines[index])
        return month_lines_selected

#Funktsioon kutsumaks read, mis vastavad valitud aastale, kuule ja kanalile
def return_channel_lines():
    return_month_lines()
    channel_lines = return_month_lines()
    channel_lines_selected = []
    if channel_lines == []:
        return channel_lines_selected
    elif select_channel.get() == 'All':
        channel_lines_selected = [line for line in channel_lines]
        return channel_lines_selected
    elif len(select_channel.get()) >= 1:
        channel_lines_selected = [line for line in channel_lines if select_channel.get() in line]
        return channel_lines_selected

#Salvestus nupu funktsioon, mis uuendab andme väljade muutujaid vastavalt valitud sättedele
def button_show_action():
    global booking_count
    
    #Nupu vajutusel tühjendab teksti välja
    label_bookings_total = Label(window_main, text='                           ', font = labelFont2)
    label_bookings_total.grid(column=1, row=8)
    
    if return_channel_lines() == None:
        booking_count = 0
        label_bookings_total = Label(window_main, text='Reservations: 0', font = labelFont2)
        label_bookings_total.grid(column=1, row=8)              
    elif return_channel_lines() == []:
        booking_count = 0
        label_bookings_total = Label(window_main, text='Reservations: 0', font = labelFont2)
        label_bookings_total.grid(column=1, row=8)
    else:
        for line in return_channel_lines():
            booking_count += 1
            label_bookings_total = Label(window_main, text='Reservations: '+ str(booking_count), font = labelFont2)
            label_bookings_total.grid(column=1, row=8)
        booking_count = 0
    
#Nupp, mis esitab vastava kuu ja aasta broneeringute andmed
label_emptyline = Label(window_main, text='')
label_emptyline.grid(column=0, row=5)
button_addbooking = Button(window_main, text="Show", command=button_show_action)
button_addbooking.grid(column=1, row=6)


'''--------------------------------------------------ANDMETE_VÄLI--------------------------------------------------------------'''

#Sektsiooni eraldav riba
label_emptyline = Label(window_main, text='\n')
label_emptyline.grid(column=0, row=7)
seperator_line = ttk.Separator(window_main,orient='horizontal').grid(column=0, row=7, columnspan=3, sticky='ew')

#Fonti stiil, mida lisan lünkadele, mida selles programmi versioonis täita ei jõudnud
labelFont1 = font.Font(overstrike=1)

#Silt näitamaks broneeringute arvu
labelFont2 = font.Font(size=12)
label_bookings_total = Label(window_main, text='Reservations: '+ str(booking_count), font = labelFont2)
label_bookings_total.grid(column=1, row=8)
 
#Silt näitamaks aja vältel klinedi poolt makstub raha summat
label_guestpay_total = Label(window_main, text='Guests: '+ str(pay_total)+'€', font = labelFont1)
label_guestpay_total.grid(column=1, row=9)    
 
#Silt näitamaks aja vältel majutajale laekunud raha summat
label_hostreceive_total = Label(window_main, text='Host: '+ str(receive_total)+'€', font = labelFont1)
label_hostreceive_total.grid(column=1, row=10)

#Silt näitamaks kanali vahendustasu protsenti
label_channelcut = Label(window_main, text='Channel Cut: '+ str(channel_cut)+'%', font = labelFont1)
label_channelcut.grid(column=1, row=11)

#Sektsiooni eraldav riba
label_emptyline = Label(window_main, text='\n')
label_emptyline.grid(column=0, row=12)
seperator_line = ttk.Separator(window_main,orient='horizontal').grid(column=0, row=12, columnspan=3, sticky='ew')

#Nupp, mis avab uue broneeringu andme salvestus akna
button_addbooking = Button(window_main, text="Add", command=window_add_present)
button_addbooking.grid(column=1, row=13)

#kuvan akna ekraanile
window_main.mainloop()

#bookingEntries.txt sample entries
''' 
Arko Annuk,Booking,12/10/2021,12/14/2021,60.12,52.12,
Randy Lahey,AirBnB,12/12/2020,12/14/2020,560.1,340.63,
Barbara Lahey,Booking,12/10/2021,12/14/2021,60.12,52.12,
John Stan,Booking,12/10/2019,12/14/2019,60.12,52.12,
Sam Samson,Booking,10/06/2020,10/07/2020,60.12,52.12,
Eric Crimson,Booking,10/06/2020,10/07/2020,60.12,52.12,
Arko Annuk,Booking,12/10/2021,12/14/2021,60.12,52.12,
Randy Lahey,AirBnB,12/12/2020,12/14/2020,560.1,340.63,
Barbara Lahey,Booking,12/10/2021,12/14/2021,60.12,52.12,
John Stan,Booking,12/10/2019,12/14/2019,60.12,52.12,
Sam Samson,Booking,10/06/2020,10/07/2020,60.12,52.12,
Eric Crimson,Booking,01/06/2020,10/07/2020,60.12,52.12,
Arko Annuk,Booking,06/10/2021,12/14/2021,60.12,52.12,
Randy Lahey,AirBnB,12/12/2020,12/14/2020,560.1,340.63,
Barbara Lahey,Booking,12/10/2021,12/14/2021,60.12,52.12,
John Stan,Other,12/10/2019,12/14/2019,60.12,52.12,
Sam Samson,Booking,10/06/2020,10/07/2020,60.12,52.12,
Eric Crimson,Booking,08/06/2020,10/07/2020,60.12,52.12,
Arko Annuk,Booking,07/10/2021,12/14/2021,60.12,52.12,
Randy Lahey,AirBnB,05/12/2020,12/14/2020,560.1,340.63,
Barbara Lahey,Booking,04/10/2021,12/14/2021,60.12,52.12,
John Stan,Booking,03/10/2019,12/14/2019,60.12,52.12,
Sam Samson,Booking,02/06/2020,10/07/2020,60.12,52.12,
Eric Crimson,Booking,01/06/2020,10/07/2020,60.12,52.12,
Sam Sammyson,Other,04/20/2021,04/25/2021,30.24,20.12,
Mate Mateson,Other,09/03/2022,24/03/2022,631.23,580.13,
'''

