name, kor, eng, mat = input("이름, 국어, 영어, 수학 점수를 차례로 입력하세요: ").split()
kor = int(kor)
eng = int(eng)
mat = int(mat)
sum = kor + eng + mat
avg = sum / 3
print("%15s%5s%5s%5s%5s%7s" % ("name", "kor", "eng", "mat", "sum", "avg"))
print("%15s%5d%5d%5d%5d%7.2f" % (name, kor, eng, mat, sum, avg))
print()
print(f"{'name':>15}{'kor':>5}{'eng':>5}{'mat':>5}{'sum':>5}{'avg':>7}")
print(f"{name:>15}{kor:>5}{eng:>5}{mat:>5}{sum:>5}{avg:>7.2f}")