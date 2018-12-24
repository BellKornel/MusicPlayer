# ~*~ coding: utf-8 ~*~

if __name__ == '__main__':
    import pygame
    import easygui
    from getpass import getuser
    from os import walk
    from random import choice
    from mutagen.mp3 import MP3


    class ClassCounter:
        __number = 0

        def plus(self):
            self.__number += 1
            return self.__number-1

        def current_number(self):
            return self.__number

        def drop_number(self):
            self.__number = 0


    class Music:
        counter = ClassCounter()
        alpha = 150
        status = 0
        sn = -1
        d = 0

        def __init__(self, m, p):
            self.music = m
            self.path = p
            self.n = self.counter.plus()
            self.music_length = MP3(p+m).info.length
            self.frequency = MP3(p+m).info.sample_rate/frequency
            warning = ''
            if self.frequency != 1:
                '''
                print('Warning!',
                      'Music with number '+str(self.n+1)+' and name '+str(self.music)+' has another frequency!',
                      'Coefficient = '+str(self.frequency)+'. MusicPlayer can\'t change frequency!')
                '''
                warning += ' [another frequency]'

            length_s = str(int(self.music_length) % 60)
            length_m = str(int(self.music_length) // 60)

            if len(length_s) == 1:
                length_s = '0'+length_s
            if len(length_m) == 1:
                length_m = '0'+length_m

            self.time = label.render(length_m+':'+length_s, 1, black)
            self.text = label.render(self.music[0:-4]+warning, 1, black)

            bias = 0
            while self.text.get_rect()[2] > 690-self.time.get_rect()[2]:
                bias += 1
                dots = '...'
                self.text = label.render(self.music[0:-4-bias]+dots+warning, 1, black)

            self.main = pygame.Surface((700, 36))
            self.color = list(white)

            self.main.set_alpha(self.alpha)
            self.main.fill(white)
            self.main.blit(self.text, (5, 3))
            self.main.blit(self.time, (700-self.time.get_rect()[2], 3))

        def check_status(self):
            if self.counter.current_number()-1 > self.n:
                if self.status:
                    return self.n
                else:
                    return musics[self.n+1].check_status()
            else:
                if self.status:
                    return self.n
                else:
                    return -1

        def del_status(self):
            if self.counter.current_number()-1 > self.n:
                if self.status:
                    self.status = 0
                musics[self.n+1].del_status()
            else:
                if self.status:
                    self.status = 0

        def move_color(self, f, t):
            f, t = list(f), list(t)
            self.color[0] -= (f[0]-t[0])/(FPS/5)
            self.color[1] -= (f[1]-t[1])/(FPS/5)
            self.color[2] -= (f[2]-t[2])/(FPS/5)
            try:
                self.main.fill(self.color)
            except TypeError:
                self.color = t
                self.main.fill(self.color)
            self.main.blit(self.text, (5, 3))
            self.main.blit(self.time, (700-self.time.get_rect()[2], 3))

        def set_sn(self, n):
            self.sn = n
            if n != -1:
                return self

        def render(self):
            global mouseButton, status
            if self.status and self.color != list(current_color):
                self.move_color(white, current_color)
            elif not self.status and self.color != list(white):
                self.move_color(current_color, white)
            if self.sn == -1:
                if self.d > 0 and len(find_text) == 0:
                    self.d -= 150/FPS
                elif self.d < 0:
                    self.d = 0
                if len(find_text) > 0 and self.alpha > 0:
                    self.alpha -= 750/FPS
                    self.main.set_alpha(self.alpha)
            else:
                if self.n*38+self.d < 50+self.sn*38:
                    self.d += (self.n+1)*38/((FPS*2)/5)
                    if self.n*38+self.d > 50+self.sn*38:
                        self.d = 50+self.sn*38 - self.n*38
                elif self.n*38+self.d > 50+self.sn*38:
                    self.d -= (Music.counter.current_number()-self.n)*38/((FPS*2)/5)
                    if self.n*38+self.d < 50+self.sn*38:
                        self.d = 50+self.sn*38 - self.n*38
            if -36 < 15+self.n*38+level+self.d < 330 and (self.sn != -1 and len(find_text) > 0 or len(find_text) == 0):
                if 50 <= mp[0] <= 750 and 15+self.n*38+level+self.d <= mp[1] <= 51+self.n*38+level+self.d and\
                        mp[1] < 330:
                    if self.alpha < 250 and (len(find_text) == 0 or self.sn != -1):
                        self.alpha += 750/FPS
                        self.main.set_alpha(self.alpha)
                    if mouseButton:
                        mouseButton = 0
                        dplay(self)
                else:
                    if self.alpha > 150:
                        self.alpha -= 750/FPS
                        self.main.set_alpha(self.alpha)
                    elif self.alpha < 150 and (len(find_text) == 0 or self.sn != -1):
                        self.alpha += 750/FPS
                        self.main.set_alpha(self.alpha)
                Smusic.blit(self.main, (50, 15+self.n*38+level+self.d))
            else:
                if self.alpha > 150:
                    self.alpha -= 750/FPS
                    self.main.set_alpha(self.alpha)
                elif self.alpha < 150 and (len(find_text) == 0 or self.sn != -1):
                    self.alpha += 750/FPS
                    self.main.set_alpha(self.alpha)


    class Wallpaper:
        counter = ClassCounter()
        alpha = 0

        def __init__(self, w, p):
            if not p.endswith('/'):
                p += '/'
            self.wallpaper = pygame.image.load(p+w)
            if self.counter.current_number() == 0:
                self.alpha = 250
            else:
                self.alpha = 0
            self.pos = [0, 0]
            self.wallpaper.set_alpha(self.alpha)
            self.n = self.counter.plus()
            rect = self.wallpaper.get_rect()[2:4]
            if rect[0]/rect[1] > size[0]/size[1]:
                rect[0] = int((rect[0]*size[1])/rect[1])
                rect[1] = size[1]
                self.pos[0] = -abs(size[0]-rect[0])/2
            elif rect[0]/rect[1] < size[0]/size[1]:
                rect[1] = int((size[0]*rect[1])/rect[0])
                rect[0] = size[0]
                self.pos[1] = -abs(size[1]-rect[1])/2
            self.wallpaper = pygame.transform.smoothscale(self.wallpaper, rect)
            '''
            self.control_sum = [0, 0, 0]
            kek = rect[0]*rect[1]
            for h in range(rect[0]):
                for w in range(rect[1]):
                    x, y, z, alpha = self.wallpaper.get_at((h, w))
                    self.control_sum[0] += x/kek
                    self.control_sum[1] += y/kek
                    self.control_sum[2] += z/kek
            '''

        def render(self):
            Sbackground.blit(self.wallpaper, self.pos)


    class Control:
        counter = ClassCounter()

        def __init__(self, png, pos, cmd, depend=None, arg=None):
            self.main = pygame.transform.smoothscale(pygame.image.load(png), (30, 30))
            self.main2 = pygame.transform.smoothscale(pygame.image.load(png), (30, 30))
            self.pos = pos
            self.cmd = cmd
            self.under = 0
            self.depend = depend
            self.n = self.counter.plus()
            self.arg = arg
            self.color = current_color
            for h in range(30):
                for w in range(30):
                    x, y, z, alpha = self.main.get_at((h, w))
                    self.main.set_at((h, w), (255-x, 255-y, 255-z, alpha))
                    self.main2.set_at((h, w), ((255-x)*(current_color[0]/255), (255-y)*(current_color[1]/255),
                                               (255-z)*(current_color[2]/255), alpha))

        def render(self):
            global mouseButton
            '''
            if self.color != current_color:
                self.color = current_color
                for h in range(30):
                    for w in range(30):
                        x, y, z, alpha = self.main.get_at((h, w))
                        self.main2.set_at((h, w), (x*(current_color[0]/255), (y*(current_color[1]/255),
                                                   z*(current_color[2]/255), alpha)))
            '''
            if self.pos[0] <= mp[0] <= self.pos[0]+30 and self.pos[1] <= mp[1]-330 <= self.pos[1]+30:
                Scontrol.blit(self.main2, self.pos)
                if mouseButton:
                    mouseButton = 0
                    if self.arg is not None:
                        self.cmd(self.arg)
                    else:
                        self.cmd()
            else:
                if self.depend is not None and globals()[self.depend]:
                    Scontrol.blit(self.main2, self.pos)
                else:
                    Scontrol.blit(self.main, self.pos)


    def load_data():
        global data
        try:
            with open('data/settings') as file:
                file = file.read().split(';\n\n')
                for i in range(3):
                    data.append(file[i].split(';\n'))
        except FileNotFoundError:
            data = [['No', 'No', 'No'], ['C:/Users/'+getuser()+'/Music/'], ['C:/Users/'+getuser()+'/Pictures/']]


    def load_music():
        for path in data[1]:
            for root, dirs, files in walk(path):
                if path == root or data[0][0] == 'Yes':
                    for file in files:
                        if file.endswith('.mp3'):
                            musics.append(Music(file, root))


    def load_wallpaper():
        for path in data[2]:
            for root, dirs, files in walk(path):
                if path == root or data[0][1] == 'Yes':
                    for file in files:
                        if file.endswith('.jpg'):
                            wallpapers.append(Wallpaper(file, root))


    def dprevious():
        global pause, delta
        if status:
            check = musics[0].check_status()
            if pause:
                pause = 0
            if rand:
                try:
                    n = rand_list[-2].n
                except IndexError:
                    n = check-1
                rand_list.pop(-1)
            else:
                n = check-1
            if n < 0:
                n = Music.counter.current_number()-1
            delta = 0
            dplay(musics[n])


    def dplay(m):
        global status, pause, delta
        if not status:
            if isinstance(m, int):
                m = musics[m]
            if len(rand_list) > 0 and rand_list[-1] != m:
                rand_list.append(m)
            elif len(rand_list) == 0:
                rand_list.append(m)
            if data[0][2] == 'Yes':
                pygame.mixer.quit()
                pygame.mixer.init(frequency=m.frequency)
                pygame.mixer.music.set_volume(current_volume/100)
            pygame.display.set_caption(m.music)
            status = 1
            pygame.mixer.music.load(m.path+m.music)
            pygame.mixer.music.play()
            musics[0].del_status()
            m.status = 1
            delta = 0
        elif pause:
            pygame.mixer.music.unpause()
            pause = 0
        else:
            pygame.mixer.music.stop()
            status = 0
            dplay(m)


    def dpause():
        global pause
        if status:
            pygame.mixer.music.pause()
            pause = 1


    def dstop():
        global status, pause, delta
        pygame.mixer.music.stop()
        pygame.display.set_caption('MusicPlayer v0.3')
        musics[0].del_status()
        delta = 0
        if status:
            status = 0
        if pause:
            pause = 0


    def dnext():
        global pause, delta
        if status:
            check = musics[0].check_status()
            if check+1 < Music.counter.current_number() or rand:
                if pause:
                    pause = 0
                n = check+1
                if rand:
                    while n == check+1:
                        n = choice(range(Music.counter.current_number()))
                delta = 0
                dplay(musics[n])


    def dvolume():
        global volume, Svolume_alpha
        if volume:
            volume = 0
            Svolume_alpha = 0
        else:
            volume = 1
            Svolume_alpha = 175
        Svolume.set_alpha(Svolume_alpha)


    def dsetting():
        global setting
        if setting:
            setting = 0
        else:
            setting = 1


    def drepeat():
        global repeat
        if repeat:
            repeat = 0
        else:
            repeat = 1


    def drand():
        global rand
        if rand:
            rand = 0
        else:
            rand = 1


    def draw_volume():
        global current_volume
        pygame.draw.polygon(Svolume, white, ((10, 10), (10, 110), (19, 110), (19, 10)))
        pygame.draw.polygon(Svolume, current_color, ((10, 110-current_volume), (10, 110), (19, 110),
                                                     (19, 110-current_volume)))
        if 760 <= mp[0] <= 779 and 240 <= mp[1] <= 340:
            if mouseButton:
                current_volume = 340 - mp[1]
                pygame.mixer.music.set_volume(current_volume/100)
        if 760 <= mp[1] <= 779:
            if mouseButton:
                if 230 <= mp[1] <= 240:
                    current_volume = 100
                    pygame.mixer.music.set_volume(current_volume / 100)
                if 340 <= mp[1] <= 350:
                    current_volume = 0
                    pygame.mixer.music.set_volume(current_volume / 100)


    def draw_setting():
        global mouseButton, musics, wallpapers, status, cw
        if Ssetting_alpha > 0:
            texts = ['Искать во вложенных папках музыки:',
                     'Расположение музыки:',
                     'Расположение картинок:']

            param = [data[0][0], data[1][0], data[2][0]]

            pos1 = [[40, 25], [40, 80], [40, 170]]
            pos2 = [[550, 25], [80, 120], [80, 210]]
            for i in range(len(texts)):
                if pos1[i][1] <= mp[1] <= pos1[i][1]+30 or pos2[i][1] <= mp[1] <= pos2[i][1]+30:
                    Ssetting.blit(label.render(texts[i], 1, current_color), pos1[i])
                    Ssetting.blit(label.render(param[i], 1, current_color), pos2[i])
                    if mouseButton:
                        mouseButton = 0
                        if i == 0:
                            if data[0][0] == 'Yes':
                                data[0][0] = 'No'
                            else:
                                data[0][0] = 'Yes'
                            if status:
                                status = 0
                                pygame.mixer.music.stop()
                            musics = []
                            Music.counter.drop_number()
                            load_music()
                            Cplay.arg = musics[0]
                        if i == 1:
                            filename = easygui.diropenbox()
                            if filename is not None:
                                data[1][0] = filename
                        if i == 2:
                            filename = easygui.fileopenbox(multiple=True)
                            if filename is not None:
                                pass
                else:
                    Ssetting.blit(label.render(texts[i], 1, white), pos1[i])
                    Ssetting.blit(label.render(param[i], 1, white), pos2[i])


    def draw_status():
        global mouseButton, delta
        pygame.draw.line(Scontrol, white, (200, 34), (600, 34), 3)
        check = musics[0].check_status()
        if check != -1:
            length = int(musics[check].music_length)
            if musics[check].frequency != 1:
                length = int(length*musics[check].frequency)
            pos = int(pygame.mixer.music.get_pos()/1000 + delta)
            pygame.draw.line(Scontrol, current_color, (200, 34), (200+(pos*400)/length, 34), 3)
            pos_s = str(pos % 60)
            pos_m = str(pos // 60)
            length_s = str(length % 60)
            length_m = str(length // 60)
            if len(pos_m) == 1:
                pos_m = '0'+pos_m
            if len(pos_s) == 1:
                pos_s = '0'+pos_s
            if len(length_m) == 1:
                length_m = '0'+length_m
            if len(length_s) == 1:
                length_s = '0'+length_s
            Scontrol.blit(label.render(pos_m+':'+pos_s, 1, white), (200, 39))
            Scontrol.blit(label.render(length_m+':'+length_s, 1, white), (537, 39))
            if 200 <= mp[0] <= 600 and 32 <= mp[1]-330 <= 39:
                sdelta = int(((mp[0]-200)*length)/400)
                if mouseButton:
                    mouseButton = 0
                    delta = ((mp[0]-200)*length)/400
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_pos(delta/musics[check].frequency)
                sdelta_s = str(sdelta % 60)
                sdelta_m = str(sdelta // 60)
                if len(sdelta_m) == 1:
                    sdelta_m = '0'+sdelta_m
                if len(sdelta_s) == 1:
                    sdelta_s = '0'+sdelta_s
                text = label.render(sdelta_m+':'+sdelta_s, 1, white)
                hihi = pygame.Surface(text.get_rect()[2:4])
                hihi.fill(black)
                hihi.set_alpha(200)
                hihi.blit(text, (0, 0))
                Scontrol.blit(hihi, (mp[0]-text.get_rect()[2]/2, 2))


    def hidden():
        global Sbackground_alpha, Smusic_alpha
        if none_do >= time_to_hidden*FPS:
            if Sbackground_alpha < 250:
                Sbackground_alpha += 750/FPS
                Sbackground.set_alpha(Sbackground_alpha)
            if Smusic_alpha > 0:
                Smusic_alpha -= 750/FPS
                Smusic.set_alpha(Smusic_alpha)
        else:
            if Sbackground_alpha > 150:
                Sbackground_alpha -= 750/FPS
                Sbackground.set_alpha(Sbackground_alpha)
            if Smusic_alpha < 200 and not setting:
                Smusic_alpha += 750/FPS
                Smusic.set_alpha(Smusic_alpha)


    def find(e):
        global find_text, find_pos, shadow_musics, smc, none_do, max_level, level
        none_do = 0
        shadow_musics = []
        smc = 0
        if e.unicode not in ('\r', '\t', '\x08', '\x1b', '') and\
                e.key not in (273, 274, 275, 276) and label.render(find_text, 1, white).get_rect()[2] < 700:
            find_text = find_text[0:find_pos]+e.unicode+find_text[find_pos:]
            find_pos += 1
        elif e.unicode == '\x08':
            if len(find_text) > 0 and find_pos > 0:
                find_text = find_text[0:find_pos-1]+find_text[find_pos:]
                find_pos -= 1
        elif e.key == pygame.K_LEFT:
            if find_pos > 0:
                find_pos -= 1
        elif e.key == pygame.K_RIGHT:
            if find_pos < len(find_text):
                find_pos += 1
        for m in musics:
            used = []
            for word1 in m.music.split(' '):
                for word2 in find_text.split(' '):
                    if word2.lower() in word1.lower() and word2 not in used and word2 != '' and word1 != '':
                        used.append(word2)
                    if word2 == '' and '' not in used:
                        used.append('')
            if len(used) >= len(find_text.split(' ')) and len(find_text) > 0:
                shadow_musics.append(m.set_sn(smc))
                smc += 1
                # print(len(used), len(find_text.split(' ')), used, m.music, 'in')
            else:
                m.set_sn(-1)
                # print(len(used), len(find_text.split(' ')), used, m.music, 'out')

        if find_text == '':
            smc = Music.counter.current_number()
        if smc <= 8:
            max_level = 0
        else:
            max_level = (smc - 8) * 38
        if level < -max_level:
            level = -max_level
        # print(find_text.split(' '), '\n')


    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    white = (255, 255, 255)
    current_color = (60, 170, 255)
    black = (0, 0, 0)
    size = (800, 400)

    window = pygame.display.set_mode(size)
    pygame.display.set_caption('MusicPlayer v0.3')
    screen = pygame.Surface(size)
    clock = pygame.time.Clock()

    Smusic = pygame.Surface((800, 330))
    Scontrol = pygame.Surface((800, 70))
    Sbackground = pygame.Surface(size)
    Ssetting = pygame.Surface((800, 330))
    Svolume = pygame.Surface((30, 120))
    Sfind = pygame.Surface((800, 50))

    Smusic_alpha = 200
    Scontrol_alpha = 175
    Sbackground_alpha = 150
    Ssetting_alpha = 0
    Svolume_alpha = 0
    Sfind_alpha = 200

    Smusic.set_alpha(Smusic_alpha)
    Scontrol.set_alpha(Scontrol_alpha)
    Sbackground.set_alpha(Sbackground_alpha)
    Ssetting.set_alpha(Ssetting_alpha)
    Svolume.set_alpha(Svolume_alpha)
    Sfind.set_alpha(Sfind_alpha)

    label = pygame.font.SysFont('Calibri', 30)

    mp = (0, 0)  # mouse position
    delta = 0  # music.get_pos()+delta
    current_volume = 100
    cw = 0  # current wallpaper
    volume = 0
    setting = 0
    repeat = 0
    rand = 0
    rand_list = []
    run = 1
    FPS = 30
    level = 0
    mouseButton = 0
    status = 0
    pause = 0
    data = []
    musics = []
    shadow_musics = []  # find
    wallpapers = []
    time = 0
    time_to_change_wallpaper = 60
    none_do = 0
    time_to_hidden = 15
    find_text = ''
    find_pos = 0
    smc = 0  # shadow music count (find)
    del_find = 0
    del_find_ping = 0
    frequency = 44100

    load_data()
    load_music()
    load_wallpaper()

    # current_color = wallpapers[0].control_sum

    Cprev = Control('data/prev.jpg', (10, 20), dprevious)
    Cplay = Control('data/play.jpg', (55, 20), dplay, arg=musics[0])
    Cpause = Control('data/pause.jpg', (55, 20), dpause)
    Cstop = Control('data/stop.jpg', (100, 20), dstop)
    Cnext = Control('data/next.jpg', (145, 20), dnext)
    Crepeat = Control('data/repeat.jpg', (625, 20), drepeat, 'repeat')
    Crand = Control('data/rand.jpg', (670, 20), drand, 'rand')
    Csetting = Control('data/gear.jpg', (715, 20), dsetting, 'setting')
    Cvolume = Control('data/sound.jpg', (760, 20), dvolume, 'volume')

    controls = [Cprev, Cplay, Cpause, Cstop, Cnext, Cvolume, Csetting, Crepeat, Crand]

    if Music.counter.current_number() <= 8:
        max_level = 0
    else:
        max_level = (Music.counter.current_number()-8)*38

    while run:
        mp_old = mp
        mp = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (750 < mp[0] or mp[0] < 50) and mp[1] < 330 and not volume:
                        none_do = time_to_hidden*FPS
                    else:
                        mouseButton = 1
                if event.button == 4 and level < 0:
                    level += 18
                    none_do = 0
                if len(find_text) > 0:
                    max_level += 50
                if event.button == 5 and level > -max_level:
                    level -= 18
                    none_do = 0
                if len(find_text) > 0:
                    max_level -= 50
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouseButton = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    del_find = event
                find(event)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    del_find = 0

        if del_find != 0 and del_find_ping >= FPS*(1/3):
            find(del_find)
            del_find_ping = FPS*(9/30)
        elif del_find != 0:
            del_find_ping += 1
        else:
            del_find_ping = 0

        if status and not pygame.mixer.music.get_busy():
            c = musics[0].check_status()
            if repeat:
                dplay(musics[c])
            else:
                dnext()

        if time < time_to_change_wallpaper*FPS:
            time += 1
        else:
            if wallpapers[cw].alpha > 0:
                wallpapers[cw].alpha -= 750/FPS
                wallpapers[cw].wallpaper.set_alpha(wallpapers[cw].alpha)
                if cw+1 < Wallpaper.counter.current_number():
                    wallpapers[cw+1].alpha += 750/FPS
                    wallpapers[cw+1].wallpaper.set_alpha(wallpapers[cw+1].alpha)
                else:
                    wallpapers[0].alpha += 750/FPS
                    wallpapers[0].wallpaper.set_alpha(wallpapers[0].alpha)
            else:
                cw += 1
                if cw == Wallpaper.counter.current_number():
                    cw = 0
                # current_color = wallpapers[cw].control_sum
                time = 0

        if setting:
            if Smusic_alpha > 0:
                Smusic_alpha -= 750/FPS
                Smusic.set_alpha(Smusic_alpha)
            if Ssetting_alpha < 150:
                Ssetting_alpha += 750/FPS
                Ssetting.set_alpha(Ssetting_alpha)
        else:
            if Smusic_alpha < 200 and none_do < time_to_hidden*FPS:
                Smusic_alpha += 750/FPS
                Smusic.set_alpha(Smusic_alpha)
            if Ssetting_alpha > 0:
                Ssetting_alpha -= 750/FPS
                Ssetting.set_alpha(Ssetting_alpha)

        if mp == mp_old:
            if none_do < time_to_hidden*FPS:
                none_do += 1
        elif 50 < mp[0] < 750 and mp[1] < 330 and not setting:
            none_do = 0
        hidden()

        screen.fill(black)
        Smusic.fill(black)
        Scontrol.fill(black)
        Ssetting.fill(black)
        Svolume.fill(black)
        Sfind.fill(black)

        if len(find_text) > 0:
            if Sfind_alpha < 200:
                Sfind_alpha += 50
                Sfind.set_alpha(Sfind_alpha)
            Sfind_text = label.render(find_text, 1, white)
            Sfind.blit(Sfind_text, (400-Sfind_text.get_rect()[2]/2, 10))
            asd = label.render(find_text[0:find_pos], 0, black).get_rect()[2]+(400-Sfind_text.get_rect()[2]/2)
            pygame.draw.line(Sfind, white, (asd, 10), (asd, 40))
        else:
            if Sfind_alpha > 0:
                Sfind_alpha -= 50
                Sfind.set_alpha(Sfind_alpha)

        draw_volume()
        draw_setting()
        draw_status()

        for wallpaper in wallpapers:
            wallpaper.render()

        if Smusic_alpha > 0:
            for music in musics:
                music.render()

        for control in controls:
            if control.n == 1:
                if not status or pause:
                    control.render()
            elif control.n == 2:
                if status and not pause:
                    control.render()
            else:
                control.render()

        screen.blit(Sbackground, (0, 0))
        Smusic.blit(Sfind, (0, 0))
        screen.blit(Smusic, (0, 0))
        screen.blit(Ssetting, (0, 0))
        screen.blit(Scontrol, (0, 330))
        screen.blit(Svolume, (760, 230))
        window.blit(screen, (0, 0))

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    with open('data/settings', 'w') as fi:
        fi.write(data[0][0]+';\n'+data[0][1]+';\n'+data[0][2]+';\n\n'+data[1][0]+';\n\n'+data[2][0])
