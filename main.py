def password_validation(password):
    val=True
    SpecialSym =['$', '@', '#', '%']
    if(len(password)>10):
        print('the length of password would have only 10 characters--')
        val=False
    if(len(password)<6):
        print('password lenght must be greater than 6--')
        val=False
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val
    return val

def user_validation(user):
    val = True
    SpecialSym = ['$', '@', '#', '%']
    if (len(user) > 10):
        print('the length of password would have only 10 characters--')
        val = False
    if (len(user) < 6):
        print('password lenght must be greater than 6--')
        val = False
    if any(char.isdigit() for char in user):
        print('username does not contains any digit')
        val = False
    if not(char in SpecialSym for char in user):
        print('username should not have any symbols like $@#')
        val = False
    return val


def verify_user(pasword,user):
    if(user=='shruti'):
        if(pasword=='Shruti$123'):
            print('--welcome',user)

        else:
            print('you entered wrong password----')
    else:
        print("username does't exist")



def main():
    user=input('enter username\t')
    password=input('enter password\t')
    if(password_validation(password) and user_validation(user)):
        verify_user(password,user)


if __name__ == '__main__':
    main()
