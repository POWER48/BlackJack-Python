from tkinter import *
import random
import sys
sys.setrecursionlimit(10000)

def variables_in_txt(money_old,money):

    #read input file
    fin = open("Save/Save.txt", "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace(str(money_old),str(money))
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open("Save/Save.txt", "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()




def Set_money():

    global money

    fin = open("Save/Save.txt", "rt")

    data = fin.read()

    money = int(data)


    
def cartes_with_value():

    cartes=[["As",(11,1)],("2",2),("3",3),("4",4),("5",5),("6",6),("7",7),("8",8),("9",9),("10",10),("V",10),("D",10),("R",10)]

    return cartes






def create_pot():
    global pot

    pot=[]
    
    for i in range(4):

        pot.append(cartes_with_value())

        for j in range(len(pot[i])):

            if i==0:
                pot[i][j]= (pot[i][j],"♣.gif")

            elif i==1:
                pot[i][j]= (pot[i][j],"♦.gif")

            elif i==2:
                pot[i][j]= (pot[i][j],"♠.gif")

            elif i==3:
                pot[i][j]= (pot[i][j],"♥.gif")



    return pot




def somme(hand):

    somme=0
    cpt=0


    for i in range(len(hand)):


        if hand[i][0][1]== (11, 1):

            somme= hand[i][0][1][0] + somme
            cpt+=1


        else:

            somme=somme + hand[i][0][1]




    if somme > 21:
        somme=somme-10*cpt




    return somme


def tirer(hand,frame):
    global pot

    a=random.randint(0,len(pot)-1)

    total=0

    for i in range(0, len(pot)):
        total=total+len(pot[i])
    
    if total==0:
        pot = create_pot()
        

    while len(pot[a]) == 0:
        a=random.randint(0,len(pot)-1)
        

    b=random.randint(0,len(pot[a])-1)

    hand.append(pot[a][b])




    img = PhotoImage(file='cards/{}_{}'.format(pot[a][b][0][0],pot[a][b][1]))



    label= Label(frame,image=img, relief="raised")

    label.umage= img

    label.pack(side="left")


    del pot[a][b]

    dealer_score_label.set(somme(dealer_hand))

    player_score_label.set(somme(player_hand))



    if somme(player_hand)> 21:
        result_text.set("Player Bust "+ " Your money: " + str(money) + "€")

        mainWindow.after(2000,lambda: mise_depart())
        button_frame.grid_forget()



    return hand





def blackjack(somme_dealer,somme_player):
    global mise_int
    global money
    global money_old

    if somme_player == 21:

        money_old= money        
        money= money+(mise_int)*3
        variables_in_txt(money_old,money)

        result_text.set("Player wins!, Black Jack Good One ! "+ " Your money: " + str(money) + "€")

        mainWindow.after(2000,lambda: mise_depart())
        button_frame.grid_forget()





def dealer_turn():
    global money
    global mise_int
    global money_old

    while somme(dealer_hand) < somme(player_hand):
        tirer(dealer_hand,dealer_card_frame)

    if somme(dealer_hand) > somme(player_hand) and somme(dealer_hand)<22:
        result_text.set("Dealer wins! "+ "Your money: " +str(money) + "€")







    elif somme(dealer_hand)>21:
        money_old= money
        money= money+(mise_int)*2
        variables_in_txt(money_old,money)
        result_text.set("Player wins! "+ " Your money: " + str(money) + "€")



    elif somme(player_hand)>21:
        result_text.set("Player Loose! "+ " Your money: " + str(money) + "€")

    elif somme(dealer_hand) == somme(player_hand):
        money_old= money
        money= money+mise_int
        variables_in_txt(money_old,money)
        result_text.set("PUSH! "+ " Your money: " + str(money) + "€")







    button_frame.grid_forget()

    mainWindow.after(3000,lambda:mise_depart())



def mise_depart():

    global mise_int

    mise_int=0

    mise_text.set(mise_int)

    dealer_score_label.set(0)

    player_score_label.set(0)

    button_frame.grid_forget()
    mise_frame.grid(row=4, column=1, columnspan=3, sticky='w')

    if mise_int == 0:
        play_button.grid_forget()


    global dealer_card_frame
    global player_card_frame



    dealer_card_frame.destroy()
    dealer_card_frame = Frame(card_frame, bg="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    # embedded frame to hold the card images
    player_card_frame.destroy()
    player_card_frame = Frame(card_frame, bg="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)





    # embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = Frame(card_frame, bg="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    # embedded frame to hold the card images
    player_card_frame.destroy()
    player_card_frame = Frame(card_frame, bg="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)





    result_text.set("Good Luck, Your money: ")
    text = result_text.get()

    result_text.set("Good Luck, Your money: "+ str(money)+ "€")






def new_game():
    button_frame.grid(row=3, column=1, columnspan=3, sticky='w')
    mise_frame.grid_forget()


    # Create the list to store the dealer's and player's hands
    

    global player_hand

    player_hand=[]

    global dealer_hand

    dealer_hand=[]

    dealer_hand= tirer(dealer_hand, dealer_card_frame)

    for i in range(2):
        player_hand = tirer(player_hand,player_card_frame)


    blackjack(somme(dealer_hand),somme(player_hand))

    mainWindow.mainloop()









def mise_down():

    global mise_int

    global money

    global money_old

    if mise_int <= 0:
        return mise_int

    money_old=money
    
    money= money +50

    variables_in_txt(money_old,money)

    mise_int = mise_int -50

    if mise_int == 0:
        play_button.grid_forget()

    result_text.set(text+ str(money) + "€")
    mise_text.set(mise_int)


    return mise_int


def mise_up():

    global mise_int

    global money

    global money_old

    if money == 0:
        return mise_int


    money_old= money

    money= money -50

    variables_in_txt(money_old,money)

    mise_int=mise_int + 50


    play_button.grid(row=0, column=5)

    result_text.set(text +str(money) + "€")

    mise_text.set(mise_int)


    return mise_int






mainWindow = Tk()

# Set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(bg="green")

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=0)
mainWindow.columnconfigure(4, weight=5)
mainWindow.columnconfigure(5, weight=0)


result_text = StringVar()
result = Label(mainWindow, textvariable=result_text,width=200)
result.grid(row=0, column=0, columnspan=3)

card_frame = Frame(mainWindow, relief="sunken", borderwidth=1, bg="black")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = IntVar()
Label(card_frame, text="Dealer", bg="black", fg="white").grid(row=0, column=0)
Label(card_frame, textvariable=dealer_score_label, bg="black", fg="white").grid(row=1, column=0)
# frame for image
dealer_card_frame = Frame(card_frame, bg="black")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = IntVar()

Label(card_frame, text="Player", bg="black", fg="white").grid(row=2, column=0)
Label(card_frame, textvariable=player_score_label, bg="black", fg="white").grid(row=3, column=0)

# frame for image
player_card_frame = Frame(card_frame, bg="black")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = Frame(mainWindow)
button_frame.grid(row=3, column=1, columnspan=3, sticky='w')


dealer_button = Button(button_frame, text="Stay", padx=5,command=dealer_turn)
dealer_button.grid(row=0, column=1)



player_button = Button(button_frame, text="Hit", padx=8,command=lambda:tirer(player_hand,player_card_frame))
player_button.grid(row=0, column=0)



#Mise tkinter:


mise_int=0

money = 0

Set_money()

money_old= money


mise_frame = Frame(mainWindow)
mise_frame.grid(row=4, column=1, columnspan=3, sticky='w')

mise_text = StringVar()
mise = Label(mise_frame, textvariable=mise_text,width=13)
mise.grid(row=0, column=2, columnspan=2)

mise_up_button= Button(mise_frame, text="+", padx=5,command=mise_up)
mise_up_button.grid(row=0, column=1)

mise_down_button = Button(mise_frame, text="  -  ",command=mise_down)
mise_down_button.grid(row=0, column=4)

play_button = Button(mise_frame, text=" OK",command=new_game)
play_button.grid(row=0, column=5)

if mise_int == 0:
        play_button.grid_forget()

mise_text.set(mise_int)

button_frame.grid_forget()



result_text.set("Good Luck, Your money: ")

text = result_text.get()

result_text.set("Good Luck, Your money: "+str(money)+ "€")


create_pot()

#Start new game + main loop

mainWindow.mainloop()









