st1, st2 = input().split()

if st1 > st2:
    print(st1,"가(이) 더 큽니다.")
elif st1 < st2:
    print(st2,"가(이) 더 큽니다")
else: 
    print("두 문자열의 크기는 같습니다.")

if st1[:3] == st2[:3]:
    print("앞의 세 문자가 같습니다.")
else:
    print("앞의 세문자가 같지 않습니다.")