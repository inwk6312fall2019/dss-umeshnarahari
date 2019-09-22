def nested_sum(values):
    total = 0
    for items in values:
        for nested in items:
            total += nested
    return total
