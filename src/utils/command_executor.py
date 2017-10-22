import re

def parse_order_string(order_string):
    comm = -1
    arg1 = None
    arg2 = None
    arg3 = None
    if order_string.startswith('put'):
        comm = 1
        both_arg  = re.search(r'\((.*?),(.*?)\)',order_string)
        arg1 = both_arg.group(1).replace("'", "")
        arg2 = both_arg.group(2).replace("'", "")
    elif order_string.startswith('get'):
        comm = 2
        arg1 = re.search(r'\((.*?)\)',order_string).group(1).replace("'", "")
    elif order_string.startswith('slice'):
        comm = 3
        all_arg = re.search(r'\((.*?),(.*?):(.*?)\)',order_string)
        arg1 = all_arg.group(1).replace("'", "")
        arg2 = all_arg.group(2).replace("'", "")
        arg3 = all_arg.group(3).replace("'", "")
    elif order_string.startswith('append'):
        comm = 4
        both_arg  = re.search(r'\((.*?),(.*?)\)',order_string)
        arg1 = both_arg.group(1).replace("'", "")
        arg2 = both_arg.group(2).replace("'", "")
    return comm, arg1, arg2, arg3


def get_result(order_string, running_state):
    # command parsing 
    #  1 - >  put (arg1, arg2)
    #  2 - >  get (arg1)    arg2 is None
    #  3 - >  slice (arg1, arg2:arg3)
    #  4 - >  append (arg1, arg2)
    comm, arg1, arg2, arg3 = parse_order_string(order_string)
    result = ""
    if comm == 1:
        running_state[arg1] = arg2
        result = "OK"
    elif comm == 2:
        if arg1 in running_state:
            result = running_state[arg1]
    elif comm == 3:
        if arg1 in running_state:
            curr_val = running_state[arg1]
            if int(arg2) >= 0 and int(arg3) <= len(curr_val) and int(arg2) <= int(arg3):
                running_state[arg1] = curr_val[ int(arg2) : int(arg3) ]
                result = "OK"
        else:
            result = "FAIL"
    elif comm == 4:
        if arg1 in running_state:
            curr_value = running_state[arg1]
            running_state[arg1] = curr_value + arg2
            result = "OK"
        else:
            result = "FAIL"
    else:
        print("Unrecognized command : ", order_string )
        return None
    return result
