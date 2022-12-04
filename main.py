def prime_checker(number):
    list=[]
    for k in range(1,number+1):
        list.append(k)
    list.remove(1)
    list.remove(number)
    end=0
    while end==0:
        for m in list:
            if number%m == 0:
                end=1
        if end==1:
            print("not prime number")
        else:
            print("prime number")
            end=1
prime_checker()