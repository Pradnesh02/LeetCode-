class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def date_to_day_of_year(date: str) -> int:
            month, day = int(date[:2]), int(date[3:])
            return sum(days_in_months[:month - 1]) + day

        start = max(date_to_day_of_year(arriveAlice), date_to_day_of_year(arriveBob))
        end = min(date_to_day_of_year(leaveAlice), date_to_day_of_year(leaveBob))

        return max(0, end - start + 1)