# Replace the "ANSWER HERE" with your answer
    
    def remove_elements(txt):
        if len(txt) == 0
            return txt
        else:
            del txt[0]

            if len(txt) >= 5:
                del txt[3:5]
                return txt
            elif len(txt) ==4
                del txt[3]
                return txt
            else:
                return txt

def add_elements(add1):
        add1.insert(0, "pink")
        add1.append("yellow")
        return add1

def is_empty(check):
    return len(check)== 0


def check_lists(compare1, compare2):
    if len(compare1) >= 3 and len(compare2) >=3:
        return (compare1[2] == compare2[2])
    else:
        return False

def list_of_lists(str):
    tx1 = str[0][0:2]
    tx2 = str[1][1:4]
    tx3 = str[2][-2:]
    return [tx1, tx2, tx3]
