def chooseOptions():
  import random
  optionVerify=True

  options = ('piedra', 'papel', 'tijera')

  #User choosing
  while optionVerify:
    print("Ingresa tu elección")
    userOption = input("Piedra, Papel o Tijera: ")
    userOption = userOption.lower()
    #validation
    if userOption in options:
      optionVerify=False
    else:
      print(f"'{userOption}' no es una opción válida. Intenta de nuevo por favor.")
      print("")

  #Machine choosing
  machineOption = random.choice(options)

  #Messages
  print("💪 ->", userOption)
  print("🦾 ->", machineOption)
  #results
  #results
  return userOption, machineOption


def cheeckRules(uo, mo, uw, mw):
  if uo == mo:
    print("¡¡EMPATE!!")
  elif (uo == 'piedra' and mo == 'tijera') or (uo == "papel" and mo == "piedra") or (uo == "tijera" and mo =="papel"):
    uw += 1
    print("Gana el usuario")
    print("")
  else:
    mw += 1
    print("Gana la computadora")
    print("")
 
  return uw, mw


def runGame():
  userWin = 0
  machineWins = 0
  rounds = 1

  while True:
    print("*" * 20)
    print("Round", rounds)
    print("*" * 20)
    print("")
    print("User", userWin, "|", machineWins, "Machine")
    print("")
    rounds += 1
    userOption, machineOption = chooseOptions()
    userWin, machineWins = cheeckRules(userOption, machineOption, userWin,
                                       machineWins)
    if userWin == 2:
      print("¡USER WIN!")
      break
    elif machineWins == 2:
      print("¡MACHINE WIN!")
      break


runGame()