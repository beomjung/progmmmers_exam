def solution(participant, completion):
    # 해시값 저장 변수
    answer = 0;

    # 해시값과 이름이 저장되는 키값 구조
    dic = {};

    for p in participant:
        dic[hash(p)] = p;
        answer += int(hash(p));

    for com in completion:
        answer -= hash(com);

    return dic[answer]