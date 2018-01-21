# -*- coding: utf-8 -*-


if __name__ == '__main__':

    s1 = []
    s2 = []
    all_area = 0
    
    for i, c in enumerate(input()):
        if c == "\\":
            s1.append([c, i])
        elif c == "/":
            if len(s1) > 0:
                _, j = s1.pop()
                area = i - j
                all_area += area

                while len(s2)>0 and s2[-1][0]>j:
                    area += s2.pop()[1]
                s2.append([j, area])
                
    print(all_area)
    ret = [len(s2)]
    for w in s2:
        ret.append(w[1])
    print(" ".join(map(str, ret)))
