from fractions import Fraction # 유리수 연산할 때 사용

def solution(numer1, denom1, numer2, denom2):
    result = Fraction(numer1, denom1) + Fraction(numer2, denom2)  # 분수 덧셈
    return [result.numerator, result.denominator]  # 기약분수로 반환
