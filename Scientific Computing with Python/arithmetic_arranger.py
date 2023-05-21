# Formateador aritmetico

def arithmetic_arranger(problems, soluc=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    if len(problems) == 0:
        return "Error: No problems to be arranged."

    arranged_problems = ""
    
    l1 = ""
    l2 = ""
    mid = ""
    fsol = ""
    for problem in problems:
        x1 = problem.split(" ")[0]
        op = problem.split(" ")[1]
        x2 = problem.split(" ")[2]
        if op != "+" and op != "-":
            return "Error: Operator must be '+' or '-'."
        if len(x1) > 4 or len(x2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if x1.isdigit() == False or x2.isdigit() == False:
            return "Error: Numbers must only contain digits."
        if op == "-":
            sol = int(x1) - int(x2)
        else:
            sol = int(x1) + int(x2)
        
        l1 = l1 + "  " + (" " * (max(len(x1), len(x2))-len(x1))) + x1 + "    "
        l2 = l2 + op + " " + (" " * (max(len(x1), len(x2))-len(x2))) + x2 + "    "
        
        mid = mid + "-" * (max(len(x1), len(x2))+2) + "    "
        if soluc == True:
            fsol = fsol + (" " * ((max(len(x1), len(x2))+2)-len(str(sol)))) + str(sol) + "    " 
    if soluc == True:
        arranged_problems = l1.rstrip() + "\n" + l2.rstrip() + "\n" + mid.rstrip() + "\n" + fsol.rstrip()
    else:
        arranged_problems = l1.rstrip() + "\n" + l2.rstrip() + "\n" + mid.rstrip()

    print(arranged_problems)
        
    return arranged_problems



arithmetic_arranger(['3801 - 2', '123 + 49'],True)