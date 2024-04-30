#Grammar Rule:
#<expr> -> <term> {(+ | -) <term>}
#<term> -> <factor> {(* | /) <factor>}
#<factor> -> id | int_constant | (<expr>)

#Import tokenizer class
from csci3333tok import Tokenizer

#Tokenize the expression
t = Tokenizer()
t.tokenize('(5 + 3) * 2')

nt = t.next_token()

#The outcome function prints the tokens
def outcome():
        global nt
        if nt.name != 'EOS':
                print(nt)
                print('token is: ' + nt.name + ', text is: ' + nt.text)

outcome() #Need to call outcome function to parse first token

#Parses the statements in first grammar rule
def expr():
        global nt
        print("Start <expr>")
        term()
        while nt.text == '+' or nt.text == '-':
                nt = t.lex()
                outcome()
                term()
        print("Finish <expr>")

#Parses the statements in second grammar rule
def term():
        global nt
        print("Start <term>")
        factor()
        while nt.text == '*' or nt.text == '/':
                nt = t.lex()
                outcome()
                factor()
        print("Finish <term>")

#Parses the statements is third grammar rule
def factor():
        global nt
        print("Start <factor>")
        if nt.name == 'ID' or nt.name == 'NUMBER':
                nt = t.lex()
                outcome()
        else:
                if nt.name == 'LPAREN':
                        nt = t.lex()
                        outcome()
                        expr()
                        if nt.name == 'RPAREN':
                                nt = t.lex()
                                outcome()
                        else:
                                print('ERROR')
                else:
                        print('ERROR')
        print("Finish <factor>")

expr() #Execute the expression