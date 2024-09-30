#Emilia Thudén Fredriksson och Sara Pirkhidran. 30 Sep 2024

kategori = input("Vilken kategori tillhör du? rabatterad, ordinarie eller skolungdom?")
reseantal = input("Hur många gånger i månaden reser du i kollektivtrafiken?")

enkelbiljetter_rabatterad = 26
månadsbiljett_rabatterad = 650
enkelbiljetter_ordinarie = 42
månadsbiljett_ordinarie = 1020

#enkelbiljetter_skolungdom = enkelbiljetter_rabatterad
#månadsbiljett_skolungdom = månadsbiljett_rabatterad


pris_enkelbiljetter_rabatterad = (int(reseantal)*enkelbiljetter_rabatterad)
pris_enkelbiljetter_ordinarie = (int(reseantal)*enkelbiljetter_ordinarie)


if kategori == "rabatterad" or kategori == "skolungdom" and pris_enkelbiljetter_rabatterad < månadsbiljett_rabatterad:
    print("Köp enkelbiljetter för",pris_enkelbiljetter_rabatterad, "kr")
elif kategori == "rabatterad" or kategori == "skolungdom" and pris_enkelbiljetter_rabatterad > månadsbiljett_rabatterad:
    print("Köp månadsbiljett för", månadsbiljett_rabatterad, "kr")
elif kategori == "ordinarie" and pris_enkelbiljetter_ordinarie < månadsbiljett_ordinarie:
    print("Köp enkelbiljetter för", enkelbiljetter_ordinarie, "kr")
elif kategori == "ordinarie" and pris_enkelbiljetter_ordinarie > månadsbiljett_ordinarie:
    print("Köp månadsbiljett för",månadsbiljett_ordinarie, "kr")
else:
    print("Testa igen")
