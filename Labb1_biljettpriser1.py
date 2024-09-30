#Emilia Thudén Fredriksson och Sara Pirkhidran. 30 Sep 2024
#Vi utgår från en student som är äldre än 20 år.
enkelbiljett = 26
månadsbiljett = 650

reseantal = input("Hur många gånger i månaden reser du i kollektivtrafiken?")

pris_enkelbiljetter = int(reseantal)*enkelbiljett
pris_månadsbiljett = månadsbiljett

if pris_enkelbiljetter < pris_månadsbiljett:
    print("Det billigatse alternativet är att köpa enkelbiljetter till varje resa")
else:
    print("Det billigatse alternativet är att köpa en månadsbiljett")
#För reseantal = 2 ges output "Det billigatse alternativet är att köpa enkelbiljetter till varje resa"
#För reseantal = 456 ges output "Det billigatse alternativet är att köpa en månadsbiljett"

    
