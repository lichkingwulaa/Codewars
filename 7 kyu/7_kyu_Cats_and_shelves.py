def solution(start, finish):
    (a, b) = divmod(finish - start, 3)
    return a + b

# def solution(start, finish):
    # answer1 = (finish - start) // 3
    # answer2 = (finish - start) % 3
    # return answer1 + answer2
