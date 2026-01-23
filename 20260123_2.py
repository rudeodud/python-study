score_dict = {
    "kim":[99,83,95],
    "Lee":[68,45,78],
    "choi":[25,56,69]
}

for name, scores in score_dict.items():
    print(name,"의 평균성적은",sum(scores)/len(scores))
    