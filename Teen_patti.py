num = int(input("Enter number of players "))
dict={}

'''Inputting initial details about players  '''
 
for i in range(1,num+1):
	dict.update({i:input("Enter name of player "+str(i)+' ')})

#echo
for x in dict.items():
	print (x)


INITIAL = int(input("Enter the initial amount"))
balance={}
for i in range(1,num+1):
	balance.update({i:INITIAL})

