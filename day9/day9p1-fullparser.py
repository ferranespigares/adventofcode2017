import platform
import re

token_pat = re.compile("\s*(?:(\d+)|(.))")

def tokenize(program):
    for number,operator in token_pat.findall(program):
        if number:
            yield literal_token(number)
        elif operator == "+":
            yield operator_add_token()
        else:
            raise SyntaxError("unknown operator")
    yield end_token()

def parse(program):
    global token, next
    next = tokenize(program).next
    token = next()
    return expression()

class literal_token:
    def __init__(self, value):
        self.value=int(value)
    def nud(self):
        return self.value

class operator_add_token:
    lbp = 10
    def led(self,left):
        right = expression(10)
        return left + right

class end_token:
    lbp = 0

def next():
    global fp
    return fp.read(1)

def expression(rbp=0):
    global token
    t=token
    token=next()
    left=t.nud()
    while rbp < token.lbp:
        t = token
        token = next()
        left = t.led(left)
    return left

parse("1+2")

#Set root path depending on the OS I'm working on that particular day
if platform.system()=='Windows':
    fp=open('C:\Users\User\Documents\dev\\adventofcode2017\day8\input')
elif platform.system()=='Linux':
    fp=open('/home/user/Devel/adventofcode2017/day9/sample')


