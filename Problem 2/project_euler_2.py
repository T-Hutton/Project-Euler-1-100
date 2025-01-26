import math

def project_euler_two(max_term: int) -> int:
    fibs = []
    start, start_minus_1 = 1, 0

    while start <= max_term:
        start += start_minus_1
        start_minus_1 += start
        fibs.append(start)

    return fibs[:-1]


def nth_fibonacci_number(n: int):

  phi = (1 + math.sqrt(5)) / 2
  psi = (1 - math.sqrt(5)) / 2

  return ((phi ** n) - (psi ** n)) // math.sqrt(5)


def sum_even_fibonacci(bound: int):
  nth_term = 0
  n = 0
  total = 0

  while nth_term < bound:
    total +=nth_term
    n +=3
    nth_term = nth_fibonacci_number(n)


  return total
