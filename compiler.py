import sys

def isChar(character):
    num = ord(character)
    if((num >= 65 and num <= 90) or (num >= 97 and num <= 122)):
        return True
    else:
        return False

def isNum(character):
    num = ord(character)
    if(num >= 48 and num <= 57):
        return True
    else:
        return False

def isWhite(character):
    if(character == ' ' or character == '\n'):
        return True
    else:
        return False

with open (sys.argv[1]) as file:
    code = file.read()
    file.close

#Use Leading/Trailing pointers to create list of lexemes

lead = 0
trail = 0
lexList = []

#Please god save us from Python's lack of switch cases and my own love for spaghetti
while(lead < len(code)):
    if(isChar(code[lead])):
        while(isChar(code[lead])):
            lead += 1
        lexList.append(code[trail:lead])
    
    elif(isWhite(code[lead])):
        while(isWhite(code[lead])):
            lead += 1
        lexList.append(code[trail:lead])
    
    elif(isNum(code[lead])):
        while(isNum(code[lead])):
            lead += 1
        lexList.append(code[trail:lead])
    
    elif(code[lead] == '('):
        lead += 1
        lexList.append('(')
    
    elif(code[lead] == ')'):
        lead += 1
        lexList.append(')')
    
    elif(code[lead] == '\"' or code[lead] == '\''):
        lead += 1
        lexList.append('\"')
    
    elif(code[lead] == ':'):
        lead += 1
        lexList.append(':')
    
    elif(code[lead] == '='):
        lead += 1
        if(code[lead] == '='):
            lexList.append('==')
            lead += 1
        else:
            lexList.append('=')

    elif(code[lead] == '.'):
        lead += 1
        lexList.append('.')
    
    elif(code[lead] == ','):
        lead += 1
        lexList.append(',')
    
    elif(code[lead] == '>'):
        lead += 1
        lexList.append('>')
    
    elif(code[lead] == '<'):
        lead += 1
        lexList.append('<')
    
    elif(code[lead] == '+'):
        lead += 1
        lexList.append('+')
    
    elif(code[lead] == '-'):
        lead += 1
        lexList.append('-')
    
    elif(code[lead] == '*'):
        lead += 1
        lexList.append('*')
    
    elif(code[lead] == '/'):
        lead += 1
        lexList.append('/')
    
    elif(code[lead] == '\\'):
        lead += 1
        lexList.append('\\')

    elif(code[lead] == '['):
        lead += 1
        lexList.append('[')
    
    elif(code[lead] == ']'):
        lead += 1
        lexList.append(']')
    
    elif(code[lead] == '#'):
        lead += 1
        lexList.append('#')

    elif(code[lead] == '!'):
        lead += 1
        lexList.append('!')
    
    elif(code[lead] == '\t'):
        lead += 1
        lexList.append('\t')

    trail = lead

classList = []

#The carnage continues, none shall survive his noodley wrath  
for x in lexList:
    print(x)