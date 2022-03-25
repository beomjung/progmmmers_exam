def solution(phone_book):
    phone_book.sort()

    answer = True

    length = len(phone_book)

    for i in range(length - 1):
        if phone_book[i] in phone_book[i + 1][0:len(phone_book[i])]:
            answer = False
            break

    return answer