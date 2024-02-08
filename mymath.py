def nCr(n,r) -> int :
    '''
    조합 함수
    :param n: 총 개수
    :param r: 뽑을 개수
    :return: 경우의수
    '''
    numerator=factorial(n)
    denominator=factorial(n-r)*factorial(r)

    return int(numerator/denominator)

def factorial(num) -> int :
    '''
    반복문을 이용한 팩토리얼 계산
    :param num:  num!
    :return: 팩토리얼 값
    '''
    result=1
    for i in range(1,num+1):
        result *=i
    return result

# def factorial(num)->int:
#     '''
#     재쉬함수를 이용함
#     :param num:
#     :return:
#     '''
#     if num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
