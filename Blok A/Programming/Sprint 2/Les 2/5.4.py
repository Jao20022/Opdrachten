def new_password(oldpassword, newpassword):
    num = False
    for i in newpassword:
        if i.isdigit():
            num = True
    if newpassword != oldpassword and len(newpassword) >= 6 and num:
        return True
    else:
        return False

op = 'asdfbvcnasd1'
np = 'asdfbvcnad'

print(new_password(op,np))