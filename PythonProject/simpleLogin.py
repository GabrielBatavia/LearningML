username = input('Input username : ')
password = input('Input password : ')

print('Your account has been created')
print('Please enter your account for logging in')

username2 = input('Enter username : ')
password2 = input('Enter password : ')

if username2 == username and password2 == password:
    print('Your login was successful')
else:
    print('Failled login, Enter your right username and password')
