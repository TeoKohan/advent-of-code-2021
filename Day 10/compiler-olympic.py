I = [line.strip() for line in open('input')]

braces = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

corrupt_score = {
    False: 0,
    ')'  : 3,
    ']'  : 57,
    '}'  : 1197,
    '>'  : 25137
}

autocomplete_score = {
    ')'  : 1,
    ']'  : 2,
    '}'  : 3,
    '>'  : 4
}

def is_corrupt(L):
    type(L)
    stack = []
    for i in L:
        if i in braces.keys():
            stack.append(i)
        elif len(stack) <= 0 or braces[stack.pop()] != i:
            return i
    return False

corruption = [is_corrupt(line) for line in I]
corrupt_score = sum([corrupt_score[p] for p in corruption])

def closing(L):
    type(L)
    stack = []
    for i in L:
        if i in braces.keys():
            stack.append(i)
        else:
            stack.pop()
    return stack

def calculate_score(L):
    score = 0
    for n in L:
        score *= 5
        score += n
    return score

incomplete = [L for L in I if is_corrupt(L) == False]
incomplete = [closing(L) for L in incomplete]
incomplete = [[autocomplete_score[braces[p]] for p in L] for L in incomplete]
incomplete = [calculate_score(reversed(L)) for L in incomplete]
incomplete.sort()
incomplete_score = incomplete[len(incomplete)//2]
output = open('output', 'w')
output.write(str(corrupt_score)+'\n'+str(incomplete_score)+'\n')
output.close()