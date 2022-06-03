import os
import sys

class colors:
    cyan = '\033[96m'
    green = '\033[92m'
    red = '\033[91m'
    normal = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    yellow = '\033[93m'


class ParensStack:
    
    open_chars = set("[{(")
    close_chars = set("}])")
    
    def __init__(self, parens):
        assert all([item in (self.open_chars | self.close_chars) for item in parens])
        self.parens = parens

    def push(self, item):
        self.container.append(item)
        self.print_state(f"PUSH {item}", colors.green)
        return None

    def process_paren(self, item):
        if item in self.open_chars:
            self.push(item)
        else:
            opener = self.pop()
            if item == "}":
                assert opener == "{"
            elif item == ")":
                assert opener == "("
            else:
                assert opener == "["
            self.print_state(f"POP {opener}", colors.red)

    def is_valid(self):
        self.container = list()
        try:
            for i, c in enumerate(self.parens):
                print("           " + colors.green + self.parens[:i] + colors.red, colors.bold + self.parens[i] + colors.normal, self.parens[i+1:])
                self.process_paren(c)
            if not self.container:
                print(colors.green + "VALID PARENS - END" + colors.normal)
                return True
        except AssertionError:
            print(colors.red + "INVALID PARENS - END" + colors.normal)
            return False

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return not self.container
        
    def get_container_string(self):
        return "[ " + colors.bold + str(self.container)[1:-1].replace("'", "").replace(",", colors.normal + "," + colors.bold) + colors.normal + " ]"
    
    def print_state(self, action, color, timeout=2):
        print(f"\n------------- State of stack ------------------\n{action} ----> " + self.get_container_string())
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")

        
os.system('cls' if os.name == 'nt' else 'clear')
print('\n')
test = ParensStack(sys.argv[1])
# test = ParensStack("{(){[{(({}))}]}[]}")
test.is_valid()