def get_peri(n = 5.0):
    radius = n
    result = radius * radius * 3.141592
    print("get_peri() = " + result)

def get_peri(radius):
    result = radius * radius* 3.141592
    print(f"get_peri({radius}) = "+f"{result}")


def main():
    radius = float(input("원의 반지름을 입력하시오:"))
    get_peri(radius)

main()
    