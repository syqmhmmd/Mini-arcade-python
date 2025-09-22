import pygame, random, sys, os

pygame.init()
pygame.mixer.init()

# --- Konfigurasi Layar ---
WIDTH, HEIGHT = 800, 600
LAYAR = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Game Arcade")
clock = pygame.time.Clock()
fullscreen = False

# --- Warna ---
PUTIH = (255, 255, 255)
HITAM = (0, 0, 0)
HIJAU = (0, 255, 0)
MERAH = (255, 0, 0)
BIRU = (0, 150, 255)
BIRU_TERANG = (0, 200, 255)
ABU = (40, 40, 40)
KUNING = (255, 255, 0)

# --- Font ---
font = pygame.font.SysFont("arial", 32, True)
title_font = pygame.font.SysFont("arial", 56, True)
small_font = pygame.font.SysFont("arial", 24, False)

# --- Sound ---
def load_sound(path):
    if os.path.exists(path):
        try:
            s = pygame.mixer.Sound(path)
            s.set_volume(1.0)
            return s
        except:
            return None
    return None

pop_sound = load_sound("sounds/pop.wav")
beep_sound = load_sound("sounds/beep.wav")
ding_sound = load_sound("sounds/ding.wav")
buzz_sound = load_sound("sounds/buzz.wav")

# --- Background Music ---
music_muted = False  # status mute

def play_music(path):
    global music_muted
    if os.path.exists(path):
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(0.0 if music_muted else 0.5)
            pygame.mixer.music.play(-1)  # looping
            print(f"Playing: {path}")
        except Exception as e:
            print(f"Gagal load musik {path}: {e}")
    else:
        print(f"File tidak ditemukan: {path}")

def stop_music():
    pygame.mixer.music.stop()

def toggle_music():
    global music_muted
    music_muted = not music_muted
    if music_muted:
        pygame.mixer.music.set_volume(0.0)
        print("Musik dimute")
    else:
        pygame.mixer.music.set_volume(0.5)
        print("Musik unmute")

# --- Toggle Fullscreen ---
def toggle_fullscreen():
    global LAYAR, fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        LAYAR = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    else:
        LAYAR = pygame.display.set_mode((WIDTH, HEIGHT))

