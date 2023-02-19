# convert items in a string which is separated by ", "
def oxford_comma(items):
    length = len(items)
    if length == 1:
        return items[0]
    elif length == 2:
        return " and ".join(items)
    else:
        if length >= 3:
            return ", and ".join([", ".join(item for item in items[0: -1]), items[-1]])
