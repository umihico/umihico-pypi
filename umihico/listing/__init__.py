
def chunks(list_, chunk_len):
    '''
    chunks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    >> [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    '''
    return list(list_[i:i + chunk_len] for i in range(0, len(list_), chunk_len))


def flatten(list_of_list):
    '''
    flatten([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]])
    >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
    return [x for list_ in list_of_list for x in list_]
