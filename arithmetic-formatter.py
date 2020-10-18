def arithmetic_arranger(problems,result=False):
    lst = []
    arranged_problems = ""
    if((len(problems) > 5)):
        arranged_problems = "Error: Too many problems."
        
    else:
        for i in problems:
            lst.append(i.split())
            if(not(i.split()[0].isnumeric()) or not(i.split()[2].isnumeric())):
                return "Error: Numbers must only contain digits."
        for i in lst:
            if(len(i[0]) > 4):
                return "Error: Numbers cannot be more than four digits."
            if(not(len(i[0]) == 4)):
                spc = ''
                spc_up = len(i[0])
                spc_down = len(i[2])
                if spc_up < spc_down: 
                    spc_len = spc_down - spc_up 
                else:
                    spc_len = 0
            else:
                spc_len = 0
            spc = (spc_len + 2) * " "
            arranged_problems += spc + i[0] + "    "
        arranged_problems = arranged_problems.rstrip(" ")
        arranged_problems += "\n"

        for i in lst:
            if(len(i[2]) > 4):
                return "Error: Numbers cannot be more than four digits."
            if(i[1] == '*' or i[1] == '/'):
                return "Error: Operator must be '+' or '-'."

            if(not(len(i[0]) == 4)):
                spc = ''
                spc_up = len(i[0])
                spc_down = len(i[2])

                if(spc_up > spc_down):
                    spc_len = spc_up - spc_down
                else:
                    spc_len = 0
            else:
                spc_len = 4 - len(i[2])
            
            spc = (spc_len) * " "
            arranged_problems += i[1] + " " + spc + i[2] + "    "
        arranged_problems = arranged_problems.rstrip(" ")
        arranged_problems += "\n"

        for i in lst:
            spc_len = max(len(i[0]),len(i[2]))
            spc = (spc_len + 2) * "-"
            arranged_problems += spc + "    "

        arranged_problems = arranged_problems.rstrip(" ")

        if(result == True):
            arranged_problems += "\n"
            for i in lst:
                ev = str(i[0] + " " + i[1] + " " + i[2])
                spc_max = max(len(i[0]),len(i[2]))
                spc_len = 0
                if(eval(ev) < 0):
                    spc_len -= 1
                if(len(str(eval(ev))) < spc_max):
                    spc_len += spc_max - len(str(eval(ev)))
                spc = (spc_len + 2) * " "
                arranged_problems += spc + str(eval(ev)) + "    "
                
    arranged_problems = arranged_problems.rstrip(" ")
    return arranged_problems
