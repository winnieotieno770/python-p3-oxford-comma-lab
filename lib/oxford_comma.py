def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    
    if len(items) >= 3:
        txt = ", ".join(items[:-1]) + f", and {items[-1]}"
        return txt

print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))
