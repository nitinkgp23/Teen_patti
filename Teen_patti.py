def round():
	temp_dict = data
	print('Input the betting money after each displayed name\n ')
	
	while(len(temp_dict)>1):
		for x in temp_dict.keys():
			prompt = input(temp_dict[x])
			if prompt.isdigit():
				bet=prompt
			else:
				gameStatus=0
				print('The game is over')
				return
			stake+=bet
			balance.update({x:(balance[x]-bet)})

			if (bet==0):
				#removing the player from current round
				#the player has packed
				del temp_dict[x]
		

global gameStatus = 1;
num = int(input("Enter number of players "))
data={}

'''Inputting initial details about players  '''
 
for i in range(1,num+1):
	data.update({i:input("Enter name of player "+str(i)+' ')})

#echo
for x in data.items():
	print (x)


INITIAL = int(input("Enter the initial amount "))
balance={}
for i in range(1,num+1):
	balance.update({i:INITIAL})
while(gameStatus==1):
	round()
	winner = int(input(Enter player number who won the round))
	balance.update({winner:(balance[winner]+stake)})
	print('The current balance of each player is ')
	for x in balance.keys():
		print(x + '	'+data[x]+'	'+ balance[x])


