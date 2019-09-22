def capitalize_nested(strings):
    res = []
    for items in strings:
        for nested in items:
            res.append(nested.capitalize())
    return res
