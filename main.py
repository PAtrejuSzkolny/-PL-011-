def get_liczby():
    with open('.\liczby.txt', 'r') as file:
        liczby = file.read().strip().split(';')
        final = []
        for i, val in enumerate(liczby):
            try:
                final.append(int(val))
            except Exception:
                raise Exception(f"Invalid input, can't make int out of '{val}'")
        try:
            if





print(get_liczby())


