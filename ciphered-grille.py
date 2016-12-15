# функция поиска координат иксов.
def part(cipher_grille, ciphered_password):
    for i in range(0,4):
        try:
        cipher_grille[i].find("X")

def rotate90(cipher_grille):
    


def recall_password(cipher_grille, ciphered_password):
    return ""

part = ""
pwd = ""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
