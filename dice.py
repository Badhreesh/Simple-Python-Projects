from random import randint

def main():
	min = 1

	max = int(input('How many sided Die do you want to use?'))

	roll = True

	while True:  
		print('Do you want to roll?')
		answer = input()
		if 'y' in answer:
			print('You rolled a', randint(min, max))
		elif answer == 'n' or answer == 'no':
			print('Thanks for playing')
			break
		else:
			print('Invalid Format. Try Again') 	

if __name__ == '__main__':
	main()