import random
win_possibility = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
choice_list = ["0","1","2","3","4","5","6","7","8"]
turn_number = 0
player_one = []
player_two = []
player1 = ""
player2 = ""
user_turn = 0
def user_rules():
    print("Welcome to tic tac toe")
    print("You must choose either X or O")
    print('Enter choices 0 through 8 to choose a position on the board')
    print('The first user to get 3 X/O in a row or diagonally WINS')
    print('Best of luck!')
def draw(x):
    print("{} | {} | {}".format(x[0],x[1],x[2]))
    print("_ | _ | _ ")
    print("{} | {} | {}  ".format(x[3],x[4],x[5]))
    print("_ | _ | _ ")
    print("{} | {} | {}  ".format(x[6],x[7],x[8]))   
def X_or_O():
    player = ["X","O","X"]
    r = random.randint(0, 10)
    print("The computer has picked a random number between 0 and 10.\nBoth users must pick a number between 1 and 10.\nThe closest to the CPU's choice is the winner of the choice")
    ch1 = int(input('Player 1 enter your choice'))
    ch2 = int(input('Player 2 enter your choice'))
    print("CPU has picked {}".format(r))
    if abs(r-ch1)<abs(r-ch2):
        print('Player1 won has won the toss')
        ch = int(input('Enter 0 for X and 1 for O: \n'))
        player2 = player[ch+1]
        player1 = player[ch]
        user_turn = 1
    elif abs(r-ch1) == abs(r-ch2):
        print("choices were equal!Try again")
        player1, player2, user_turn = None, None, None
        return player1,player2,user_turn
    else:
        print('Player2 won has won the toss')
        ch = int(input('Enter 0 for X and 1 for O'))
        player1 = player[ch+1]
        player2 = player[ch]
        user_turn = 2
    print('Player 1 picked {}   Player 2 picked {} , Player {} will start'.format(player1,player2,user_turn))
    return player1,player2,user_turn
#player = X_or_O() ->>tuple
def play():
	print("It is {}'s turn".format(user_turn))
	print("Enter your choice of input on board..")
	ch = int(input('Enter a choice between 0-9\t'))
	if ((ch in player_one) or (ch in player_two)):
		print('ERROR! you entered a choice again.')
		exit(0)
	if (turn_number%2==0):
		player_one.append(ch)
	else:
		player_two.append(ch)
	return ch
def check_win(player1,player2):
	player_one.sort()
	player_two.sort()
	if player1 in win_possibility:
		print("player1 is the winner")
		exit(0)
	if player2 in win_possibility:
		print("player2 is the winner")
		exit(0)
def board_full():
	if len(player_one)==5 or len(player_two)==5:
		print("DRAW")
		exit(0)
user_rules()
draw(choice_list)
while(True):
	player1,player2,user_turn = X_or_O()
	if player1 is not None:
		break
while(turn_number<10):
	ch = play()
	if turn_number%2==0:
		choice_list[ch] = player1
	else:
		choice_list[ch] = player2
	draw(choice_list)
	turn_number+=1
	check_win(player_one, player_two)
	board_full()
	print('----------------------------------------------')
	user_turn = 1 if user_turn>1 else 2