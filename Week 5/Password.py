
        ### Changing Password Program ###

Password_list = ['password', 'Password', 'sesame', 'Sesame', 'letmein', 'LetMeIn', 'Qwerty' , 'Cheese']

Username = str(input('Username: '))
print('Hi, ' + str(Username) + ' to change your password you need to create a new password, this password must be: \n between 6 and 12 characters \n And it must not match any of the following passwords: ' + str(Password_list))
def change_password():
    Password = str(input('Password: '))
    Password_confirm = str(input('Confirm your password: '))
    if len(Password) < 6:
        print('Error: Your password must be between 6 and 12 characters in length')
        change_password()
    elif len(Password) > 12:
        print('Error: Your password must be between 6 and 12 characters in length')
        change_password()
    elif Password != Password_confirm:
        print('Your passwords dont\'t match please try again.')
        change_password()
    elif any(word in Password for word in Password_list):
        print('please try again and enter a valid password')
        # runs the change password block again
        change_password()
    else:
        print('')
        print('Your password has been changed')
#runs the change password block
change_password()