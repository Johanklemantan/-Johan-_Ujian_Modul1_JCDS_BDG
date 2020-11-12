class Statistic:
    def __init__(self, masuk):
        self.inputt = masuk

    def mean(self,masuk):
        for i in masuk:
            if type(i) != int:
                print('Invalid Input! All values must be Integer.')
            elif type(i) == int:            
                total = 0
                for i in masuk:
                    total += i
                hasil = total/len(masuk)
                return print(hasil)
    # mean(self,[12,10,10,10,10])

    def mode(self,masuk):
        for i in masuk:
            if type(i) != int:
                print('Invalid Input! All values must be Integer.')
            elif type(i) == int:            
                max_count = (0,0)
                for i in masuk:
                    muncul = masuk.count(i)
                    if muncul>max_count[0]:
                        max_count=(muncul,i)
                return print(max_count[1])
    # mode()

    def median(self,masuk):
        for i in masuk:
            if type(i) != int:
                print('Invalid Input! All values must be Integer.')
            elif type(i) == int:            
                masuk.sort()
                if len(masuk)%2!=0:
                    tengah = int((len(masuk)-1)/2)
                    return masuk[tengah]
                elif len(masuk) %2 ==0:
                    tengah_1 = int(len(masuk)/2)
                    tengah_2 = int(len(masuk)/2)-1
                    return print((sum(i)/len(masuk))([masuk[tengah_1],masuk[tengah_2]]))
    # median()
    # def std(self,masuk):
    #     for i in masuk:
    #         if type(i) != int:
    #             print('Invalid Input! All values must be Integer.')
    #         elif type(i) == int: 
    #             return ((sum((i)-(sum(i)/len(masuk)(i))**2)/len(masuk))**0.5
    # std()


st=Statistic([12,10,10,10,10])
print(st.mean([12,10,10,10,10]))
print(st.mode([12,10,10,10,10]))
print(st.median([12,10,10,10,10]))
# print(st.std([12,10,10,10,10]))