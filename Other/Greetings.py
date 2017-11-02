name = str(input('Enter your name: '))
number = ['1','2','3','4','5','6','7','8','9','0']
def username():
    if any(word in name for word in number):
        print('Error your name can\'t contain a number')
        username()
    else:
        print('Hi, ' + name)
username()