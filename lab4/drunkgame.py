# Напишите программу drunkgame.py, которая моделирует вариацию карточной игры “пьяница”.
# На вход в виде строки подается колода из четного количества карт, обозначаемых целыми числами,
# например, “1 3 2 5 4 8”. Эта колода разделяется пополам между двумя игроками
# (первый игрок забирает себе первую половину колоды, второй – вторую) и начинается игра.
# На каждом ходу игроки выкладывают по одной левой карте:
#
#     игрок со старшей картой (9 > 3, 2 > 1 и т.д.) забирает обе карты и кладет в правый конец своей колоды
#     (например, для p1=3 2, p2=1 4 получаем после хода p1=2 3 1, p2=4)
#     если выложены одинаковые карты, то игроки начинают выкладывать по одной карте пока кто-то не выиграет –
#     выигравший забирает все карты (например, для p1=4 5 2 1, p2=4 5 3 получаем после хода p1=1, p2=4 4 5 5 3 2)
#
# Выигрывает тот, кто в конце концов соберет у себя все карты. Программа выводит начальную позицию и все ходы до
# завершения игры. Важно: Программа должна быть построена с использованием дек, списков внутри не должно быть.

import sys
from queuedummy import Queue
def getPlayers(inpt):
    p1, p2 = Queue(), Queue()
    for i in range(0, len(inpt) // 2):
        p1.enqueue(inpt[i])

    for i in range(len(inpt) // 2  , len(inpt)):
        p2.enqueue(inpt[i])
    return p1, p2

def play(pl1,pl2):
    while not pl1.is_empty() and not pl2.is_empty():
        pl1_move = pl1.dequeue()
        pl2_move = pl2.dequeue()

        if pl1_move > pl2_move:
            pl1.enqueue(pl1_move)
            pl1.enqueue(pl2_move)
        elif pl1_move < pl2_move:
            pl2.enqueue(pl2_move)
            pl2.enqueue(pl1_move)
        else:
            tempDeq = Queue()
            tempDeq.enqueue(pl1_move)
            tempDeq.enqueue(pl2_move)
            while pl1_move == pl2_move:
                pl1_move = pl1.dequeue()
                pl2_move = pl2.dequeue()
                tempDeq.enqueue(max(pl1_move, pl2_move))
                tempDeq.enqueue(min(pl1_move, pl2_move))
            #print(f"items: {tempDeq.items}")
            if pl1_move > pl2_move:
                for i in range(len(tempDeq.items)):
                    move = tempDeq.dequeue()
                    pl1.enqueue(move)
            elif pl1_move < pl2_move:
                for i in range(len(tempDeq.items)):
                    move = tempDeq.dequeue()
                    pl2.enqueue(move)
        print(f"p1: {' '.join([i for i in pl1.items])}")
        print(f"p2: {' '.join([i for i in pl2.items])}")
        print(' ')

if __name__ == '__main__':
    inp = sys.argv[1]
    #inp ='2 8 4 6 1 5 3 8 3 7 4 7 6 2 1 5'
    inp = inp.split(' ')
    pl1 = getPlayers(inp)[0]
    pl2 = getPlayers(inp)[1]
    print(f"p1: {' '.join([i for i in pl1.items])}")
    print(f"p2: {' '.join([i for i in pl2.items])}")
    print(' ')

    play(pl1,pl2)
