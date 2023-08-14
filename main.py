def depth(list_box):
    if not isinstance(list_box, list):
        return 0
    elif not list_box:
        return 1
    else:
        count = 1
        for item in list_box:
            count += depth(item)
        return count


print(depth([]))
print(depth([1, [2, [3, [4, [5]]]]]))
