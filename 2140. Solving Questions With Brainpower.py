"""
2140

You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.



"""
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
      
        max_points = [0] * (n + 1)
     
        for i in range(n - 1, -1, -1):
            points, jump = questions[i]
           
            next_question = min(jump + i + 1, n)
            points_from_this_question = points + max_points[next_question]
            max_points[i] = max(points_from_this_question, max_points[i + 1])
        
        return max_points[0]
