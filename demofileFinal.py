import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def checkemail(email):
	# pass the regular expression
	# and the string into the fullmatch() method
	if(re.fullmatch(regex, email)):
		return(True)
	else:
		print("Invalid email address")
		return(False)

def checkpwd(pwd):
	SpecialSym = ['$', '@', '#', '%']
	val = True
	if len(pwd) < 5:
		print('length should be at least 5')
		val = False
	if len(pwd) > 18:
		print('length should be not be greater than 18')
		val = False
	if not any(char.isdigit() for char in pwd):
		print('Password should have at least one numeral')
		val = False
	if not any(char.isupper() for char in pwd):
		print('Password should have at least one uppercase letter')
		val = False
	if not any(char.islower() for char in pwd):
		print('Password should have at least one lowercase letter')
		val = False
	if not any(char in SpecialSym for char in pwd):
		print('Password should have at least one of the symbols $@#')
		val = False
	if val:
		return val

def checkuser(email, pwd):
	file1 = open("User_Data.txt", 'r')
	# setting flag and index to 0
	sstatus = "Not Found"
	index = 0
	# Loop through the file line by line
	for line in file1:
		index += 1
		# checking string is present in line or not
		if email in line:
			if pwd in line:
				sstatus = "Logged In"
				break
			else:
				sstatus = "Bad Password"
	# closing text file
	file1.close()
	return sstatus


# Driver Code
if __name__ == '__main__':
	print("Please Provide")
	email = str(input("Email: "))
	pwd = str(input("Password: "))
	if checkemail(email) and checkpwd(pwd):
		info = 'Email address : {0}, Password : {1}'.format(email, pwd)
		sstatus = checkuser(email, pwd)
		if sstatus == "Logged In":
			print("Logged in successfully")
		elif sstatus == "Bad Password":
			print("Bad Password")
			print("reenter password")
			pwd1 = str(input("Password: "))

		else:
			f = open("User_Data.txt", 'a')
			info = 'Email address : {0}, Password : {1}'.format(email, pwd)
			f.write(info)
			f.write("\n")
			print("Registered")
	else:
		print("Not Registered")
