# 사전 문제
# 알파벳의 개수를 출력할 때, 알파벳 순서대로 (a 부터 z 의 순서) 출력하도록 작성하시오.
sentence = """by the rivers of babylon, there we sat down yeah we wept,
when we remember zion.
when the wicked carried us away in captivity required from us a song
now how shall we sing the lord’s song in a strange land"""

alphabet = dict()                  # 빈 사전을 생성
for c in sentence :
    if c.isalpha() == False :
        continue
    c = c.lower()
    if c not in alphabet :
        alphabet[c] = 1
    else :
        alphabet[c] += 1
print(sorted(alphabet.items()))