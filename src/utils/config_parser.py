import pprint

def get_config(full_path):
    with open(full_path,'r') as f:
        config = {}
        for line in f:
            if line[0] != '#':
                (key,sep,val) = line.partition('=')
                # if the line does not contain '=', it is invalid and hence ignored
                if len(sep) != 0:
                    val = val.strip()
                    config[key.strip()] = int(val) if str.isdecimal(val) else val
        return config            

def print_config(full_path):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(get_config(full_path))
