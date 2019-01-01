poket = ["phone", "wallet"]
call = input()

if call == poket[0]:
    print ("엄마한테 전화해라")
elif call == poket[1]:
    print ("택시타고 가라")
else:
    print ("걸어가세요~~")

#리스트 문과 if문을 동시에 사용해야 하는문제를 주었다.
#처음 리스트를 사용하지 않고 call=="phone" 이런식으로 접근했는데 리스트문이 사용되지 않아서 생각해 보고 코드를 만들었다.