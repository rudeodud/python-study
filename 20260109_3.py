def scored(score):
    if score >= 90:
        print("성적은 A 입니다.")
    elif score >= 80:
        print("성적은 B 입니다.")
    elif score >= 70:
        print("성적은 C 입니다.")
    elif score >= 60:
        print("성적은 D 입니다.")
    else:
        print("성적은 F 입니다.")

def main():
    score = int(input("점수를 입력 하세요."))
    scored(score)

main()