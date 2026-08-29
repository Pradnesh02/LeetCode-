import bisect


class MyCalendar:

  def __init__(self):
    # Maintain a sorted list of booked intervals: [(startTime, endTime), ...]
    self.calendar = []

  def book(self, startTime: int, endTime: int) -> bool:
    # Find insertion point using binary search
    idx = bisect.bisect_right(self.calendar, (startTime, endTime))

    # Check overlap with previous interval (idx - 1)
    if idx > 0 and self.calendar[idx - 1][1] > startTime:
      return False

    # Check overlap with next interval (idx)
    if idx < len(self.calendar) and self.calendar[idx][0] < endTime:
      return False

    # Insert into the sorted calendar
    self.calendar.insert(idx, (startTime, endTime))
    return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime, endTime)