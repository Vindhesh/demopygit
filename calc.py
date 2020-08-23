
class Calculator:
    def __init__(self):
        pass
    
    def calculate(self):
        answer = 0
        memory = list()
        while True:

            input1, operator, input2 = input("Enter your first number, operator and second number with space: ").split()
            input1 = float(input1)
            input2 = float(input2)
            if operator == "+":
                answer = input1 + input2

            elif operator == "-":
                answer = input1 - input2

            elif operator == "*":
                answer = input1 * input2
                        
            elif operator == "/":
                answer = input1 / input2
                    
            memory.append(answer)
            memory.reverse()
            print("Your answer for current calculation is:", answer)

            check = input("Want to calculate?: y/n ")
            if check == "y":
                continue
            else:
                pass
            print("The memory of last five calculations is: ", memory[1 : 6])
            break
            
one = Calculator()
one.calculate()
