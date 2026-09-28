class Solution:

  def findRotation(
      self, mat: list[list[int]], target: list[list[int]]
  ) -> bool:
    for _ in range(4):
      if mat == target:
        return True
      # Rotate matrix 90 degrees clockwise: transpose and reverse each row
      mat = [list(row) for row in zip(*mat[::-1])]

    return False