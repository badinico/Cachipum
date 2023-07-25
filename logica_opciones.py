def log_tijera(p1, p2):
    if p1 == 'tijera' and p2 == 'piedra':
        return False, True
    elif p1 == 'tijera' and p2 == 'papel':
        return True, False
    elif p1 == 'tijera' and p2 == 'tijera':
        return False, False

def log_papel(p1, p2):
    if p1 == 'papel' and p2 == 'tijera':
        return False, True
    elif p1 == 'papel' and p2 == 'piedra':
        return True, False
    elif p1 == 'papel' and p2 == 'papel':
        return False, False

def log_piedra(p1, p2):
    if p1 == 'piedra' and p2 == 'papel':
        return False, True
    elif p1 == 'piedra' and p2 == 'tijera':
        return True, False
    elif p1 == 'piedra' and p2 == 'piedra':
        return False, False