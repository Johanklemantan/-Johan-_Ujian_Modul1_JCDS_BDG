num=(input('Input your phone number: '))
def create_phone_number(num):

    a = [num]
    for i in a:
        if i.isalpha()==True:
            print('Invalid Input. No Alphabeth')
            return
        elif i.isnumeric()==False:
            print('Invalid input. No Symbols')
            return
        elif i.isnumeric()==True:
            if len(num)!=10:
                print('Digits must be in length of 10, not more or less.')
                return
            elif int(i) < 0:
                    print('Input only positive number.')
                    return
            else:
               
                phone_number = []
                for i in range(0,len(num)):
                    if i == 0:
                        phone_number.append('('+num[i])
                    elif i == 2:
                        phone_number.append(num[i]+') ')
                    elif i == 5:
                        phone_number.append(num[i]+'-')
                    else:
                        phone_number.append(num[i])

    hasil = ''.join(phone_number)
    # print(a)
    print(hasil)
create_phone_number(num)
                    

