def add_int(a, b):
    if not isinstance(a, int):
        raise TypeError("int 타입만 연산 가능")

    if not isinstance(b, int):
        raise  TypeError("int 타입만 연산 가능")

    return a+b
