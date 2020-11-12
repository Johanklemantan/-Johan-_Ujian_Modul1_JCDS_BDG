def move_zeros(x):
    # print('1',(x))
    penampungan0=[]
    for i in x:
        if type(i) == bool:
            continue
        elif type(i)==str:
            continue
        elif type(i)==int:
            if i == 0 :
                penampungan0.append(i)
                x.pop(i)
        
        
        
    # print('2',(x))
    # print(penampungan0)
    x.extend(penampungan0)
    print((x))
    print('')
move_zeros([False,1,0,1,2,0,1,3,'a'])
move_zeros([0,0,0,'Test',0,3,'a',True,False])
move_zeros([0,True,True,False,'a','b',1,1,1])


