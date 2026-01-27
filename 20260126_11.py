# 1. 성적과 점수를 매칭한 딕셔너리 만들기
grade_map = {
    "A+": 4.5, "A": 4.0,
    "B+": 3.5, "B": 3.0,
    "C+": 2.5, "C": 2.0,
    "D+": 1.5, "D": 1.0,
    "F": 0.0
}

grade_input = input("성적을 입력(예: A+): ").upper()

if grade_input in grade_map:
    score = grade_map[grade_input]
    print(f"성적: {score}")
else:
    print("올바른 성적 형식이 아닙니다.")
