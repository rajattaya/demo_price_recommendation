
def get_valid_consistent_string(data_string):
    """
    convert the string to lower case in case of none/null(string) return None
    :param data_string:
    """
    res_str = str(data_string).lower()
    res_str = res_str if res_str not in {'none', 'null'} else None
    return res_str
