def array_to_string (arr_):
    str_ = ','.join(str(x) for x in arr_)
    return str_

def string_to_array (str_):
    arr_ = [int(x) for x in str_.split(",")]
    return arr_
