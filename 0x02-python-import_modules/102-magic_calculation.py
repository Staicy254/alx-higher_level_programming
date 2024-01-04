def magic_calculation(a, b):
    add = __import__('magic_calculation_102', globals(), locals(), ['add'], 0).__dict__['add']
    sub = __import__('magic_calculation_102', globals(), locals(), ['sub'], 0).__dict__['sub']

    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
