#Emilia Thudén Fredriksson och Sara Pirkhidran. 30 Sep 2024

#här får vi indata från användaren vi kan använda i programmet
kategori = input("Vilken kategori tillhör du? rabatterad, ordinarie eller skolungdom?")
reseantal = input("Hur många gånger i månaden reser du i kollektivtrafiken?")

#SL:s biljettpriser för enkel- respektive månadsbiljett i de olika priskategorierna
enkelbiljetter_rabatterad = 26
månadsbiljett_rabatterad = 650

enkelbiljetter_ordinarie = 42
månadsbiljett_ordinarie = 1020

#enkelbiljetter_skolungdom = enkelbiljetter_rabatterad
#månadsbiljett_skolungdom = månadsbiljett_rabatterad

#omvandla indata reseantal till ett heltal så att följande beräkningar kan genomföras
pris_enkelbiljetter_rabatterad = (int(reseantal)*enkelbiljetter_rabatterad)
pris_enkelbiljetter_ordinarie = (int(reseantal)*enkelbiljetter_ordinarie)

#om användaren reser med rabatterad biljett och priset för enkelbiljetter understiger 650 kronor:
if kategori == "rabatterad" or kategori == "skolungdom" and pris_enkelbiljetter_rabatterad < månadsbiljett_rabatterad:
    print("Köp enkelbiljetter för",pris_enkelbiljetter_rabatterad, "kr")
    print("Du sparar då: ", -(pris_enkelbiljetter_rabatterad-650), "kr")

#om användaren reser med rabatterad biljett och priset för enkelbiljetter överstiger 650 kronor:
elif kategori == "rabatterad" or kategori == "skolungdom" and pris_enkelbiljetter_rabatterad > månadsbiljett_rabatterad:
    print("Köp månadsbiljett för", månadsbiljett_rabatterad, "kr")
    print("Du sparar då: ", -(650-pris_enkelbiljetter_rabatterad), "kr")

#om användaren reser med ordinarie biljett och priset för enkelbiljetter understiger 1020 kronor:
elif kategori == "ordinarie" and pris_enkelbiljetter_ordinarie < månadsbiljett_ordinarie:
    print("Köp enkelbiljetter för", enkelbiljetter_ordinarie, "kr")
    print("Du sparar då: ", -(pris_enkelbiljetter_ordinarie-1020), "kr")

#om användaren reser med ordinarie biljett och priset för enkelbiljetter överstiger 1020 kronor:
elif kategori == "ordinarie" and pris_enkelbiljetter_ordinarie > månadsbiljett_ordinarie:
    print("Köp månadsbiljett för",månadsbiljett_ordinarie, "kr")
    print("Du sparar då: ", -(1020-pris_enkelbiljetter_ordinarie), "kr")

#för ogiltig indata
else:
    print("Du har angett ogiltiga värden. Testa igen.")

#för indata: kategori: ordinarie, resdata: 17 ges utdata: Köp enkelbiljetter för 42 kr Du sparar då:  306 kr
#för indata: kategori: skolungdom, resdata: 64 ges utdata: Köp månadsbiljett för 650 kr Du sparar då:  1014 kr
#för indata: kategori: bananfluga, resdata: 3 ges utdata: Du har angett ogiltiga värden. Testa igen.

