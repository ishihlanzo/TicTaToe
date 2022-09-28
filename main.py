import tkinter

root = tkinter.Tk()

player = ["x", "o"]

grille = [[0,0,0],
          [0,0,0],
          [0,0,0]]

def verif_win():
    for i in range(3):
        if (grille[i][0] == grille[i][1] == grille[i][2]) and grille[i][0] in player:
            player_turn.config(text = f"player\n{grille[i][0]}\nwin !")
    for i in range(3):
        if (grille[0][i] == grille[1][i] == grille[2][i]) and grille[0][i] in player:
            player_turn.config(text = f"player\n{grille[0][i]}\nwin !")
    if (grille[0][0] == grille[1][1] == grille[2][2]) and grille[0][0] in player:
        player_turn.config(text = f"player\n{grille[0][0]}\nwin !")
    if (grille[0][2] == grille[1][1] == grille[2][0]) and grille[0][2] in player:
        player_turn.config(text = f"player\n{grille[0][2]}\nwin !")
    


def user_play(coord) :
    if player_turn.cget("text") == "o" or player_turn.cget("text") == "x":
        case[coord].grid_forget()
        play[coord].config(text = player_turn.cget("text"))
        if player_turn.cget("text") == "o" :
            player_turn.config(text="x")
            grille[coord[0]][coord[1]] = "o"
        elif player_turn.cget("text") == "x" :
            player_turn.config(text="o")
            grille[coord[0]][coord[1]] = "x"
        for i in range(3) :
            print(grille[i]) 
        verif_win()


play = {}
for i in range(3) :
    for j in range(3) :
        play[(i,j)] = tkinter.Label(root)
        play[(i,j)].grid(row = i, column=j, ipadx = 6, ipady = 3)


case = {}
for i in range(3) :
    for j in range(3) :
        case[(i,j)] = tkinter.Button(root, command = lambda x = (i, j): user_play(x))
        case[(i,j)].grid(row = i, column=j, ipadx = 6)

player_turn = tkinter.Label(root, text = player[0])
player_turn.grid(row = 1, column=4)



root.mainloop()
