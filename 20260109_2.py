def cale(num1, num2):
    def plus(num1, num2):
        result = num1 + num2
        return result
    def minus(num1, num2):
        result = num1 - num2
        return result
    def multi(num1, num2):
        result = num1 * num2
        return result
    def div(num1, num2):
        result = num1 / num2
        return result
    
    resultplus = plus(num1, num2)
    resultminus = minus(num1, num2) 
    resultmulti = multi(num1, num2)
    resultdiv = div(num1, num2)
    return resultplus, resultminus, resultmulti, resultdiv

def main():
    num1 = int(input("첫번째 숫자 입력:"))
    num2 = int(input("두번쨰 숫자 입력"))

    result = cale(num1, num2)
    print()
    print(result[0], result[1], result[2], "{}이 반환되었습니다.".format(result[3]))

main()