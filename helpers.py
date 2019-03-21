def sort(flist, att='signature_count'):
    length = len(flist)
    if length == 0:
        return []

    my_list = []
    for i in range(0, length):
        lowest = flist[0]
        length = len(flist)
        for j in range(0, length):
            if flist[j].get(att) < lowest.get(att):
                lowest = flist[j]
        flist.remove(lowest)
        my_list.append(lowest)

    return my_list
