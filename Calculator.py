import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, expression: str) -> bool:
        parenthesis = []
        for char in expression:
            # print(char)
            if char == "(":
                parenthesis.append("(")
                # print(parenthesis)
            elif char == ")":
                if len(parenthesis) == 0: return False
                parenthesis.pop()
        if len(parenthesis) > 0: return False
        else: return True
        

    def print_expression(self, exp: str) :
        new_exp = ""
        for char in exp:
            
            if char.isalpha():
                value = self.dict.find(char)
                if value is None:
                    new_exp = new_exp + char
                else:
                    new_exp = new_exp + str(value)
            else:
                new_exp = new_exp + char
        # print(new_exp)
        return new_exp         
            
        # return a string where the variables have been replaced
    def build_parse_tree(self, exp:str) -> str:
        return self._build_parse_tree(exp)
    
    def _build_parse_tree(self, exp: str) -> str:
        if self.matched_expression(exp) == False:
            raise ValueError("Parenthesis are not matched")

        tree = BinaryTree.BinaryTree()
        tree.r = tree.Node(None)
        current = tree.r
        i = 0

        while i < len(exp):
            char = exp[i]
            if char == "(":
                # print(char, "-- CREATED LEFT CHILD NODE") 
                current.insert_left(tree.Node(None)) 
                current = current.left
            elif char == ")":
                # print(char, "-- EXITED TO PARENT") 
                current = current.parent
            elif char == "+" or char == "-" or char == "*" or char == "/":
                current.k = char
                current.v = char
                # print(char, "-- SET NODE VALUE", current) 
                current.insert_right(tree.Node(None)) 
                # we insert right but we ended up with a None value, not the same as a None object
                current = current.right
            elif char.isalpha():
                # treat as variable
                j = i + 1
                while j < len(exp):
                    if exp[j] not in "-*/+()":
                        j += 1
                    else:
                        break;
                var_name = exp[i:j]
                value = self.dict.find(var_name)
                if not value:
                    print("Result: Error - Not all variable values are defined.")
                    return None;
                else:
                    current.k = var_name
                    current.v = value
                    # print(var_name, "-- SET VARIABLE")
                    current = current.parent
                i = j - 1
            else:
                # treat as number
                j = i + 1
                while j < len(exp) and exp[j].isdigit():
                    j += 1
                num = int(exp[i:j])
                current.k = num
                current.v = num
                # print(num, "-- SET NUMBER")
                current = current.parent
                i = j - 1

            i += 1
        return tree

  

    def _evaluate(self, root: BinaryTree.BinaryTree.Node):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        
        # root holds an operator
        if root.left and root.right:
            operationFn = op[root.v]
            # print('has roots ---', root.v)
            # something is wrong here
            if root.left.v is not None and root.right.v is not None:
                return operationFn(self._evaluate(root.left), self._evaluate(root.right))
            else:
                raise ValueError('Missing operand(s) for operator', root.v)
        elif root.left is None and root.right is None:
            # if root.v is a number
            if root.v is not None:
                # print(root.k, root.v)
                return float(root.v)
            elif root.k and root.v is None:
                raise ValueError("Error - Not all variable values are defined", root.k)
        elif root.left is not None:
            return self._evaluate(root.left);
        elif root.right is not None:
            return self._evaluate(root.right);
        
    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        if parseTree is None:
            raise ValueError("Result: Error - Not all variable values are defined.")
        return self._evaluate(parseTree.r)


# calc = Calculator()
# calc.set_variable("delta5" , 9.05)
# calc.set_variable("beta6" , 5.15)
# calc.set_variable("gamma3", 7.8)
# calc.set_variable("gamma9" , 10.4)
# calc.set_variable("alpha6" ,10.42)
# calc.set_variable("omega3" , 10.5)
# calc.set_variable("alpha8" , 9.96)
# calc.set_variable("zeta1" , 7.98)
# print(calc.evaluate("(((delta5/beta6)*(gamma3+gamma9))/((alpha6+omega3)+(alpha8+zeta1)))"))

# print(calc.evaluate("(((delta3-lambda6)*(tau2*mu5))-((mu7*alpha1)*(zeta6+delta2)))"))

