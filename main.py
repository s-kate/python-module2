def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        rev_str = string[-1] + reverse_string(string[:-1])
        return rev_str


print(reverse_string("Hello"))
