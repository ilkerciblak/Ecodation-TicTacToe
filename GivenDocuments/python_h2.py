###############################################################
# Bu program:
# - Inline iç-içe for ile [[1, 2, 3], [4, 'X', 6], [7, 8, 9]] çok boyutlu liste oluşturur
# - Randrange fonksiyonu için random modülü ekler
# - For döngüsü ile board'u ekrana basar
# - Digit olarak seçilen karelerin (1, 2, 3, 4,  6 ...) 
# - Matrise dönüştülmesini sağlar 1 → [0][0], 2 → [0][1], 3 → [0][2], 4 → [1][0], 6 → [1][2] gibi 
# - Belirli aralıkta değer girdirmeyi başarır 
# - break-continue doğru anda kullanmayı bilir
#
# Öğrenci:
# 1. Randrange fonksiyonu için kütüphaneleri import edecek.
# 2. Oyunun Başlangıcında ve Oyunun Herhangi Bir Anında Board'u Görüntüleyecek
# 3. Oyuncu Kare Seçecek → O
# 4. Seçili Olmayan Kareleri Belirleyecek
# 5. Kazananı Belirleyecek
# 6. PC Kare Seçecek → X
# 7. Main Block Tasarlayacak
###############################################################

# 1 → Randrange fonksiyonu için kütüphaneleri import edelim.
<!!!buradaki kodu değiştir>

# 2 → Oyunun Başlangıcında ve Oyunun Herhangi Bir Anında Board'u Görüntüleyelim
def DisplayBoard(board):
    print("<!!!buradaki kodu değiştir>" * 3, "+", sep="")
    for row in range(3):
        print("<!!!buradaki kodu değiştir>" * 3, "|", sep="")
        for col in range(3):
            print("<!!!buradaki kodu değiştir>" + str(board[row][col]) + "   ", end="")
        print("<!!!buradaki kodu değiştir>")
        print("<!!!buradaki kodu değiştir>" * 3, "|", sep="")
        print("<!!!buradaki kodu değiştir>" * 3, "+", sep="")

# 3 → Oyuncu Kare Seçiyor → O
def EnterMove(board):
    ok = False
    while not ok:
        move = int(input("Lütfen Kare Seçin [1-9]: "))
        ok = <!!!buradaki kodu değiştir>  # kullanıcı girişi doğru aralıkta mı?
        if not ok:
            print("[1-9] Arası Kare Seçmediniz. Lütfen Tekrar Giriniz!")
            continue
        move = <!!!buradaki kodu değiştir> 	# bu üç satır çok önemli. seçili digit değerine sahip kareyi
        row = <!!!buradaki kodu değiştir> 	# [row][col] değerine dönüştürmeliyiz. Örn
        col = <!!!buradaki kodu değiştir>		# 1 → [0][0], 2 → [0][1], 3 → [0][2], 4 → [1][0], 6 → [1][2] gibi 
        sign = board[?][?]  # seçili kareyi oku
        ok = sign not in ['O', 'X']
        if not ok:  # seçili kare dolu ise tekrar denenmeli
            print("Seçili Kare. Lütfen Tekrar Giriniz!")
            continue
    board[?][?] = <!!!buradaki kodu değiştir>    	# seçili kareyi '0' olarak set et

# 4 → Seçili Olmayan Kareleri Belirleme
def MakeListOfFreeFields(board):
    free = []  # boş liste tanımlanıyor
    for row in range(3):  # rows
        for col in range(3):  # columns
            if <!!!buradaki kodu değiştir> not in ['O', 'X']:  # boş kare mi?
                # evet ise append et
                <!!!buradaki kodu değiştir>
    return free

# 5 → Kazananı Belirleyelim
def VictoryFor(board, sgn):
    if sgn == "X":  # X için mi board'u kontrol edecek?
        who = 'me'  # PC
    elif sgn == "O":  # O için mi board'u kontrol edecek?
        who = 'you'  # Kullanıcı
    cross1 = cross2 = True  # for diagonals
    for rc in range(3):
        if <!!!buradaki kodu değiştir>:  # satırları kontrol edelim
            return who
        if <!!!buradaki kodu değiştir>:  # sütunları kontrol edelim
            return who
        if <!!!buradaki kodu değiştir> != sgn:  # 1. köşegeni kontrol edelim
            cross1 = False
        if <!!!buradaki kodu değiştir> != sgn:  # 2. köşegeni kontrol edelim
            cross2 = False
    if cross1 or cross2:
        return who
    return None

# 6 → PC Kare Seçiyor → X
def DrawMove(board):
    free = MakeListOfFreeFields(board)  # boş olan karelerden bir liste tanımlayalım
    cnt = len(free)
    if cnt > 0:  # list boş değil ise, 'X' i set edeceğimiz kareyi random seçelim
        this = randrange(cnt)
        row, col = <!!!buradaki kodu değiştir>
        board[?][?] = <!!!buradaki kodu değiştir>

# 7 → main
board = [[<!!!buradaki kodu değiştir> for j in range(3)] for i in range(3)]
#print(board) #[[1, 2, 3], [4, 5 , 6], [7, 8, 9]]
board[?][?] = 'X'  # ortadaki kareyi 'X' olarak set et
#print(board) #[[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
free = MakeListOfFreeFields(board)
humanturn = True  # sıra kim de? önce oyuncu başlayacak
while len(free):
    DisplayBoard(board)
    if humanturn:
        EnterMove(board)
        victor = VictoryFor(board, 'O')
    else:
        DrawMove(board)
        victor = VictoryFor(board, 'X')
    if victor != None:
        break
    humanturn = <!!!buradaki kodu değiştir>
    free = MakeListOfFreeFields(board)

DisplayBoard(board)
if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won")
else:
    print("Tie!")