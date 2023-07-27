"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
"""
class Solution:
    def average(self, salary: List[int]) -> float:
        # find & remove min and max
        salary.remove(min(salary))
        salary.remove(max(salary))
        # calc average
        sal_len = len(salary)
        sum = 0
        for num in salary:
            sum += num
        return 0 if sal_len < 1 else sum / sal_len
