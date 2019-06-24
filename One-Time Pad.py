#!/bin/python3

# os.randum is more secure for generating random numbers
from random import randint

alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ,./\;:"[]{}()_-!@#$%^&*|?<>`~'

# Generate numbers and write it to file
def generate_otp(sheets, length):

	# A new file needs to be created for every sheet
	for sheet in range(sheets):
		with open("otp" + str(sheet) + ".txt", "w") as f:

			# Write random numbers to file
			for i in range (length):
				f.write(str(randint(0, 81)) + "\n")

# Open file
def load_sheet(filename):
	with open(filename, "r") as f:

		# 'splitlines() breaks each line up into a single
		# item in the list and removes '\n' character
		contents = f.read().splitlines()

	return contents

# Ask for user's message
def get_plaintext():
	plain_text = input('Enter your message: ')

	# lowercase characters make it easier to encrypt
	#return plain_text.lower()
	return plain_text

# Load file
def load_file(filename):

	# Open file with read-only
	with open(filename, 'r') as f:
		contents = f.read()
	return contents

# Save file
def save_file(filename, data):

	# Open file with write-only
	with open(filename, 'w') as f:
		f.write(data)

# Encrypt message with 'plain_text' and 'sheet'
def encrypt(plaintext, sheet):
	ciphertext = ''

	# Check if character is in 'alphabet'
	for position, character in enumerate(plaintext):

		# Check if character is part of the alphabet
		if character not in alphabet:
			ciphertext += character
		else:
			# Get position of the character with sheet
			encrypted = (alphabet.index(character) + int(sheet[position])) % 81

			# Change number to letter
			ciphertext += alphabet[encrypted]

	return ciphertext

# Decrypt message with 'ciphertext' and 'sheet'
def decrypt(ciphertext, sheet):
	plaintext = ''

	for position, character in enumerate (ciphertext):

		if character not in alphabet:
			plaintext += character
		else:
			decrypted = (alphabet.index(character) - int(sheet[position])) % 81
			plaintext += alphabet[decrypted]

	return plaintext

# Main menu when program starts running
def menu():
	choices = ['1', '2', '3', '4']
	choice = '0'

	# Keep program running in infinite loop
	while True:
		while choice not in choices:
			print('1. Generate one-time pads')
			print('2. Encrypt a message')
			print('3. Decrypt a message')
			print('4. Quit program')

			# Have user enter command
			choice = input('Enter number: ')

			# Instructions for each command
			if choice == '1':
				sheets = int(input('How many OTP should be generated? '))
				length = int(input('What will be the maximum message length? '))

				generate_otp(sheets, length)

			elif choice == '2':
				filename = input('Enter filename of the OTP you want to use: ')
				sheet = load_sheet(filename)
				plaintext = get_plaintext()
				ciphertext = encrypt(plaintext, sheet)
				filename = input('Enter name of encrypted file: ')

				save_file(filename, ciphertext)

			elif choice == '3':
				filename = input('Enter filename of the OTP you want to use: ')
				sheet = load_sheet(filename)
				filename = input('Type the name of the file to be decrypted: ')
				ciphertext = load_file(filename)
				plaintext = decrypt(ciphertext, sheet)

				print('Decrypted Message: \n' + plaintext)

			elif choice == '4':
				exit()

			# reset choice number
			choice = '0'


# Start program with 'menu()'
menu()
