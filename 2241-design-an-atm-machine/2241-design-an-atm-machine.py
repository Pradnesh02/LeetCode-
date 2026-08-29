from typing import List


class ATM:

  def __init__(self):
    # Denominations matching indices 0 to 4: $20, $50, $100, $200, $500
    self.denominations = [20, 50, 100, 200, 500]
    self.banknotes = [0] * 5

  def deposit(self, banknotesCount: List[int]) -> None:
    for i in range(5):
      self.banknotes[i] += banknotesCount[i]

  def withdraw(self, amount: int) -> List[int]:
    take = [0] * 5

    # Greedily pick from the largest denomination to the smallest
    for i in range(4, -1, -1):
      val = self.denominations[i]
      count = min(self.banknotes[i], amount // val)
      take[i] = count
      amount -= count * val

    # If the exact amount cannot be fulfilled, reject transaction
    if amount != 0:
      return [-1]

    # Deduct the banknotes used from the ATM storage
    for i in range(5):
      self.banknotes[i] -= take[i]

    return take