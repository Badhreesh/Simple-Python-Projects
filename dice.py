from random import randint

def dice_roll(sides):
	while True:
		answer = input('Do you want to roll? (y/n)')
		if answer == 'y':
			print('You rolled a', randint(1, sides))
		elif answer == 'n':
			print('Thanks for playing')
			break
		else:
			print('Invalid Format. Try Again')


def main():
	sides = int(input('How many sided Die do you want to use?'))
	dice_roll(sides)
	

if __name__ == '__main__':
	main()