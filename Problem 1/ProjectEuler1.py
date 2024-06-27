def project_euler_one(p: int, q: int, bound: int) -> int:
  '''
  A function that returns the sum of all multiples of "p" or "q" below "bound"
  where p, q, and bound are natural numbers.

  The function utlises the linearity of series and the sum of a series to
  efficiently calculate a series of multiples of p and q.
  It then does the same for the series of multiples of p & q.

  Parameters:
  -----------
  p: int
    A natural number for the mutliple.

  q: int
    A natural number for the multiple.

  bound: int
    The bounding natural number for the sum.

  Output:
  -------
  int
    Sum of all multiples of "p" or "q" below "bound".
  '''

  bound -= 1
  pq = p * q
  p_bound, q_bound, pq_bound = bound//p, bound//q, bound//(pq)

  sum_of_p_series = p * p_bound * (p_bound + 1) * 0.5
  sum_of_q_series = q * q_bound * (q_bound + 1) * 0.5
  sum_of_pq_series = pq * pq_bound * (pq_bound + 1) * 0.5

  return int(sum_of_p_series + sum_of_q_series - sum_of_pq_series)
