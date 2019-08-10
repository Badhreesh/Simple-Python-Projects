from random import randint

def guess_num(num):
	
	while True:
		guess = int(input('Take a guess: '))	
		if guess < num:
			print('Guess higher!')
		elif guess > num:
			print('Guess lower!')
		elif guess == num:
			print('Hooray! You are right!')
			break
		

def main():
	num = randint(1, 101)
	start = input('I have a number between 1 and 100 in mind. Want to guess what it is?(y/n)')
	
	if start =='y':
		print('Excellent! Let\'s begin!')
		guess_num(num)
	
	elif start == 'n':
		print('Maybe next time...')

if __name__ == '__main__':
	main()