stroka = str(input("Напишите строку: ")) #запрос на введение строки
all_glasn = "ауоиэыяюеёАУОИЭЫЯЮЕЁ" #список всех гласных 
all_soglasn =  "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЦ" #список всех согласных
glasn = 0 
soglasn = 0
for i in stroka: # Цикл фор
  if i in all_glasn: 
        glasn +=1 #определяется кол-во гласных
  elif i in all_soglasn:
        soglasn +=1 #определяется кол-во согласных
print(f"длина строки {len(stroka)}") #вывод кол-во длины строки
print(f"кол-во гласных {glasn}")#вывод кол-во гласных строки
print(f"кол-во согласных {soglasn} ")#вывод кол-во согласных строки
