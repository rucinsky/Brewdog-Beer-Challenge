import requests


def check_if_value_is_float(value)->bool:
    return isinstance(value,float)

def check_if_value_is_int(value)->bool:
    return isinstance(value, int)

def check_if_value_not_null(value)->bool:
    return value is not None

def check_if_not_empty_string(value)->bool:
    if isinstance(value,str):
        if not value:
            return False
        else:
            return True
    else:
        return True

def check_if_value_higher(value:float, compare:float)->bool:
    return value>compare

def check_if_value_higher_or_equal(value:float, compare:float)->bool:
    return value>=compare

def check_if_website_is_up(website:str)->bool:
    try:
        status = requests.head(website)
        return status.status_code == 200
    except:
        return False

