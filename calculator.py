
# Main entrance to program



class AlgebraCalculator():
    def __init__(self, equation = ""):
        self.equation = equation
    
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if(num2 == 0):
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    
    # Calculates the equation
    def calculate_equation(self, equation):
        # Split equation into left and right side
        equation = equation.replace(" ", "")
        equation = equation.split("=")
        left_side = equation[0]
        right_side = equation[1]


        operators = ["*", "/","+", "-"]
        # loop through left side and find operator
        for i, j in enumerate(left_side):
            if(j in operators):
                print(i , j)
                operator = i,
                break
        
        if left_side[int(operator)] == "*":
            print("multiply")
            left_num = left_side[operator - 1]
        elif(left_side[operator - 1] == "x"):
            left_num = "x"
            
        answer = left_num
        print(answer) 

        # Find the operator
        
        
        # Return the answer
        return answer
    
cal = AlgebraCalculator()
equation = "x + 5 = 10"
cal.calculate_equation(equation)
