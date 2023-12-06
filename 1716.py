class Solution:
    def totalMoney(self, n: int) -> int:
        # Initialize variables
        total = 0
        # Calculate complete weeks and remaining days
        complete_weeks = n // 7
        remaining_days = n % 7
        
        # Calculate the total for complete weeks
        for i in range(complete_weeks):
            # Calculate the initial deposit for the week
            initial_deposit = i + 1
            # Calculate the total for the week using the arithmetic progression formula
            week_total = 7 * initial_deposit + 7 * (7 - 1) // 2 * 1
            total += week_total
        
        # Calculate the total for the remaining days
        if remaining_days > 0:
            initial_deposit = complete_weeks + 1
            # Calculate the total for the remaining days using the arithmetic progression formula
            remaining_total = remaining_days * initial_deposit + remaining_days * (remaining_days - 1) // 2
            total += remaining_total
        
        return total
