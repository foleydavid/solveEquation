class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        Condition: ans will be integer for all relevent inputs
        """
        #xleft(0) numleft(1) xright(2) numright(3)
        vals = [[],[],[],[]]
        val_pos = 0
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        ans = ""

        #break up equation into left and right side in full_eq[]
        eq_left = "+" + equation[0:equation.find("=")] + "+"
        eq_right = "+" + equation[equation.find("=") + 1:] + "+"
        full_eq = [eq_left, eq_right]

        #fill in vals
        for eqn in full_eq:
            index = 1

            while index < len(eqn):
                temp = ""
                offset = 0
                
                #found a number or x
                if eqn[index] in nums or eqn[index] == "x":
                    
                    #add number
                    while eqn[index + offset] in nums:
                        temp = temp + eqn[index + offset]
                        offset += 1
                            
                    #reading x
                    if eqn[index + offset] == "x":
                        
                        #x not preceded by a num
                        if len(temp) == 0:
                            temp = "1"

                        #check if number is pos or negative
                        if eqn[index - 1] == "-":
                            temp = "-" + temp
                        vals[val_pos].append(int(temp))
                            
                    #reading symbol
                    else:
                        if eqn[index - 1] == "-":
                            temp  = "-" + temp
                        vals[val_pos + 1].append(int(temp))

                #skip past already seen info
                index = index + offset + 1
                
            #passing the equals sign
            val_pos += 2
 
        #sums vals
        vals = [sum(x) for x in vals]

        #checks for zeros in numerator and denomenator
        if vals[0] - vals[2] == 0 and vals[3] - vals[1] == 0:
            ans = "Infinite solutions"
        elif vals[0] - vals[2] == 0:
            ans = "No solution"
        else:
            ans = "x="
            ans += str(int((vals[3] - vals[1]) / (vals[0] - vals[2])))

        return ans
