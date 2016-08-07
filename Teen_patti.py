def chance(temp_dict,stake):
	temp=temp_dict
	packed=[]
	keys = temp.keys()
	for x in keys:
		prompt = input(temp[x]+' ')
		if prompt.isdigit():
			bet=int(prompt)
		else:
			global gameStatus
			gameStatus=0
			print('The game is over')
			return {},stake
		stake+=bet
		balance.update({x:(balance[x]-bet)})

		if (bet==0):
			#a list of peope who have packed
			#the player has packed
		        packed.append(x)
	for x in packed:
		del temp_dict[x]
	return temp_dict,stake

def round():
	stake=0
	temp_dict =data.copy() 
	print('New Round!')
	while(len(temp_dict)>1):
		print('Input the betting money after each displayed name\n ')
		temp_dict, stake =chance(temp_dict,stake)
		# print(temp_dict)
		# print(data)

	return stake
		
stake=0
gameStatus = 1;
num = int(input("Enter number of players "))
data={}

'''Inputting initial details about players  '''
 
for i in range(1,num+1):
	data.update({i:input("Enter name of player "+str(i)+' ')})

#echo
print(data)


INITIAL = int(input("Enter the initial amount "))
balance={}

for i in range(1,num+1):
	balance.update({i:INITIAL})

while(gameStatus==1):
	stake=round()
	if(gameStatus==1):
		winner = int(input('Enter player number who won the round'))
		balance.update({winner:(balance[winner]+stake)})
		print('The current balance of each player is ')
		for x in balance.keys():
			print(str(x) + '	'+data[x]+'	'+str(balance[x]))
		# print (str(x) + '	'+ str(balance[x])
	else:
		print('The final balance of each player is ')
		for x in balance.keys():
			print(str(x) + '        '+data[x]+'     '+str(balance    [x]))

	'''print('balance')
	print(balance)
	print('data')
	print(data)'''
