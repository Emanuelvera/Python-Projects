import random
seguir = "si"
count_u = 0
count_c = 0
draw = 0

while seguir == "si":


  tuple = ["si","no"]
  options = ["piedra", "papel", "tijeras"]
  user = input("Elija, piedra, papel o tijeras =>")
  user = user.lower()

  if user not in options:
    print("esa no es una opcion valida")
    continue

  Computer = random.choice(options)
  print(".")
  print(".")
  print(".")
  print("Usted elegio =>", user)
  print(".")
  print(".")
  print(".")
  print (f"El opponente elijio => {Computer}")
  print(".")
  print(".")
  print(".")

  if user == Computer:
    draw +=1 
    print("♦♦♦ Es un empate ♦♦♦")

  elif user == "papel":
    if Computer == "piedra":
      count_u +=1
      print("Ganaste ♡⸜(˶˃ ᵕ ˂˶)⸝♡")
    else:
      count_c +=1
      print ("Perdiste ( • ᴖ • ｡)")

  elif user == "piedra":
    if Computer == "tijeras":
      count_u +=1
      print("Ganaste ♡⸜(˶˃ ᵕ ˂˶)⸝♡")
    else:
      count_c +=1
      print ("Perdiste ( • ᴖ • ｡)")

  elif user == "tijeras":
    if Computer == "papel":
      count_u +=1
      print("Ganaste ♡⸜(˶˃ ᵕ ˂˶)⸝♡")
    else:
      count_c +=1
      print ("Perdiste ( • ᴖ • ｡)")


  print(".")
  print(".")
  print(".")
  print(f"°--------------------°")
  print(f"|    Usuario   |  {count_u }  |")
  print(f"|              |     |")
  print(f"|  Computadora |  {count_c}  |")
  print(f"|              |     |")
  print(f"|    Empates   |  {draw}  |")
  print(f"|              |     |")
  print(f"°--------------------°")
  print(".")
  print(".")
  print(".")


  seguir = input("Quieres seguir jugando? ")
  seguir = seguir.lower()
  while seguir not in tuple:
    print(".")
    print("Esa no es una opcion valida, ingrese si o no...")
    print(".")
    seguir = input("Quieres seguir jugando? ")
    seguir = seguir.lower()