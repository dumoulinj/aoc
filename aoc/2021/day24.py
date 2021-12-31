# a:
# b:

with open('ex24.txt') as infile:
   lines = infile.readlines()

def check_monad(model):
    variables = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    m_idx = 0
    for l in lines:
        _l = l.strip().split(' ')
        if len(_l) == 2:
            a = _l[1]
            variables[a] = int(model[m_idx])
            m_idx += 1
        else:
            op = _l[0]
            a = _l[1]

            try:
                b = int(_l[2])
            except:
                b = variables[_l[2]]

            if op == "add":
                variables[a] = variables[a] + b
            elif op == "mul":
                variables[a] = variables[a] * b
            elif op == "div":
                assert b != 0
                variables[a] = variables[a] // b
            elif op == "mod":
                assert variables[a] >= 0
                assert b > 0
                variables[a] = variables[a] % b
            elif op == "eql":
                variables[a] = 1 if variables[a] == b else 0

    return variables["z"]

def check_monads():
    i = 0
    j = -1 
    total = 9e14

    a = 1
    b = 10
    s = 1
    r = False

    ans = -1
    for _1 in range(a, b, s):
        for _2 in range(a, b, s):
            for _3 in range(a, b, s):
                for _4 in range(a, b, s):
                    for _5 in range(a, b, s):
                        for _6 in range(a, b, s):
                            for _7 in range(a, b, s):
                                for _8 in range(a, b, s):
                                    for _9 in range(a, b, s):
                                        for _10 in range(a, b, s):
                                            for _11 in range(a, b, s):
                                                for _12 in range(a, b, s):
                                                    for _13 in range(a, b, s):
                                                        for _14 in range(a, b, s):
                                                            k = int(i / total * 100)
                                                            if k != j:
                                                                j = k
                                                                print(f"{j}%")

                                                            i += 1
                                                            m = str(_1) + str(_2) + str(_3) + str(_4) + str(_5) + str(_6) + str(_7) + str(_8) + str(_9) + str(_10) + str(_11) + str(_12) + str(_13) + str(_14)
                                                            # assert len(m) == 14
                                                            # assert "0" not in m
                                                            if check_monad(m) == 0:
                                                                if r:
                                                                    return m
                                                                else:
                                                                    ans = m
    return ans
res = check_monads()
print("part a: {}".format(res))
#puzzle.answer_a = res 

#print("part b: {}".format(res))
#puzzle.answer_b = res 