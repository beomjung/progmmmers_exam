
clothes= [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

clothesTypeMap = {}

for clothe, clothesType in clothes:
    print("clothe:",clothe)
    print("clothesType : ", clothesType)
    clothesTypeMap[clothesType] = clothesTypeMap.get(clothesType, 0) + 1

print(clothesTypeMap)

answer = 1
for clothesType in clothesTypeMap:
    answer *= (clothesTypeMap[clothesType] + 1)

print(answer-1)