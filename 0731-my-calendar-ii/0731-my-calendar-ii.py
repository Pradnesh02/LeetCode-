class MyCalendarTwo:

  def __init__(self):
    self.bookings = []  # Stores single booking intervals
    self.overlaps = []  # Stores double-booked (overlap) intervals

  def book(self, startTime: int, endTime: int) -> bool:
    # Check if the new interval conflicts with any existing double-booking
    for s, e in self.overlaps:
      if max(startTime, s) < min(endTime, e):
        return False

    # Find and record any new double-bookings created by this interval
    for s, e in self.bookings:
      overlap_start = max(startTime, s)
      overlap_end = min(endTime, e)
      if overlap_start < overlap_end:
        self.overlaps.append((overlap_start, overlap_end))

    # Add the interval to bookings
    self.bookings.append((startTime, endTime))
    return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime, endTime)