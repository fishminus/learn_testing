def capitalize_function(x):
    if not isinstance(x, str):
        raise TypeError("Please string me up")
    return x.capitalize()