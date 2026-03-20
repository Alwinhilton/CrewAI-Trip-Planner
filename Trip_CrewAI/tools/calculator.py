import ast
import operator
import re

from crewai.tools import tool


class CalculatorTools:

    @tool("Make a calculation")
    def calculate(operation: str):
        """
        Perform safe mathematical calculations.
        Example inputs: '200*7', '5000/2*10'
        """
        try:
            allowed_operators = {
                ast.Add: operator.add,
                ast.Sub: operator.sub,
                ast.Mult: operator.mul,
                ast.Div: operator.truediv,
                ast.Pow: operator.pow,
                ast.Mod: operator.mod,
                ast.USub: operator.neg,
                ast.UAdd: operator.pos,
            }

            if not re.match(r"^[0-9+\-*/().% ]+$", operation):
                return "Error: Invalid characters in expression"

            tree = ast.parse(operation, mode="eval")

            def _eval(node):
                if isinstance(node, ast.Expression):
                    return _eval(node.body)
                if isinstance(node, ast.Constant):
                    return node.value
                if isinstance(node, ast.Num):
                    return node.n
                if isinstance(node, ast.BinOp):
                    left = _eval(node.left)
                    right = _eval(node.right)
                    op = allowed_operators.get(type(node.op))
                    if not op:
                        raise ValueError("Unsupported operator")
                    return op(left, right)
                if isinstance(node, ast.UnaryOp):
                    operand = _eval(node.operand)
                    op = allowed_operators.get(type(node.op))
                    if not op:
                        raise ValueError("Unsupported operator")
                    return op(operand)
                raise ValueError("Unsupported expression")

            return _eval(tree)

        except Exception as e:
            return f"Error: {str(e)}"