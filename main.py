stroka = str(input("Напишите строку: "))
all_glasn = "ауоиэыяюеёАУОИЭЫЯЮЕЁ"
all_soglasn =  "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЦ"
glasn = 0
soglasn = 0
for i in stroka:
  if i in all_glasn:
        glasn +=1
  elif i in all_soglasn:
        soglasn +=1 
print(f"длина строки {len(stroka)}")
print(f"кол-во гласных {glasn}")
print(f"кол-во согласных {soglasn} ")