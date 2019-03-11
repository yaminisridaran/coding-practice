class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        solution = []
        self.generateParenthesisRec(n,0,0,[],solution)
        return solution
    
    def generateParenthesisRec(self, n, openParentheses, closeParentheses,tempSolution,solution):
        if closeParentheses == n:
            solution.append(''.join(tempSolution))
            print(tempSolution)
            return
        if openParentheses<n:
            tempSolution.append('(')
            print("openParentheses Before func", tempSolution, openParentheses, closeParentheses)
            self.generateParenthesisRec(n,openParentheses+1,closeParentheses,tempSolution,solution)
            print("openParentheses Before pop", tempSolution, openParentheses, closeParentheses)
            tempSolution.pop()
            print("openParentheses After pop", tempSolution, openParentheses, closeParentheses)
        if closeParentheses<openParentheses:
            tempSolution.append(')')
            print("closeParentheses Before func", tempSolution, openParentheses, closeParentheses)
            self.generateParenthesisRec(n,openParentheses,closeParentheses+1,tempSolution,solution)
            print("closeParentheses Before pop", tempSolution, openParentheses, closeParentheses)
            tempSolution.pop()
            print("closeParentheses After pop", tempSolution, openParentheses, closeParentheses)

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))