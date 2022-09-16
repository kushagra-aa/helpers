
def replace_null_with_string(req, str=''):
    """_summary_
    Replaces NULL in the list or dictionary with the given string(or '')
    Args:
        req (list/dict): Array/Dict to modify
        str (str, optional): String want to replace with - Defaults to ''.

    Returns:
        Result: modified Array/Dict
    """
    if type(req) == dict:
        for i in req:
            if req[i] == 'NULL' or req[i] == None or req[i] == 'None' or req[i] == 'null':
                req[i] = str
    if type(req) == list:
        for obj in req:
            for i in obj:
                if obj[i] == 'NULL' or obj[i] == None or obj[i] == 'None' or obj[i] == 'null':
                    obj[i] = ''
                elif type(obj[i]) == int:
                    obj[i] = str(obj[i])
    return req


def replace_with_string(req, target, str='', isSensitive=True):
    """_summary_
    Replaces target string in the list or dictionary with the given string(or '')
    Args:
        req (list/dict): Array/Dict to modify
        target (str): String want to replace with - Defaults to ''.
        str (str, optional): String want to replace with - Defaults to ''.
        isSensitive (bool, optional): If the check is Case Sensitive.

    Returns:
        Result: modified Array/Dict
    """
    if type(req) == dict:
        for i in req:
            if not isSensitive:
                req[i] = req[i].lower()
                target = target.lower()
            if req[i] == target:
                req[i] = str
    if type(req) == list:
        for obj in req:
            for i in obj:
                if not isSensitive:
                    obj[i] = obj[i].lower()
                    target = target.lower()
                if obj[i] == target:
                    obj[i] = ''
                elif type(obj[i]) == int:
                    obj[i] = str(obj[i])
    return req
