# HANGMAN - AHORCADO
lives = 5
word = "COHETE"
word = list(word.lower())
nletters = len(word)
game = "_"*nletters
game = list(game)
answer = "".join(word)
#print(word)
#print(nletters)
print()

print("--------------------------------------------------------------------")
print("                              HANGMAN                               ")
print("--------------------------------------------------------------------")
print()
print("Tienes {} vidas".format(lives))
print()
print(game)
print("--------------------------------------------------------------------")
print()

# Funciones
def lesslives():
    global lives
    lives -= 1
    return lives

cont = -1
find = 0
aux_find = 0

while lives > 0 and find < nletters:
    print()
    l_player = input("Ingrese una letra: ")
    l_player = l_player.lower()
    print()
    for i in word:
        cont += 1
        if i == l_player:
            game[cont] = l_player
            find += 1
            aux_find += 1

    if aux_find == 0:
        lesslives()

    cont = -1
    aux_find = 0
    print(game)
    print()
    print("Te quedan {} vidas".format(lives))
    print("--------------------------------------------------------------------")

print()
print()

if lives > 0 and find == nletters:
    print("¡Felicidades has ganado la partida 🎉🏆! La palabra era \"{}\"".format(answer))
else:
    print("Lo sentimos has perdido esta partida 😭 La palabra era \"{}\"".format(answer))
