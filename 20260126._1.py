def readData():
    a, b = map(int, input("2개의 정수를 입력:").split())
    
    if a > b:
        print(f"더 큰수는 {a} 입니다")
    else:
        print(f"더 큰수는 {b} 입니다")

readData()
