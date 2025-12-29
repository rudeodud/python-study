st = input().strip()
words = st.split("<slash>")
for word in words: 
    print(word.strip())