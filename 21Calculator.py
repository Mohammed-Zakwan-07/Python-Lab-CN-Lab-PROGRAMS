class Calculator:
    def operate(self, *args):
        """
        Performs different operations based on number of arguments:
        - 1 arg  → square
        - 2 args → addition
        - 3 args → (a * b) + c
        - more    → sum of all
        """
        count = len(args)
        
        if count == 1:
            return f"Square of {args[0]} = {args[0] ** 2}"
        
        elif count == 2:
            return f"{args[0]} + {args[1]} = {args[0] + args[1]}"
        
        elif count == 3:
            return f"({args[0]} × {args[1]}) + {args[2]} = {(args[0] * args[1]) + args[2]}"
        
        else:
            total = sum(args)
            return f"Sum of {args} = {total}"

# Demo
calc = Calculator()

print(calc.operate(7))              # Square
print(calc.operate(10, 5))          # Addition
print(calc.operate(4, 3, 8))        # (a*b)+c
print(calc.operate(1, 2, 3, 4, 5))  # Sum
