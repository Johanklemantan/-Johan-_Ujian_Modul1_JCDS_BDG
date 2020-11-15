# #1
def create_phone_number(num):
    y = num.split()
    t = ''.join(y)
    print('Input your phone number:',t)

    hasil = []
    for i,j in enumerate (y):
        if len(j)>1:
            print('Input only positive number.')
            print('')
            return
        if j.isnumeric():
            if len(y)<10 or len(y)>10:
                print('DIgits must be in length of 10, not more or less.')
                print('')
                return
                
            elif len(y)==10 :
                if i == 0:
                    hasil.append('(' + j)
                elif i==2:
                    hasil.append(j+') ')
                elif i == 5:
                    hasil.append(j+'-')
                else:
                    hasil.append(j)
                    akhir = ''.join(hasil)
        
    
        elif j.isalnum():
            print('Invalid input. No Alphabet.')
            print('')
            return
        else:
            print('Invalid Input. No symbols.')
            print('')
            return
        # print(i,j)
    print(akhir)
    print('')
# num = input('Input your phone number:')
# num = '1234567890'

# create_phone_number('1 2 3 4 5 6 7 8 9 0')
# create_phone_number('2 3 4 5 -6 7 8 9 0 1')
# create_phone_number('a b c 1 2 3 4 5 5 6')
# create_phone_number('1 2 3 4 5 6 7')
# create_phone_number('1 2 3 4 5 6 7 8 9 0 1')
# create_phone_number('! @ # $ % ^ & 8 9 0')



#2
def moveZeros(num):
    print(f'moveZeros{num}')
    tempat0=[]
    awal = []
    for i in num:
        if type(i) == bool:
            awal.append(i)
        elif type(i)==str:
            awal.append(i)
        else:
        # print(i)
            if i == 0:
                tempat0.append(i)
            else:
                awal.append(i)
    # print(tempat0)
    # print(awal)
    awal.extend(tempat0)
    # print(awal)
    print(f'result:{awal}')
    print('')
    return
# moveZeros([False,1,0,1,2,0,1,3,'a'])
# moveZeros([0,0,0,'Test',0,3,'a',True,False])
# moveZeros([0,True,True,False,'a','b',1,1,1])

#3
class Statistic:
    def __init__(self,num):
        self.nums = num
    @property
    def mean(self):
        total = 0
        for i in self.nums:
            if type(i) == str:
                print('Invalid Input! All values must be Integer.')
                # print('')
                return
            
            elif type(i) == int:
                
                total += i
                rata2 = total / len(self.nums)
        # print(f'total',total)
        print(rata2)
        # print('')
        return


    # mean([1,2,3,4,5,'a'])
    # mean([12,10,10,10,10])
    # mean([4,5,2,1,6,7])

    def median(self):
        
        for i in self.nums:
            if type(i) == str:
                print('Invalid Input! All values must be Integer.')
                # print('')
                return
        for i in self.nums:
            self.nums.sort()
            if type(i) == int:
                if len(self.nums)%2!=0:
                    med = self.nums[int(len(self.nums)/2)]
                else:
                    md = self.nums[int(len(self.nums)/2)-1]+self.nums[int(len(self.nums)/2)]
                    med = md/2
        print(med)
        # print('')
        return
    # median([1,2,3,4,5,'a'])
    # median([12,10,10,10,10])
    # median([4,5,2,1,6,7])


    def mode(self):
        for i in self.nums:
            if type(i) == str:
                print('Invalid Input! All values must be Integer.')
                # print('')
                return
        for i in self.nums:
            if type(i) == int:
                counter = 0
                nos = self.nums[0]
                for i in self.nums:
                    curr_frequency = self.nums.count(i)
                    # print(curr_frequency)
                    if curr_frequency>counter:
                        counter = curr_frequency
                        nos = i
                        # print(nos)
                    elif len(set(self.nums)) == len(self.nums):
                        print('tidak ada modus')
                        return
                return print(nos)
                
    # mode([1,2,3,4,5,'a'])
    # mode([12,10,10,10,10])
    # mode([4,5,2,1,6,7])

    def std(self):
        for i in self.nums:
            if type(i) == str:
                print('Invalid Input! All values must be Integer.')
                # print('')
                return
        # total = 0
        total3 = 0
        for i in self.nums:
            if type(i) == int:
                # total += i
                # print('total',total)
                rata2 = sum(self.nums) / len(self.nums)
                # print('rataa',rata2)
                total2 = ((i)-rata2)**2
                total3+= total2
                # print('total 2 tahapan',total2)
        
        # print('rata2',rata2)
        # print('total 3',total3)
        deviasi = (total3/len(self.nums))**0.5
        return print(deviasi)
# std([1,2,3,4,5,'a'])
# std([12,10,10,10,10])
# std([4,5,2,1,6,7])
st = Statistic

# st.mean([1,2,3,4,5,'a'])
# st.median([1,2,3,4,5,'a'])
# st.mode([1,2,3,4,5,'a'])
# st.std([1,2,3,4,5,'a'])
# print('')
# st.mean([12,10,10,10,10])
# st.median([12,10,10,10,10])
# st.mode([12,10,10,10,10])
# st.std([12,10,10,10,10])
# print('')
# st.mean([4,5,2,1,6,7])
# st.median([4,5,2,1,6,7])
# st.mode([4,5,2,1,6,7])
# st.std([4,5,2,1,6,7])

kasus_1 = Statistic([1,2,3,4,5,'a'])
kasus_2 = Statistic([12,10,10,10,10])
kasus_3 = Statistic([4,5,2,1,6,7])

print(kasus_1.mean)
print(kasus_1.median())
print(kasus_1.mode())
print(kasus_1.std())
print('')
print(kasus_2.mean)
print(kasus_2.median())
print(kasus_2.mode())
print(kasus_2.std())
print('')
print(kasus_3.mean)
print(kasus_3.median())
print(kasus_3.mode())
print(kasus_3.std())
print('')