# --- Countdown ---
def countdown():
    for angka in ["3", "2", "1", "GO!"]:
        LAYAR.fill(HITAM)
        teks = title_font.render(angka, True, KUNING)
        LAYAR.blit(teks, (WIDTH//2 - teks.get_width()//2, HEIGHT//2 - teks.get_height()//2))
        pygame.display.flip()
        pygame.time.delay(1000)

# --- Pilihan Mode ---
def choose_mode(game):
    while True:
        LAYAR.fill(ABU)
        judul = title_font.render(f"{game} - Pilih Mode", True, KUNING)
        LAYAR.blit(judul, (WIDTH//2 - judul.get_width()//2, 70))

        instruksi1 = small_font.render("P1 = WASD", True, PUTIH)
        instruksi2 = small_font.render("P2 = Panah", True, PUTIH)
        instruksi3 = small_font.render("ESC = Kembali ke Menu", True, PUTIH)
        instruksi4 = small_font.render("F11 = Toggle Fullscreen", True, PUTIH)
        instruksi5 = small_font.render("M = Mute/Unmute Musik", True, PUTIH)
        LAYAR.blit(instruksi1, (WIDTH//2 - instruksi1.get_width()//2, 150))
        LAYAR.blit(instruksi2, (WIDTH//2 - instruksi2.get_width()//2, 180))
        LAYAR.blit(instruksi3, (WIDTH//2 - instruksi3.get_width()//2, 210))
        LAYAR.blit(instruksi4, (WIDTH//2 - instruksi4.get_width()//2, 240))
        LAYAR.blit(instruksi5, (WIDTH//2 - instruksi5.get_width()//2, 270))

        tombol_1p = pygame.Rect(WIDTH//2 - 150, 320, 300, 60)
        tombol_2p = pygame.Rect(WIDTH//2 - 150, 400, 300, 60)
        tombol_back = pygame.Rect(WIDTH//2 - 150, 480, 300, 60)

        pygame.draw.rect(LAYAR, BIRU, tombol_1p, border_radius=12)
        pygame.draw.rect(LAYAR, BIRU, tombol_2p, border_radius=12)
        pygame.draw.rect(LAYAR, MERAH, tombol_back, border_radius=12)

        LAYAR.blit(font.render("1 Player", True, PUTIH), (tombol_1p.centerx-60, tombol_1p.centery-15))
        LAYAR.blit(font.render("2 Player", True, PUTIH), (tombol_2p.centerx-60, tombol_2p.centery-15))
        LAYAR.blit(font.render("Kembali", True, PUTIH), (tombol_back.centerx-60, tombol_back.centery-15))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    toggle_fullscreen()
                if event.key == pygame.K_m:
                    toggle_music()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tombol_1p.collidepoint(event.pos):
                    return 1
                if tombol_2p.collidepoint(event.pos):
                    return 2
                if tombol_back.collidepoint(event.pos):
                    return None

        pygame.display.flip()
        clock.tick(30)

# --- Menu ---
def menu():
    play_music("sounds/terima-kasih-pak-jokowi-jokowi-128-ytshorts.savetube.me.mp3")
    while True:
        LAYAR.fill(ABU)
        judul = title_font.render("Mini Game Arcade", True, KUNING)
        LAYAR.blit(judul, (WIDTH//2 - judul.get_width()//2, 80))

        tombol_snake = pygame.Rect(WIDTH//2 - 180, 250, 360, 60)
        tombol_pong  = pygame.Rect(WIDTH//2 - 180, 350, 360, 60)
        tombol_exit  = pygame.Rect(WIDTH//2 - 180, 450, 360, 60)

        pygame.draw.rect(LAYAR, BIRU, tombol_snake, border_radius=12)
        pygame.draw.rect(LAYAR, BIRU, tombol_pong, border_radius=12)
        pygame.draw.rect(LAYAR, MERAH, tombol_exit, border_radius=12)

        LAYAR.blit(font.render("Snake", True, PUTIH), (tombol_snake.centerx-50, tombol_snake.centery-15))
        LAYAR.blit(font.render("Pong", True, PUTIH), (tombol_pong.centerx-40, tombol_pong.centery-15))
        LAYAR.blit(font.render("Keluar", True, PUTIH), (tombol_exit.centerx-50, tombol_exit.centery-15))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    toggle_fullscreen()
                if event.key == pygame.K_m:
                    toggle_music()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tombol_snake.collidepoint(event.pos):
                    stop_music()
                    mode = choose_mode("Snake")
                    if mode:
                        countdown()
                        snake(mode)
                    play_music("sounds/terima-kasih-pak-jokowi-jokowi-128-ytshorts.savetube.me.mp3")
                if tombol_pong.collidepoint(event.pos):
                    stop_music()
                    mode = choose_mode("Pong")
                    if mode:
                        countdown()
                        pong(mode)
                    play_music("sounds/raja-tipu-tipu-128-ytshorts.savetube.me.mp3")
                if tombol_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(30)

# --- Game Snake ---
def snake(mode=1):
    play_music("sounds/ayo-ayo-ganyang-fufufafa-memes-memeabsurd-masukberanda-fyp-128-ytshorts.savetube.me.mp3")
    grid = 20
    ular1 = [pygame.Rect(WIDTH//3, HEIGHT//2, grid, grid)]
    arah1 = (grid, 0)
    skor1 = 0

    ular2 = [pygame.Rect(2*WIDTH//3, HEIGHT//2, grid, grid)] if mode==2 else []
    arah2 = (-grid, 0)
    skor2 = 0

    makanan = pygame.Rect(random.randrange(0, WIDTH, grid), random.randrange(0, HEIGHT, grid), grid, grid)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop_music()
                    return
                if event.key == pygame.K_F11:
                    toggle_fullscreen()
                if event.key == pygame.K_m:
                    toggle_music()
                if event.key == pygame.K_w and arah1 != (0, grid): arah1 = (0, -grid)
                if event.key == pygame.K_s and arah1 != (0, -grid): arah1 = (0, grid)
                if event.key == pygame.K_a and arah1 != (grid, 0): arah1 = (-grid, 0)
                if event.key == pygame.K_d and arah1 != (-grid, 0): arah1 = (grid, 0)
                if mode==2:
                    if event.key == pygame.K_UP and arah2 != (0, grid): arah2 = (0, -grid)
                    if event.key == pygame.K_DOWN and arah2 != (0, -grid): arah2 = (0, grid)
                    if event.key == pygame.K_LEFT and arah2 != (grid, 0): arah2 = (-grid, 0)
                    if event.key == pygame.K_RIGHT and arah2 != (-grid, 0): arah2 = (grid, 0)

        kepala1 = ular1[0].move(arah1)
        ular1.insert(0, kepala1)
        if kepala1.colliderect(makanan):
            skor1 += 1
            if pop_sound: pop_sound.play()
            makanan = pygame.Rect(random.randrange(0, WIDTH, grid), random.randrange(0, HEIGHT, grid), grid, grid)
        else:
            ular1.pop()

        if mode==2:
            kepala2 = ular2[0].move(arah2)
            ular2.insert(0, kepala2)
            if kepala2.colliderect(makanan):
                skor2 += 1
                if pop_sound: pop_sound.play()
                makanan = pygame.Rect(random.randrange(0, WIDTH, grid), random.randrange(0, HEIGHT, grid), grid, grid)
            else:
                ular2.pop()

        def tabrakan(ular, kepala):
            return (kepala.left < 0 or kepala.right > WIDTH or kepala.top < 0 or kepala.bottom > HEIGHT or len(ular) != len(set((p.x,p.y) for p in ular)))

        if tabrakan(ular1, kepala1) or (mode==2 and tabrakan(ular2, kepala2)) or (mode==2 and kepala1.colliderect(kepala2)):
            if buzz_sound: buzz_sound.play()
            stop_music()
            return

        LAYAR.fill(HITAM)
        for bagian in ular1:
            pygame.draw.rect(LAYAR, HIJAU, bagian)
        if mode==2:
            for bagian in ular2:
                pygame.draw.rect(LAYAR, BIRU_TERANG, bagian)
        pygame.draw.ellipse(LAYAR, MERAH, makanan)

        teks1 = font.render(f"P1: {skor1}", True, HIJAU)
        LAYAR.blit(teks1, (10, 10))
        if mode==2:
            teks2 = font.render(f"P2: {skor2}", True, BIRU_TERANG)
            LAYAR.blit(teks2, (WIDTH-120, 10))

        pygame.display.flip()
        clock.tick(10)

# --- Game Pong ---
def pong(mode=1):
    play_music("sounds/raja-tipu-tipu-128-ytshorts.savetube.me.mp3")
    bola = pygame.Rect(WIDTH//2-10, HEIGHT//2-10, 20, 20)
    bola_x = 5 * random.choice((1,-1))
    bola_y = 5 * random.choice((1,-1))

    paddle_p1 = pygame.Rect(30, HEIGHT//2-60, 10, 120)
    paddle_p2 = pygame.Rect(WIDTH-40, HEIGHT//2-60, 10, 120)

    skor1 = 0
    skor2 = 0
    skor_max = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop_music()
                    return
                if event.key == pygame.K_F11:
                    toggle_fullscreen()
                if event.key == pygame.K_m:
                    toggle_music()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle_p1.top > 0: paddle_p1.y -= 7
        if keys[pygame.K_s] and paddle_p1.bottom < HEIGHT: paddle_p1.y += 7

        if mode==2:
            if keys[pygame.K_UP] and paddle_p2.top > 0: paddle_p2.y -= 7
            if keys[pygame.K_DOWN] and paddle_p2.bottom < HEIGHT: paddle_p2.y += 7
        else:
            if paddle_p2.centery < bola.centery: paddle_p2.y += 6
            if paddle_p2.centery > bola.centery: paddle_p2.y -= 6

        bola.x += bola_x
        bola.y += bola_y

        if bola.top <= 0 or bola.bottom >= HEIGHT:
            bola_y *= -1
            if beep_sound: beep_sound.play()

        if bola.colliderect(paddle_p1) or bola.colliderect(paddle_p2):
            bola_x *= -1
            if beep_sound: beep_sound.play()

        if bola.left <= 0:
            skor2 += 1
            if ding_sound: ding_sound.play()
            bola.center = (WIDTH//2, HEIGHT//2)
            bola_x = 5 * random.choice((1,-1))
            bola_y = 5 * random.choice((1,-1))
        if bola.right >= WIDTH:
            skor1 += 1
            if ding_sound: ding_sound.play()
            bola.center = (WIDTH//2, HEIGHT//2)
            bola_x = 5 * random.choice((1,-1))
            bola_y = 5 * random.choice((1,-1))

        if skor1 >= skor_max or skor2 >= skor_max:
            winner = "Player 1" if skor1 >= skor_max else "Player 2"
            stop_music()

            while True:
                LAYAR.fill(HITAM)
                teks_win = title_font.render(f"{winner} Menang!", True, KUNING)
                LAYAR.blit(teks_win, (WIDTH//2 - teks_win.get_width()//2, 150))

                tombol_try = pygame.Rect(WIDTH//2 - 120, 300, 240, 60)
                tombol_menu = pygame.Rect(WIDTH//2 - 120, 400, 240, 60)

                pygame.draw.rect(LAYAR, BIRU, tombol_try, border_radius=12)
                pygame.draw.rect(LAYAR, MERAH, tombol_menu, border_radius=12)

                LAYAR.blit(font.render("Try Again", True, PUTIH), (tombol_try.centerx - 60, tombol_try.centery - 15))
                LAYAR.blit(font.render("Menu", True, PUTIH), (tombol_menu.centerx - 40, tombol_menu.centery - 15))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F11:
                            toggle_fullscreen()
                        if event.key == pygame.K_m:
                            toggle_music()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if tombol_try.collidepoint(event.pos):
                            return pong(mode)
                        if tombol_menu.collidepoint(event.pos):
                            return

                pygame.display.flip()
                clock.tick(30)

        LAYAR.fill(HITAM)
        for y in range(0, HEIGHT, 20):
            pygame.draw.rect(LAYAR, ABU, (WIDTH//2-2, y, 4, 10))

        pygame.draw.rect(LAYAR, HIJAU, paddle_p1)
        pygame.draw.rect(LAYAR, BIRU_TERANG, paddle_p2)
        pygame.draw.ellipse(LAYAR, PUTIH, bola)

        teks = font.render(f"{skor1} - {skor2}", True, PUTIH)
        LAYAR.blit(teks, (WIDTH//2 - teks.get_width()//2, 20))

        pygame.display.flip()
        clock.tick(60)

# --- Jalankan ---
menu()
