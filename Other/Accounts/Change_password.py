
### Changing Password Program ###

__author__      = "Morgan Chorlton"
__email__       = "morgan.chorlton3@gmail.com"

Password_list = ['password', 'Password', 'sesame', 'Sesame', 'letmein', 'LetMeIn', 'Qwerty' , 'Cheese']

username = str(input('Username: '))
print('Hi, ' + str(username) + ' to change your password you need to create a new password, this password must be: \n between 6 and 12 characters \n And it must not match any of the following passwords: ' + str(Password_list))
def change_password():
    password = str(input('Password: '))
    password_confirm = str(input('Confirm your password: '))
    if len(password) < 6:
        print('Error: Your password must be between 6 and 12 characters in length')
        change_password()
    elif len(password) > 12:
        print('Error: Your password must be between 6 and 12 characters in length')
        change_password()
    elif password != password_confirm:
        print('Your passwords dont\'t match please try again.')
        change_password()
    elif any(word in password for word in Password_list):
        print('please try again and enter a valid password')
        # runs the change password block again
        change_password()
    else:
        print('')
        print('Your password has been changed')
        new_password = [username, password]
        with open("Passwords.txt", "w") as output:
            output.write(str(new_password))
#runs the change password block
change_password()