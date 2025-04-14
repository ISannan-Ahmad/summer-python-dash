def append_to_list(val, list = None) -> list[int]:
    
    if list is None:
        list = []
    list.append(val)
    return list