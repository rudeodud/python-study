def get_peri():
    radius = 5.0
    result = radius * radius * 3.141592
    print("get_peri() = " + result)

def get_pero(radius):
    result = radius * radius * 3.141592
    print("get_peri({})")


def main():
    radius = float(input("원의 반지름을 입력하시오:"))
    