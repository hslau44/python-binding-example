import argparse
from build import SumFunction


class TextMathSolver:
    """
    Perform basic arithmetic operations from text
    """
    _operators = {
        '+': SumFunction.suming_a_b,
        '-': SumFunction.subtracting_a_b,
        'x': SumFunction.multiplying_a_b,
        '/': SumFunction.dividing_a_b,
    }

    def __call__(self, text: str):
        """
        Perform basic arithmetic operations from text

        Parameters
        ----------
        text: str
            question to be solved, must only contain two positive 
            number (float or integer) with operator in between
        
        Return
        ------
        float
        """
        for sym, func in self._operators.items():
            if len(text.split(sym)) == 2:
                a, b = [self._convert_to_num(n) 
                        for n in text.split(sym)]
                return func(a, b)
    
    def _convert_to_num(self, text: str):
        return float(text)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                prog='BasicMathSolver',
                description='Perform basic arithmetic operations from text',
                epilog='Text at the bottom of help'
            )
    parser.add_argument('text', type=str,  help='Math problem to be solved')
    args = parser.parse_args()
    solver = TextMathSolver()
    try:
        print(solver(args.text))
    except:
        print("Not solvable")
