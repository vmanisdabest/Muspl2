def ROTATE(IMG, POS, ROT, SZ, SCND = False, POST = [0, 0]):
    try:
        global EDIMG
        exec("EDIMG = " + IMG + ".copy()", globals())
        ORECT = EDIMG.get_rect()
        RRECT = ORECT.copy()
        if ROT == 90 or ROT == 270:
            ROT += 1
        EDIMG = pygame.transform.rotate(EDIMG, round(ROT))
        RRECT.center = EDIMG.get_rect().center
        EDIMG = EDIMG.subsurface(RRECT).copy()
        screen.blit(EDIMG, POS)
        if SCND:
            screen.blit(EDIMG, POST)
    except:
        #print(ROT)
        pass
def GetChimes(NUM):
    TEN = int(NUM/10)
    NUM = NUM-(TEN*10)
    FIV = int(NUM/5)
    NUM = NUM-(FIV*5)
    THR = int(NUM/3)
    NUM = NUM - (THR*3)
    return TEN, FIV, THR, NUM
def CHK_PLAYER():
    try:
        #T4MT global screen
        global NEXT
        global CMD
        global EXIT
        global SLC
        global VOL
        global PREV
        global POINT
        global PLIST
        global RAND
        global PUSH
        global ACVR
        global CURR
        global PP
        global LENG
        global MPOS
        global SUPSHF
        global ARTS
        global CURL
        if SLC == 0:
            pygame.display.set_caption("MUSPL2: All Songs")
        if CMD == "PAUSE":
            mixer.music.pause()
            CMD = ""
        elif CMD == "SHUFFLE" and PLIST:
            if RAND:
                RAND = False
            else:
                if SUPSHF:
                    TMZ = 100
                else:
                    TMZ = 1
                while TMZ > 0:
                    #print(TMZ)
                    RAND = True
                    OPOINT = POINT
                    EDI = NEXT
                    NEXT = []
                    while len(EDI) != 0:
                        if random.randint(1, 2) == 1:
                            POINT = round(numpy.random.uniform(0, len(EDI)-1, size=1)[0])
                        else:
                            POINT = random.randint(0, len(EDI)-1)
                        NEXT.append(EDI[POINT])
                        del EDI[POINT]
                    PUSH = True
                    random.shuffle(NEXT)
                    TMZ -= 1
                    if random.randint(1, 3) == 1:
                        pygame.event.get()
            CMD = ""
        elif CMD == "PLAY":
            mixer.music.unpause()
            CMD = ""
        elif CMD == "VOLS":
            SET_VOL(VOL/100)
            CMD = ""
        elif CMD == "VOL-":
            VOL -= 1
            if VOL < 0:
                VOL = 0
            #SET_VOL(VOL/100)
            CMD = ""
        elif CMD == "VOL+":
            VOL += 1
            if VOL > 100:
                VOL = 100
            #SET_VOL(VOL/100)
            CMD = ""
        elif CMD == "STOP":
            mixer.music.stop()
            NEXT = []
            ACVR = None
            POINT = 0
            PUSH = False
            CMD = ""
            CURR = "Not Playing"
        elif CMD == "SKIP":
            if PLIST:
                POINT += 1
                PUSH = True
            else:
                if len(NEXT) > 0:
                    PREV = NEXT[0]
                    del NEXT[0]
                    PUSH = True
                else:
                    mixer.music.pause()
            CMD = ""
        elif CMD == "PREVIUS":
            if PLIST:
                POINT -= 1
                PUSH = True
            else:
                if PREV != "":
                    EDI = PREV
                    PREV = NEXT[0]
                    NEXT[0] = PREV
                    PUSH = True
                else:
                    mixer.music.pause()
            CMD = ""
        if PP and not pygame.mixer.music.get_busy() and len(NEXT) < 2:
            PP = False
        elif not PP and pygame.mixer.music.get_busy():
            PP = True
        if not pygame.mixer.music.get_busy() and PP or PUSH:
            if len(NEXT) != 0 and PUSH == False:
                if PLIST:
                    POINT += 1
                else:
                    if PREV != "":
                        PREV = NEXT[0]
                        del NEXT[0]
                    else:
                        PREV = NEXT[0]
            if len(NEXT) != 0:
                if PLIST:
                    if POINT < 0:
                        POINT = len(NEXT)-1
                    elif POINT > len(NEXT)-1:
                        if not RAND:
                            if SUPSHF:
                                TMZ = 100
                            else:
                                TMZ = 1
                            while TMZ > 0:
                                #print(TMZ)
                                RAND = True
                                OPOINT = POINT
                                EDI = NEXT
                                NEXT = []
                                while len(EDI) != 0:
                                    if random.randint(1, 2) == 1:
                                        POINT = round(numpy.random.uniform(0, len(EDI)-1, size=1)[0])
                                    else:
                                        POINT = random.randint(0, len(EDI)-1)
                                    NEXT.append(EDI[POINT])
                                    del EDI[POINT]
                                PUSH = True
                                random.shuffle(NEXT)
                                TMZ -= 1
                                if random.randint(1, 3) == 1:
                                    pygame.event.get()
                        POINT = 0
                    CRMS = pygame.mixer.Sound(NEXT[POINT])
                    mixer.music.load(NEXT[POINT])
                    LENG = pygame.mixer.Sound.get_length(CRMS)
                    CURR = NEXT[POINT]
                    CURL = pygame.mixer.Sound(CURR).get_length()
                    time.sleep(0.2)
                else:
                    if PUSH and pygame.mixer.music.get_busy():
                        mixer.music.stop()
                        pygame.mixer.music.unload()
                        mixer.music.load(NEXT[0])
                    else:
                        mixer.music.load(NEXT[0])
                    CRMS = pygame.mixer.Sound(NEXT[0])
                    LENG = pygame.mixer.Sound.get_length(CRMS)
                    #print(LENG)
                    CURR = NEXT[0]
                    CURL = pygame.mixer.Sound(CURR).get_length()
                    time.sleep(0.2)
                mixer.music.play()
            if not PLIST:
                try:
                    NAM = CURR
                    NAM = NAM.split(" - ")
                    NAM = NAM[0] + ".png"
                    ACVR = pygame.image.load(NAM).convert_alpha()
                    ACVR = pygame.transform.scale(ACVR, (400, 400))
                except Exception as E:
                    #print(E)
                    ACVR = None
            else:
                try:
                    NAM = NEXT[POINT]
                    NAM = NAM.split(" - ")
                    NAM = NAM[0] + ".png"
                    ARTS = pygame.image.load(NAM).convert_alpha()
                    ARTS = pygame.transform.scale(ARTS, (400, 400))
                except Exception as E:
                    #print(E)
                    ARTS = None
            PUSH = False
        pygame.event.get()
    except Exception as E:
        #print(E)
        CMD = ""
        PUSH = False
def cv2ImageToSurface(cv2Image):
    if cv2Image.dtype.name == 'uint16':
        cv2Image = (cv2Image / 256).astype('uint8')
    size = cv2Image.shape[1::-1]
    if len(cv2Image.shape) == 2:
        cv2Image = np.repeat(cv2Image.reshape(size[1], size[0], 1), 3, axis = 2)
        format = 'RGB'
    else:
        format = 'RGBA' if cv2Image.shape[2] == 4 else 'RGB'
        cv2Image[:, :, [0, 2]] = cv2Image[:, :, [2, 0]]
    surface = pygame.image.frombuffer(cv2Image.flatten(), size, format)
    return surface.convert_alpha() if format == 'RGBA' else surface.convert()
def VIDPLAYER(VIDLIST):
    if type(VIDLIST) == str():
        VIDP = VIDLIST
        PLYL = False
    else:
        VIDP = VIDLIST[0]
        PLYL = True
    POINT = 0
    redo = True
    while redo:
        screen.fill((40,40,40))
        Y = 50
        display_screen.fill((40,40,40))
        vidcap = cv2.VideoCapture(VIDP)
        FPS = vidcap.get(cv2.CAP_PROP_FPS)
        success, image = vidcap.read()
        count = 0
        image = image
        w, h = pygame.display.get_surface().get_size()
        clock = pygame.time.Clock()
        screen.fill((40,40,40))
        AVNC = 1
        KEYPR = ""
        while success:
            clock.tick(FPS)
            if AVNC == 1:
                Img = cv2ImageToSurface(image)
                if w > h:
                    RATE = display_screen.get_height()/h
                    Img = pygame.transform.scale(Img, (w*RATE, h*RATE))
                elif w < h:
                    RATE = display_screen.get_height()/w
                    Img = pygame.transform.scale(Img, (w*RATE, h*RATE))
                else:
                    if display_screen.get_width() > display_screen.get_height():
                        RATE = display_screen.get_height()/h
                    else:
                        RATE = display_screen.get_height()/w
                    Img = pygame.transform.scale(Img, (w*RATE, h*RATE))
            display_screen.blit(Img, ((display_screen.get_width()/2)-(Img.get_width()/2),(display_screen.get_height()/2)-(Img.get_height()/2)))
            if AVNC == 1:
                success,image = vidcap.read()
            keys = pygame.key.get_pressed()
            for I in range(len(keys)):
                if keys[I]:
                    success = False
                    redo = False
            pygame.event.get()
            pygame.display.update()
            if AVNC == 1:
                count += 1
            CHK_PLAYER()
        if PLYL:
           POINT += 1
           if POINT > len(VIDLIST)-1:
               POINT = 0
           VIDP = VIDLIST[POINT]
def TEST(NUM = None):
    if NUM == None:
        NUM = random.randint(1, 45)
    CHTM = GetChimes(NUM)
    print(NUM, CHTM)
    for I in range(CHTM[0]):
       pygame.mixer.Channel(0).play(pygame.mixer.Sound('Muspl2 - Bell Chime 10.mp3'))
       time.sleep(2.4)
       pygame.event.get()
    for I in range(CHTM[1]):
       pygame.mixer.Channel(0).play(pygame.mixer.Sound('Muspl2 - Bell Chime 5.mp3'))
       time.sleep(2.4)
       pygame.event.get()
    for I in range(CHTM[2]):
       pygame.mixer.Channel(0).play(pygame.mixer.Sound('Muspl2 - Bell Chime 3.mp3'))
       time.sleep(2.4)
       pygame.event.get()
    for I in range(CHTM[3]):
       pygame.mixer.Channel(0).play(pygame.mixer.Sound('Muspl2 - Bell Chime 1.mp3'))
       time.sleep(2.4)
       pygame.event.get()
def SET_VOL(VOL):
    if VOL > 1:
        VOL = 1
    elif VOL < 0:
        VOL = 0
    VOL = round((VOL*100)/2)
    for I in range(50):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
    for I in range(VOL):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
def DisToScr(XY):
    global C_SCL
    EXY = list(XY)
    EXY[0] = EXY[0] - round((display_screen.get_width()/2) - ((C_SCL*900)/2))
    EXY[1] =  EXY[1] - round((display_screen.get_height()/2) - ((C_SCL*700)/2))
    EXY[0] = round(EXY[0]/C_SCL)
    EXY[1] = round(EXY[1]/C_SCL)
    return EXY
def MUS_DISPLAY():
    #T4MT global screen
    global EXIT
    global keys
    global NEXT
    global CMD
    global SLC
    global PUSH
    global CURR
    global RL
    global PLIST
    global VOL
    global PLIST
    global DWID
    global ACVR
    global POINT
    global PP
    global SHNEXT
    global LENG
    global MPOS
    global EURO
    global BEEP
    global SLEP
    global ARTS
    global CHIME
    global NXT
    global CURL
    global C_SCL
    global SEARCH
    global LOOKFOR
    FILS = []
    HIG = 0
    VEL = 0
    SELEC = False
    POS = 1
    OUT = ".mp3"
    ACVR = None
    SCROLL = 0
    PP = True
    DIS = False
    RFF = 0
    TRK = 0
    DPOS = 0
    REC = False
    SLP = True
    MFRM = 100
    SFRM = 0
    BAND = "Unkown"
    PPOS = 0
    MODE = 0
    BRES = True
    FRM = 0
    NOPLST = False
    TXTDIS = ""
    while EXIT == False:
       if SLC != 0:
           SEARCH = False
           LOOKFOR = ""
           TXTDIS = ""
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
                EXIT = True
                mixer.music.stop()
                pygame.quit()
                sys.exit()
       #print(pygame.display.get_active() and pygame.mouse.get_focused())
       if pygame.display.get_active() and pygame.mouse.get_focused():
           #if SFRM >= 20:
           #    for I in range(len(keys)):
           #        if keys[I]:
           #            SFRM = 0
           #if SLP:
               #if SFRM > MFRM:
               #    SFRM = 0
               #    VIDPLAYER("Media Player 2023-04-20 11-38-12.mp4")
               #else:
               #    SFRM += 1
           screen.fill([0, 47, 71])
           screen.blit(BACK, [0,0])
           if SLC == 4:
               pygame.display.set_caption("MUSPL2: Power")
               pygame.draw.rect(screen, [255, 140, 0], pygame.Rect(800, 45, 70, 5))
               screen.blit(PBOX, [250, 200])
               if PPOS == 0:
                   TXT = MFONT.render("> Standby <", False, [252, 191, 73])
               else:
                   TXT = MFONT.render("Standby", False, [252, 191, 73])
               screen.blit(TXT, [450-(TXT.get_width()/2), 230])
               screen.blit(PBOX, [250, 342])
               if PPOS == 1:
                   TXT = MFONT.render("> Sleep <", False, [252, 191, 73])
               else:
                   TXT = MFONT.render("Sleep", False, [252, 191, 73])
               screen.blit(TXT, [450-(TXT.get_width()/2), 372])
               screen.blit(PBOX, [250, 484])
               if PPOS == 2:
                   TXT = MFONT.render("> Alarm <", False, [252, 191, 73])
               else:
                   TXT = MFONT.render("Alarm", False, [252, 191, 73])
               screen.blit(TXT, [450-(TXT.get_width()/2), 514])
               keys = pygame.key.get_pressed()
               if keys[pygame.K_UP]:
                   PPOS -= 1
                   if PPOS < 0:
                       PPOS = 2
                   time.sleep(0.15)
               elif keys[pygame.K_DOWN]:
                   PPOS += 1
                   if PPOS > 2:
                       PPOS = 0
                   time.sleep(0.15)
               elif keys[pygame.K_RETURN]:
                   time.sleep(0.25)
                   keys = pygame.key.get_pressed()
                   X = 300
                   Y = 200
                   DIR = random.randint(1, 4)
                   if PPOS == 2:
                       DIR = random.randint(1, 11)
                       FRM = 0
                       TIMES = ["00:00", "00:15", "00:30", "00:45"]
                       APN = ["00", "15", "30", "45"]
                       H = 1
                       M = 0
                       while TIMES[len(TIMES)-1] != "23:45":
                           TIMES.append(str(H) + ":" + APN[M])
                           if M < 3:
                               M += 1
                           else:
                               M = 0
                               H += 1
                       ALRM = ["8:30", 20, 80]
                       TALRM = ALRM.copy()
                       TALRM[0] = 0
                       ALSET = False
                       time.sleep(0.3)
                       keys = pygame.key.get_pressed()
                       QUIET = False
                       HOURD = False
                       while not keys[pygame.K_ESCAPE]:
                           if ALSET:
                              time.sleep(0.011)
                           else:
                               #time.sleep(0.011)
                               time.sleep(0.7)
                           if DIR == 1:
                               screen.blit(CLK, [0,0])
                           elif DIR == 2:
                               screen.blit(CLK1, [0,0])
                           elif DIR == 3:
                               screen.blit(CLK2, [0,0])
                           elif DIR == 4:
                               screen.blit(CLK3, [0,0])
                           elif DIR == 5:
                               screen.blit(CLK4, [0,0])
                           elif DIR == 6:
                               screen.blit(CLK5, [0,0])
                           elif DIR == 7:
                               screen.blit(CLK6, [0,0])
                           elif DIR == 8:
                               screen.blit(CLK7, [0,0])
                           elif DIR == 9:
                               screen.blit(CLK8, [0,0])
                           elif DIR == 10:
                               screen.blit(CLK8, [0,0])
                           else:
                               screen.blit(CLK9, [0,0])
                           if FRM >= 90 and not ALSET:
                               DIR = random.randint(1, 11)
                               FRM = 0
                           else:
                               FRM += 1
                           NOW = datetime.now()
                           DTIME = str(NOW.strftime("%H:%M"))
                           DTIME = DTIME.replace("01:", "1:")
                           DTIME = DTIME.replace("02:", "2:")
                           DTIME = DTIME.replace("03:", "3:")
                           DTIME = DTIME.replace("04:", "4:")
                           DTIME = DTIME.replace("05:", "5:")
                           DTIME = DTIME.replace("06:", "6:")
                           DTIME = DTIME.replace("07:", "7:")
                           DTIME = DTIME.replace("08:", "8:")
                           DTIME = DTIME.replace("09:", "9:")
                           ATIME = DTIME
                           try:
                               if int(DTIME.split(":")[0]) >= 22 and SLEP and not QUIET:
                                   QUIET = True
                                   SET_VOL(0)
                                   mixer.music.pause()
                                   #print("Quiet")
                           except:
                               pass
                               #print("ERR")
                           if not EURO:
                               DTIME = DTIME.replace("00:", "12:")
                               DTIME = DTIME.split(":")
                               PM = False
                               if int(DTIME[0]) > 12:
                                   PM = True
                                   DTIME[0] = str(int(DTIME[0])-12)
                               if int(DTIME[0]) == 12:
                                   PM = True
                               DTIME = ":".join(DTIME)
                           TXT = CFONT.render(DTIME, False, [237, 116, 36])
                           screen.blit(TXT, [450-(TXT.get_width()/2), 253])   
                           if not EURO:
                               if PM:
                                   TTXT = AFONT.render("PM", False, [237, 116, 36])
                               else:
                                   TTXT = AFONT.render("AM", False, [237, 116, 36])
                               screen.blit(TTXT, [450+(TXT.get_width()/2), 253+TXT.get_height()-TTXT.get_height()])
                           if ALSET:
                               DTEST = TIMES[TALRM[0]]
                               if not EURO:
                                   DTEST = DTEST.replace("00:", "12:")
                                   DTEST = DTEST.split(":")
                                   PM = False
                                   if int(DTEST[0]) > 12:
                                       DTEST[0] = str(int(DTEST[0])-12)
                                       PM = True
                                   if int(DTIME[0]) == 12:
                                       PM = True
                                   DTEST = ":".join(DTEST)
                                   if PM:
                                       DTEST += "PM"
                                   else:
                                       DTEST += "AM"
                               TXT = AFONT.render("*Alarm " + str(DTEST) + " " + str(TALRM[1]) + " L " + str(TALRM[2]) + " A*", False, [237, 116, 36])
                           else:
                               DTEST = ALRM[0]
                               if not EURO:
                                   DTEST = DTEST.replace("00:", "12:")
                                   DTEST = DTEST.split(":")
                                   PM = False
                                   if int(DTEST[0]) > 12:
                                       DTEST[0] = str(int(DTEST[0])-12)
                                       PM = True
                                   if int(DTIME[0]) == 12:
                                       PM = True 
                                   DTEST = ":".join(DTEST)
                                   if PM:
                                       DTEST += "PM"
                                   else:
                                       DTEST += "AM"
                               TXT = AFONT.render("-Alarm " + str(DTEST) + " " + str(ALRM[1]) + " L " + str(ALRM[2]) + " A-", False, [237, 116, 36])
                           screen.blit(TXT, [450-(TXT.get_width()/2), 395])
                           try:
                               if NXT and len(NEXT) != 0:
                                   if len(NEXT)-POINT > 3:
                                       NUP = 3
                                   else:
                                       NUP = len(NEXT)-POINT
                                   PNUP = POINT + 1
                                   for NXUP in range(NUP):
                                       try:
                                           NAM = NEXT[PNUP+NXUP].replace(".mp3", "")
                                           TXT = FONT.render(NAM, False, [237, 116, 36])
                                           screen.blit(TXT, [450-(TXT.get_width()/2), 427+(NXUP*12)])
                                       except:
                                           pass
                           except:
                               pass
                           keys = pygame.key.get_pressed()
                           if keys[pygame.K_RETURN]:
                               time.sleep(0.3)
                               if ALSET:
                                   TALRM[0] = TIMES[TALRM[0]]
                                   ALRM = TALRM
                                   ALSET = False
                                   SET_VOL(TALRM[1]/100)
                               else:
                                   ALSET = True
                                   SLC = 0
                                   TALRM = ALRM
                                   TALRM[0] = 0
                                   SAFE = TALRM
                           if ALSET:
                               if keys[pygame.K_UP]:
                                   time.sleep(0.2)
                                   TALRM[SLC] += 1
                               elif keys[pygame.K_DOWN]:
                                   time.sleep(0.2)
                                   TALRM[SLC] -= 1
                               if keys[pygame.K_LEFT]:
                                   time.sleep(0.3)
                                   SLC -= 1
                               elif keys[pygame.K_RIGHT]:
                                   time.sleep(0.3)
                                   SLC += 1
                               if SLC > 2:
                                   SLC = 0
                               elif SLC < 0:
                                   SLC = 2
                               if TALRM[0] > len(TIMES)-1:
                                   TALRM[0] = 0
                               elif TALRM[0] < 0:
                                   TALRM[0] = len(TIMES)-1
                               if TALRM[1] > 100:
                                  TALRM[1] = 100
                               elif TALRM[1] < 0:
                                  TALRM[1] = 0
                               if TALRM[2] > 100:
                                  TALRM[2] = 100
                               elif TALRM[2] < 0:
                                  TALRM[2] = 0
                               if TALRM[1] + TALRM[2] > 100:
                                   TALRM = SAFE.copy()
                               else:
                                   SAFE = TALRM.copy()
                           if ATIME == ALRM[0] and BRES:
                               if BEEP:
                                   BRES = False
                                   mixer.music.pause()
                                   SET_VOL(ALRM[1]+ALRM[2])
                                   for I in range(15):
                                       pygame.mixer.Channel(0).play(pygame.mixer.Sound('MUSPL_ALRM.mp3'))
                                       time.sleep(0.5)
                                   SET_VOL(ALRM[1])
                                   mixer.music.unpause()
                                   time.sleep(1)
                               else:
                                   for I in range(ALRM[2]):
                                       CHK_PLAYER()
                                       SET_VOL(ALRM[1]+I+1/100)
                                       time.sleep(0.2)
                                   for I in range(60):
                                       CHK_PLAYER()
                                       time.sleep(0.2)
                                   for I in range(ALRM[2]):
                                       CHK_PLAYER()
                                       try:
                                           SET_VOL(ALRM[1]-(I+1)/100)
                                       except:
                                           pass
                                       time.sleep(0.2)
                               if QUIET:
                                   QUIET = False
                                   mixer.music.unpause()
                                   SET_VOL(ALRM[1]/100)
                           elif DTIME != ALRM[0] and not BRES:
                               SET_VOL(ALRM[1]/100)
                               BRES = True
                           CHK_PLAYER()
                           if display_screen.get_width() != 900 or display_screen.get_height() != 700:
                               display_screen.fill([0, 0, 0])
                               DWID = round(display_screen.get_width()/900-0.5)
                               DHIG = round(display_screen.get_height()/700-0.5)
                               if DWID == 0 or DHIG == 0:
                                   DWID = 1
                                   DHIG = 1
                               if DWID == DHIG or DWID > DHIG:
                                   edi_screen = pygame.transform.scale(screen.copy(), [DHIG*900, DHIG*700])
                               else:
                                   edi_screen = pygame.transform.scale(screen.copy(), [DWID*900, DWID*700])
                               display_screen.blit(edi_screen, [(display_screen.get_width()/2)-(edi_screen.get_width()/2), (display_screen.get_height()/2)-(edi_screen.get_height()/2)])
                           else:
                               display_screen.blit(screen, [0, 0])
                           pygame.event.get()
                           pygame.display.update()
                           if DTIME.split(":")[1] != "00":
                               HOURD = False
                           if CHIME and DTIME.split(":")[1] == "00" and not QUIET and not HOURD:
                               HOURD = True
                               mixer.music.pause()
                               pygame.mixer.Channel(0).play(pygame.mixer.Sound('Muspl2 - Bell Song.mp3'))
                               pygame.event.get()
                               time.sleep(16.77)
                               CHTM = GetChimes(int(DTIME.split(":")[0]))
                               for I in range(CHTM[0]):
                                   pygame.mixer.Channel(0).play(pygame.mixer.Sound('Muspl2 - Bell Chime 10.mp3'))
                                   time.sleep(2.45)
                                   pygame.event.get()
                               for I in range(CHTM[1]):
                                   pygame.mixer.Channel(0).play(pygame.mixer.Sound('Muspl2 - Bell Chime 5.mp3'))
                                   time.sleep(2.45)
                                   pygame.event.get()
                               for I in range(CHTM[2]):
                                   pygame.mixer.Channel(0).play(pygame.mixer.Sound('Muspl2 - Bell Chime 3.mp3'))
                                   time.sleep(2.45)
                                   pygame.event.get()
                               for I in range(CHTM[3]):
                                   pygame.mixer.Channel(0).play(pygame.mixer.Sound('Muspl2 - Bell Chime 1.mp3'))
                                   time.sleep(2.45)
                                   pygame.event.get()
                               mixer.music.unpause()
                   elif PPOS == 0:
                       COL = [0,0,0]
                       while not keys[pygame.K_ESCAPE]:
                           screen.fill(COL)
                           screen.blit(MUS, [X, Y])
                           if DIR == 1:
                               X -= 3
                               Y -= 3
                           elif DIR == 2:
                               X -= 3
                               Y += 3
                           elif DIR == 3:
                               X += 3
                               Y -= 3
                           else:
                               X += 3
                               Y += 3
                           if X + 300 >= 900:
                               DIR = random.randint(1, 2)
                               COL = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
                           if X <= 0:
                               DIR = random.randint(3, 4)
                               COL = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
                           if Y + 300 >= 700:
                               PIK = [1, 3]
                               DIR = PIK[random.randint(0, 1)]
                               COL = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
                           if Y <= 0:
                               PIK = [2, 4]
                               DIR = PIK[random.randint(0, 1)]
                               COL = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
                           keys = pygame.key.get_pressed()
                           if display_screen.get_width() != 900 or display_screen.get_height() != 700:
                               display_screen.fill([0, 0, 0])
                               DWID = round(display_screen.get_width()/900-0.5)
                               DHIG = round(display_screen.get_height()/700-0.5)
                               if DWID == 0 or DHIG == 0:
                                   DWID = 1
                                   DHIG = 1
                               if DWID == DHIG or DWID > DHIG:
                                   C_SCL = DHIG
                                   edi_screen = pygame.transform.scale(screen.copy(), [DHIG*900, DHIG*700])
                               else:
                                   C_SCL = DWID
                                   edi_screen = pygame.transform.scale(screen.copy(), [DWID*900, DWID*700])
                               display_screen.blit(edi_screen, [(display_screen.get_width()/2)-(edi_screen.get_width()/2), (display_screen.get_height()/2)-(edi_screen.get_height()/2)])
                           else:
                               display_screen.blit(screen, [0, 0])
                           pygame.event.get()
                           pygame.display.update()
                           CHK_PLAYER()
                           time.sleep(0.8)
                   else:
                        screen.fill([0,0,0])
                        if display_screen.get_width() != 900 or display_screen.get_height() != 700:
                           display_screen.fill([0, 0, 0])
                           DWID = round(display_screen.get_width()/900-0.5)
                           DHIG = round(display_screen.get_height()/700-0.5)
                           if DWID == 0 or DHIG == 0:
                               DWID = 1
                               DHIG = 1
                           if DWID == DHIG or DWID > DHIG:
                               C_SCL = DHIG
                               edi_screen = pygame.transform.scale(screen.copy(), [DHIG*900, DHIG*700])
                           else:
                               C_SCL = DWID
                               edi_screen = pygame.transform.scale(screen.copy(), [DWID*900, DWID*700])
                           display_screen.blit(edi_screen, [(display_screen.get_width()/2)-(edi_screen.get_width()/2), (display_screen.get_height()/2)-(edi_screen.get_height()/2)])
                        else:
                           display_screen.blit(screen, [0, 0])
                        pygame.event.get()
                        pygame.display.update()
                        while not keys[pygame.K_ESCAPE]:
                           keys = pygame.key.get_pressed()
                           pygame.event.get()
                           time.sleep(0.9)
           elif SLC == 3:
               pygame.display.set_caption("MUSPL2: Music Player")
               pygame.draw.rect(screen, [255, 140, 0], pygame.Rect(597, 45, 130, 5))
               OPTS = ["Shuffle", "Previous", "Play/Pause", "Skip", "Stop"]
               ROTATE("ICON", [99, 200], round(RL), [303, 303], True, [490, 200])
               #ROTATE("ICON", [257, 351], round(RL), [303, 303])
               if len(NEXT) > 1: #PLIST and SHNEXT:
                   if len(NEXT)-POINT > 15:
                       NUP = 15
                   else:
                       NUP = len(NEXT)-POINT
                   PNUP = POINT + 1
                   PNUPY = 150
                   #print("WORK", NUP)
                   for NXUP in range(NUP):
                       try:
                           NAM = NEXT[PNUP]
                           NAM = NAM.split(" - ")
                           TXT = LFONT.render(NAM[0][:16], False, [200, 100, 33]) #[0, 27, 51])
                           screen.blit(TXT, [round(245-TXT.get_width()), PNUPY])
                           TXT = LFONT.render(NAM[1].replace(".mp3", "")[:16], False, [200, 100, 33]) #[0, 27, 51])
                           screen.blit(TXT, [655, PNUPY])
                       except:
                           pass
                       PNUP += 1
                       PNUPY += 26
                       
               if ACVR != None:
                   if PLIST and ARTS != None:
                       screen.blit(ARTS, [250, 150])
                   else:
                       screen.blit(ACVR, [250, 150])
               else:
                   screen.blit(NOFILE, [250, 150])
               TXT = LFONT.render(CURR[:60].replace(".mp3", ""), False, [200, 100, 33])
               screen.blit(TXT, [round(450-(TXT.get_width()/2)), 556])
               if PP:
                   TXT = LFONT.render("|  Shuffle  |  Previous  |  Pause  |  Skip  |  Stop  |", False, [200, 100, 33])
               else:
                   TXT = LFONT.render("|  Shuffle  |  Previous  |  Play  |  Skip  |  Stop  |", False, [200, 100, 33])
               screen.blit(TXT, [round(450-(TXT.get_width()/2)), 583]) 
               if DIS:
                   TXT = LFONT.render("[" + str(OPTS[POS-1]) + "]", False, [200, 100, 33])
               else:
                   TXT = LFONT.render("[" + str(VOL) + "]", False, [200, 100, 33])
               if FRM > 0:
                   FRM -= 1
               else:
                   if not DIS:
                       CMD = "VOLS"
                   DIS = True
               screen.blit(TXT, [round(450-(TXT.get_width()/2)), 610])
               try:
                   MPOS = pygame.mixer.music.get_pos()/1000
               except:
                   pass
               try:
                   screen.blit(PROBAR, [-900+round((900/LENG)*MPOS), 670])
                   #pygame.draw.rect(screen, [200, 100, 33], pygame.Rect(0, 670, round((900/LENG)*MPOS), 30))
               except:
                   pass
               try:
                   SEC = round(CURL)
                   MMIN = str(round((SEC % 3600) // 60))[:2]
                   MSEC = str(round(SEC % 60))[:2]
                   if len(MMIN) == 1:
                       MMIN = "0" + MMIN
                   if len(MSEC) == 1:
                       MSEC = "0" + MSEC
                   SEC = int(pygame.mixer.music.get_pos()/1000)
                   MIN = str(round((SEC % 3600) // 60))[:2]
                   SEC = str(round(SEC % 60))[:2]
                   if len(MIN) == 1:
                       MIN = "0" + MIN
                   if len(SEC) == 1:
                       SEC = "0" + SEC
                   TXT = LFONT.render(str(MIN) + ":" + str(SEC) + " / " + str(MMIN) + ":" + str(MSEC), False, [0, 27, 47])
                   screen.blit(TXT, [10, 675])
               except Exception as E:
                   print(E)
               keys = pygame.key.get_pressed()
               #if keys[pygame.K_d]:
               #    try:
               #        REWD = pygame.mixer.music.get_pos()/1000
               #        print("========")
               #        print(LENG)
               #        print(REWD)
               #        pygame.mixer.music.play()
               #        REWD += 10
               #        if REWD > LENG:
               #            REWD = LENG
               #        print(REWD)
               #        pygame.mixer.music.set_pos(REWD)
               #        print(pygame.mixer.music.get_pos()/1000)
               #    except Exception as E:
               #        mixer.music.unpause()
               #elif keys[pygame.K_a]:
               #    try:
               #        REWD = pygame.mixer.music.get_pos()/1000
               #        print("========")
               #        print(LENG)
               #        print(REWD)
               #        pygame.mixer.music.play()
               #        REWD -= 10
               #        if REWD < 0:
               #            REWD = 0
               #        print(REWD)
               #        pygame.mixer.music.set_pos(REWD)
               #        print(pygame.mixer.music.get_pos()/1000)
               #    except:
               #        mixer.music.unpause()
               if keys[pygame.K_UP]:
                   POS -= 1
                   DIS = True
                   FRM = 200
                   time.sleep(0.3)
               elif keys[pygame.K_DOWN]:
                   POS += 1
                   DIS = True
                   FRM = 200
                   time.sleep(0.3)
               if POS > 5:
                   POS = 1
               elif POS < 1:
                   POS = 5
               if keys[pygame.K_RETURN]:
                   time.sleep(0.3)
                   if POS == 1:
                       CMD = "SHUFFLE"
                   elif POS == 2:
                       CMD = "PREVIUS"
                   elif POS == 3:
                       if PP:
                           CMD = "PAUSE"
                           PP = False
                       else:
                           CMD = "PLAY"
                           PP = True
                   elif POS == 4:
                       CMD = "SKIP"
                   else:
                       CMD = "STOP"
           elif SLC == 2:
               pygame.display.set_caption("MUSPL2: File Maneger")
               pygame.draw.rect(screen, [255, 140, 0], pygame.Rect(370, 45, 140, 5))
               if MODE == 2:
                   OUT = ".mp3"
                   Y = 48
                   RES = 0
                   if FILS != []:
                       OFILS = FILS
                   AFILS = []
                   FILS = []
                   DIR = dir_path = os.path.dirname(os.path.realpath("MUSPL2.py"))
                   for root, dirs, files in os.walk(DIR):
                       for file in files:
                           if OUT.lower() in file.lower() and RES-SCROLL < 42 and RES >= SCROLL:
                               FILS.append(str(file))
                           if OUT.lower() in file.lower():
                               RES += 1
                               AFILS.append(str(file))
                   for I in range(len(FILS)):
                       if FILS[I] != "":
                           Y += 15
                           if HIG-SCROLL == I:
                               if SELEC:
                                   if POS == 1:
                                       TXT = FONT.render("::::: |>ADD<| EXIT SELECTION |", False, [200, 100, 33])
                                   else:
                                       TXT = FONT.render("::::: | ADD |>EXIT SELECTION<|", False, [200, 100, 33])
                               else:
                                   TXT = FONT.render(":> " + str(FILS[I]), False, [200, 100, 33])
                           else:
                               TXT = FONT.render("::::: " + str(FILS[I]), False, [200, 100, 33])
                           screen.blit(TXT, [4, Y])
                   keys = pygame.key.get_pressed()
                   tim = 0.3-(VEL)/200
                   if tim < 0.02:
                       tim = 0.02
                   if keys[pygame.K_DOWN]:
                       if SELEC:
                           POS += 1
                           if POS > 2:
                               POS = 1
                           time.sleep(0.3)
                       else:
                           HIG += 1
                           VEL += 4
                           if HIG > RES:
                               HIG = 0
                           time.sleep(tim)
                   elif keys[pygame.K_UP]:
                       if SELEC:
                           POS -= 1
                           if POS < 1:
                               POS = 2
                           time.sleep(0.3)
                       else:
                           HIG -= 1
                           VEL += 4
                           if HIG < 0:
                               HIG = RES
                           time.sleep(tim)
                   elif keys[pygame.K_RETURN]:
                       if SELEC:
                           if POS == 1:
                               MODE = 1
                               PREAD.insert(INSC, FILS[HIG-SCROLL])
                               HIG = 0
                           SELEC = False
                           POS = 1
                       else:
                           SELEC = True
                       time.sleep(0.3)
                   else:
                       VEL = 0
                       time.sleep(0.01)
                   if HIG > SCROLL+42:
                       SCROLL = HIG
                   elif HIG < SCROLL:
                       SCROLL = SCROLL - 42
               elif MODE == 0:
                   if NOPLST:
                       TXT = FONT.render("No Playlists", False, [200, 100, 33])
                       screen.blit(TXT, [10, 63])
                   else:
                       screen.blit(MUS, [250, 50])
                   OUT = ".plist"
                   Y = 48
                   RES = 0
                   if FILS != []:
                       OFILS = FILS
                   FILS = []
                   DIR = dir_path = os.path.dirname(os.path.realpath("MUSPL2.py"))
                   for root, dirs, files in os.walk(DIR):
                       for file in files:
                           if OUT.lower() in file.lower() and RES < 42:
                               FILS.append(str(file))
                               RES += 1
                           if RES > 42:
                               break
                   for I in range(len(FILS)):
                       if FILS[I] != "":
                           Y += 15
                           if HIG == I:
                               if SELEC:
                                   if POS == 1:
                                       TXT = FONT.render("::::: |>EDIT<| EXIT SELECTION |", False, [200, 100, 33])
                                   else:
                                       TXT = FONT.render("::::: | EDIT |>EXIT SELECTION<|", False, [200, 100, 33])
                               else:
                                   TXT = FONT.render(":> " + str(FILS[I][:20]), False, [200, 100, 33])
                           else:
                               TXT = FONT.render("::::: " + str(FILS[I][:20]), False, [200, 100, 33])
                           screen.blit(TXT, [4, Y])
                   try:
                       FILE = open(FILS[HIG], "r+", encoding = "utf-8", errors="ignore")
                       READ = FILE.read().split("\n")
                       del READ[0]
                   except:
                       READ = []
                   NOPLST = False
                   try:
                       TXT = LFONT.render(FILS[HIG].replace(".plist", "")[:18], False, [0, 0, 0])
                       screen.blit(TXT, [395-(TXT.get_width()/2), 130])
                       TXT = FONT.render(str(len(READ)), False, [0, 0, 0])
                       screen.blit(TXT, [270, 230])
                   except:
                       NOPLST = True
                   Y = 305
                   X = 250
                   for I in range(len(READ)):
                       TXT = FONT.render(READ[I][:40], False, [200, 100, 33])
                       screen.blit(TXT, [X, Y])
                       Y += 15
                       if I == 23:
                           X = 560
                           Y = 105
                       elif I >= 62:
                           break
                   keys = pygame.key.get_pressed()
                   tim = 0.3-(VEL)/200
                   if tim < 0.02:
                       tim = 0.02
                   if keys[pygame.K_DOWN]:
                       if SELEC:
                           POS += 1
                           if POS > 2:
                               POS = 1
                           time.sleep(0.3)
                       else:
                           HIG += 1
                           VEL += 1
                           if HIG > len(FILS)-1:
                               HIG = 0
                           time.sleep(tim)
                   elif keys[pygame.K_UP]:
                       if SELEC:
                           POS -= 1
                           if POS < 1:
                               POS = 2
                           time.sleep(0.3)
                       else:
                           HIG -= 1
                           VEL += 1
                           if HIG < 0:
                               HIG = len(FILS)-1
                           time.sleep(tim)
                   elif keys[pygame.K_RETURN]:
                       if SELEC:
                           if POS == 1:
                               MODE = 1
                               try:
                                   FNAM = FILS[HIG]
                                   FILE = open(FILS[HIG], "r+", encoding = "utf-8", errors="ignore")
                                   PREAD = FILE.read().split("\n")
                                   FILE.close()
                                   DETA = PREAD[0]
                                   del PREAD[0]
                               except Exception as E:
                                   #print(E)
                                   PREAD = []
                           SELEC = False
                           POS = 1
                       else:
                           SELEC = True
                       time.sleep(0.3)
                   else:
                       VEL = 0
                       time.sleep(0.01)
               else:
                   Y = 48
                   for I in range(len(PREAD)):
                       if PREAD[I] != "":
                           Y += 15
                           if HIG == I:
                               if SELEC:
                                   if POS == 1:
                                       TXT = FONT.render("::::: |>REMOVE<| ADD | EXIT SELECTION | SAVE |", False, [200, 100, 33])
                                   elif POS == 2:
                                       TXT = FONT.render("::::: | REMOVE |>ADD<| EXIT SELECTION | SAVE |", False, [200, 100, 33])
                                   elif POS == 3:
                                       TXT = FONT.render("::::: | REMOVE | ADD |>EXIT SELECTION<| SAVE |", False, [200, 100, 33])
                                   else:
                                       TXT = FONT.render("::::: | REMOVE | ADD | EXIT SELECTION |>SAVE<|", False, [200, 100, 33])
                               else:
                                   TXT = FONT.render(":> " + str(PREAD[I]), False, [200, 100, 33])
                           else:
                               TXT = FONT.render("::::: " + str(PREAD[I]), False, [200, 100, 33])
                           screen.blit(TXT, [4, Y])
                   keys = pygame.key.get_pressed()
                   tim = 0.3-(VEL)/200
                   if tim < 0.02:
                       tim = 0.02
                   if keys[pygame.K_DOWN]:
                       if SELEC:
                           POS += 1
                           if POS > 4:
                               POS = 1
                           time.sleep(0.3)
                       else:
                           HIG += 1
                           VEL += 1
                           if HIG > len(FILS)-1:
                               HIG = 0
                           time.sleep(tim)
                   elif keys[pygame.K_UP]:
                       if SELEC:
                           POS -= 1
                           if POS < 1:
                               POS = 4
                           time.sleep(0.3)
                       else:
                           HIG -= 1
                           VEL += 1
                           if HIG < 0:
                               HIG = len(FILS)-1
                           time.sleep(tim)
                   elif keys[pygame.K_RETURN]:
                       if SELEC:
                           if POS == 1:
                               del PREAD[HIG]
                               SELEC = False
                           elif POS == 2:
                               MODE = 2
                               INSC = HIG
                               HIG = 0
                               SELEC = False
                           elif POS == 3:
                               SELEC = False
                           else:
                               SELEC = False
                               screen.blit(SAVE, [0,0])
                               if display_screen.get_width() != 900 or display_screen.get_height() != 700:
                                   #display_screen.fill([0, 47, 71])
                                   display_screen.fill([0, 0, 0])
                                   DWID = round(display_screen.get_width()/900-0.5)
                                   DHIG = round(display_screen.get_height()/700-0.5)
                                   if DWID == 0 or DHIG == 0:
                                       DWID = 1
                                       DHIG = 1
                                   if DWID == DHIG or DWID > DHIG:
                                       edi_screen = pygame.transform.scale(screen.copy(), [DHIG*900, DHIG*700])
                                   else:
                                       edi_screen = pygame.transform.scale(screen.copy(), [DWIG*900, DWIG*700])
                                   display_screen.blit(edi_screen, [(display_screen.get_width()/2)-(edi_screen.get_width()/2), (display_screen.get_height()/2)-(edi_screen.get_height()/2)])
                               else:
                                   display_screen.blit(screen, [0, 0])
                               pygame.event.get()
                               pygame.display.update()
                               time.sleep(0.3)
                               FILE = open(FNAM, "w+", encoding="utf-8", errors="ignore")
                               FILE.write(DETA + "\n")
                               TFRM = 0
                               for I in range(len(PREAD)):
                                   FILE.write(PREAD[I] + "\n")
                                   if TFRM > 100:
                                       TFRM = 0
                                       pygame.event.get()
                                   else:
                                       TFRM += 1
                               FILE.close()
                               MODE = 0
                           time.sleep(0.3)
                       else:
                           SELEC = True
                           time.sleep(0.3)
                   else:
                       VEL = 0
                       time.sleep(0.01)
           elif SLC == 1:
               pygame.display.set_caption("MUSPL2: All Playlists")
               pygame.draw.rect(screen, [255, 140, 0], pygame.Rect(178, 45, 120, 5))
               OUT = ".plist"
               Y = 48
               RES = 0
               if FILS != []:
                   OFILS = FILS
               FILS = ["Play All"]
               DIR = dir_path = os.path.dirname(os.path.realpath("MUSPL2.py"))
               for root, dirs, files in os.walk(DIR):
                   for file in files:
                       if OUT.lower() in file.lower() and RES < 42:
                           FILS.append(str(file))
                           RES += 1
                       if RES > 42:
                           break
               for I in range(len(FILS)):
                   if FILS[I] != "":
                       Y += 15
                       if HIG == I:
                           if SELEC:
                               if POS == 1 or HIG == 0 and POS == 2:
                                   TXT = FONT.render("::::: |>PLAY NOW<| ADD TO QUEUE | EXIT SELECTION |", False, [200, 100, 33])
                               elif POS == 2:
                                   TXT = FONT.render("::::: | PLAY NOW |>ADD TO QUEUE<| EXIT SELECTION |", False, [200, 100, 33])
                               else:
                                   TXT = FONT.render("::::: | PLAY NOW | ADD TO QUEUE |>EXIT SELECTION<|", False, [200, 100, 33])
                           else:
                               TXT = FONT.render(":> " + str(FILS[I]), False, [200, 100, 33])
                       else:
                           TXT = FONT.render("::::: " + str(FILS[I]), False, [200, 100, 33])
                       screen.blit(TXT, [4, Y])
               keys = pygame.key.get_pressed()
               tim = 0.3-(VEL)/200
               if tim < 0.02:
                   tim = 0.02
               if keys[pygame.K_DOWN]:
                   if SELEC:
                       POS += 1
                       if POS > 3:
                           POS = 1
                       time.sleep(0.3)
                   else:
                       HIG += 1
                       VEL += 1
                       if HIG > len(FILS)-1:
                           HIG = 0
                       time.sleep(tim)
               elif keys[pygame.K_UP]:
                   if SELEC:
                       POS -= 1
                       if POS < 1:
                           POS = 3
                       time.sleep(0.3)
                   else:
                       HIG -= 1
                       VEL += 1
                       if HIG < 0:
                           HIG = len(FILS)-1
                       time.sleep(tim)
               elif keys[pygame.K_RETURN]:
                   if SELEC:
                       if POS == 1 or HIG == 0 and POS == 2:
                           if HIG == 0:
                               NEXT = []
                               DIR = dir_path = os.path.dirname(os.path.realpath("MUSPL2.py"))
                               for root, dirs, files in os.walk(DIR):
                                   for file in files:
                                       if ".mp3" in file.lower():
                                           NEXT.append(str(file))
                               PUSH = True
                               PLIST = True
                               POINT = 0
                           else:
                               IN = FILS[HIG]
                               try:
                                   FILE = open(IN, "r+", encoding = "utf-8", errors = "ignore")
                                   LIST = FILE.read().split("\n")
                                   IN = LIST[0]
                                   I = 0
                                   if ":ALBUM: " in IN:
                                       IN = IN.replace(":ALBUM: ", "")
                                       ACVR = pygame.image.load(IN).convert_alpha()
                                       ACVR = pygame.transform.scale(ACVR, (400, 400))
                                       I = 1
                                       del LIST[0]
                                       NEXT = LIST
                                       PUSH = True
                                   PLIST = True
                                   POINT = 0
                               except Exception as E:
                                   #print(E)
                                   pass
                       elif POS == 2:
                           IN = FILS[HIG]
                           try:
                               FILE = open(IN, "r+", encoding = "utf-8", errors = "ignore")
                               LIST = FILE.read().split("\n")
                               IN = LIST[0]
                               del LIST[0]
                               CHK = " ".join(NEXT) + " "
                               for I in range(len(LIST)):
                                   if LIST[I] not in CHK:
                                       NEXT.append(LIST[I])
                                       CHK += LIST[I] + " "
                               PLIST = True
                           except Exception as E:
                               print(E)
                               pass
                           if type(POINT) != int:
                               POINT = 0
                       SELEC = False
                       POS = 1
                   else:
                       SELEC = True
                   time.sleep(0.3)
               else:
                   VEL = 0
                   time.sleep(0.01)
           elif SLC == 0:
               pygame.draw.rect(screen, [255, 140, 0], pygame.Rect(15, 45, 95, 5))
               if SEARCH:
                   screen.blit(SRCH, [652,55])
                   if TXTDIS != "":
                       TXT = FONT.render(TXTDIS, False, [200, 100, 33])
                   elif LOOKFOR == "":
                       TXT = FONT.render("Enter Text To Find", False, [200, 100, 33])
                   else:
                       TXT = FONT.render(LOOKFOR[:15], False, [200, 100, 33])
                   screen.blit(TXT, [703, 77])
               else:
                   screen.blit(SRCH, [852,55])
               OUT = ".mp3"
               Y = 48
               RES = 0
               if FILS != []:
                   OFILS = FILS
               AFILS = []
               FILS = []
               DIR = dir_path = os.path.dirname(os.path.realpath("MUSPL2.py"))
               for root, dirs, files in os.walk(DIR):
                   for file in files:
                       if LOOKFOR.lower() in file.lower() or not SEARCH:
                           if OUT.lower() in file.lower() and RES-SCROLL < 42 and RES >= SCROLL:
                               FILS.append(str(file))
                           if OUT.lower() in file.lower():
                               RES += 1
                               AFILS.append(str(file))
               for I in range(len(FILS)):
                   if FILS[I] != "":
                       Y += 15
                       if HIG-SCROLL == I:
                           if SELEC:
                               if POS == 1:
                                   TXT = FONT.render("::::: |>ADD TO QUEUE<| PLAY NOW | EXIT SELECTION |", False, [200, 100, 33])
                               elif POS == 2:
                                   TXT = FONT.render("::::: | ADD TO QUEUE |>PLAY NOW<| EXIT SELECTION |", False, [200, 100, 33])
                               else:
                                   TXT = FONT.render("::::: | ADD TO QUEUE | PLAY NOW |>EXIT SELECTION<|", False, [200, 100, 33])
                           else:
                               TXT = FONT.render(":> " + str(FILS[I]), False, [200, 100, 33])
                       else:
                           TXT = FONT.render("::::: " + str(FILS[I]), False, [200, 100, 33])
                       screen.blit(TXT, [4, Y])
               keys = pygame.key.get_pressed()
               if SEARCH:
                   if SELEC:
                       if POS == 1:
                           TXTDIS = "|>ADD<| PLAY | EXIT |"
                       elif POS == 2:
                           TXTDIS = "| ADD |>PLAY<| EXIT |"
                       else:
                           TXTDIS = "| ADD | PLAY |>EXIT<|"
                       if keys[pygame.K_UP]:
                           POS -= 1
                           if POS < 1:
                               POS = 3
                           time.sleep(0.15)
                       elif keys[pygame.K_DOWN]:
                           POS += 1
                           if POS > 3:
                               POS = 1
                           time.sleep(0.15)
                   if keys[pygame.K_RETURN] and not SELEC:
                       SELEC = True
                       time.sleep(0.1)
                   elif keys[pygame.K_RETURN] and SELEC:
                       if POS == 1:
                           if len(NEXT) == 0:
                               PUSH = True
                           NEXT.append(AFILS[HIG])
                           PP = True
                       elif POS == 2:
                           NEXT = [AFILS[HIG]]
                           PLIST = False
                           PUSH = True
                           PP = True
                       SELEC = False
                       SEARCH = False
                       POS = 1
                   else:
                       if keys[pygame.K_BACKSPACE]:
                           LOOKFOR = LOOKFOR[:-1]
                       else:
                           CHR = ""
                           for I in range(26):
                               if keys[I + 97]:
                                   CHR = chr(I + 97)
                                   break
                           if CHR == "":
                               for I in range(10):
                                   if keys[I + 48]:
                                       CHR = chr(I + 48)
                                       break
                           LOOKFOR += CHR
                           time.sleep(0.09)
               else:
                   if pygame.mouse.get_pressed()[0]:
                       XY = pygame.mouse.get_pos()
                       XY = DisToScr(XY)
                       if XY[0] >= 849 and XY[0] <= 900 and XY[1] >= 61 and XY[1] <= 110:
                           SEARCH = True
                           SELEC = False
                           LOOKFOR = ""
                           TXTDIS = ""
                           POS = 1
                   tim = 0.3-(VEL)/200
                   if tim < 0.02:
                       tim = 0.02
                   if keys[pygame.K_DOWN]:
                       if SELEC:
                           POS += 1
                           if POS > 3:
                               POS = 1
                           time.sleep(0.3)
                       else:
                           HIG += 1
                           VEL += 4
                           if HIG > RES:
                               HIG = 0
                           time.sleep(tim)
                   elif keys[pygame.K_q]:
                       if SEARCH:
                           SEARCH = False
                           SELEC = False
                       else:
                           SEARCH = True
                           SELEC = False
                           LOOKFOR = ""
                           TXTDIS = ""
                           POS = 1
                       time.sleep(0.1)
                   elif keys[pygame.K_UP]:
                       if SELEC:
                           POS -= 1
                           if POS < 1:
                               POS = 3
                           time.sleep(0.3)
                       else:
                           HIG -= 1
                           VEL += 4
                           if HIG < 0:
                               HIG = RES
                           time.sleep(tim)
                   elif keys[pygame.K_RETURN]:
                       if SELEC:
                           if POS == 1:
                               if len(NEXT) == 0:
                                   PUSH = True
                               NEXT.append(AFILS[HIG])
                               PP = True
                           elif POS == 2:
                               NEXT = [AFILS[HIG]]
                               PLIST = False
                               PUSH = True
                               PP = True
                           SELEC = False
                           POS = 1
                       else:
                           SELEC = True
                       time.sleep(0.3)
                   else:
                       VEL = 0
                       time.sleep(0.01)
                   if HIG > SCROLL+42:
                       SCROLL = HIG
                   elif HIG < SCROLL:
                       SCROLL = SCROLL - 42
           if not SEARCH:
               if keys[pygame.K_w]:
                   CMD = "VOL+"
                   FRM = 40
                   DIS = False
                   time.sleep(0.2)
               elif keys[pygame.K_s]:
                   CMD = "VOL-"
                   FRM = 40
                   DIS = False
                   time.sleep(0.2)
               if pygame.mouse.get_pressed()[0]:
                   XY = pygame.mouse.get_pos()
                   XY = DisToScr(XY)
                   #print(XY)
                   if XY[1] >= 0 and XY[1] <= 60:
                       if XY[0] <= 143:
                           SLC = 0
                       elif XY[0] <= 324:
                           SLC = 1
                       elif XY[0] <= 547:
                           SLC = 2
                       elif XY[0] <= 770:
                           SLC = 3
                       elif XY[0] <= 900:
                           SLC = 4
               for event in pygame.event.get():
                   #print("chk")
                   if event.type == pygame.MOUSEWHEEL:
                       #print(event.x, event.y)
                       if event.x != 0:
                           SLC += -(event.x)
                           if SLC > 4:
                               SLC = 0
                           elif SLC < 0:
                               SLC = 4
                           time.sleep(0.1)
                       else:
                           #print(POS)
                           if SLC >= 0 and SLC <= 2 and SELEC:
                                POS += -(event.y)
                           elif SLC == 3:
                               POS += -(event.y)
                               if POS > 5:
                                   POS = 1
                               elif POS < 1:
                                   POS = 5
                           elif SLC == 4:
                               PPOS += -(event.y)
                               if PPOS > 2:
                                   PPOS = 0
                               elif PPOS < 0:
                                   PPOS = 2
                           else:
                               HIG += -(event.y)
                               VEL += -(event.y*4)
                               if HIG > RES:
                                   HIG = 0
                               elif HIG < 0:
                                   HIG = RES
               if keys[pygame.K_LEFT]:
                   SCROLL = 0
                   POS = 1
                   SLC -= 1
                   HIG = 0
                   if SLC < 0:
                       SLC = 4
                   time.sleep(0.3)
               elif keys[pygame.K_RIGHT]:
                   SCROLL = 0
                   POS = 1
                   HIG = 0
                   SLC += 1
                   if SLC > 4:
                       SLC = 0
                   time.sleep(0.3)
           if PP:
               RL += 0.1*DWID
               if RL >= 360:
                   RL = 0
           if display_screen.get_width() != 900 or display_screen.get_height() != 700:
               #display_screen.fill([0, 47, 71])
               display_screen.fill([0, 0, 0])
               DWID = round(display_screen.get_width()/900-0.5)
               DHIG = round(display_screen.get_height()/700-0.5)
               if DWID == 0 or DHIG == 0:
                   DWID = 1
                   DHIG = 1
               if DWID == DHIG or DWID > DHIG:
                   C_SCL = DHIG
                   edi_screen = pygame.transform.scale(screen.copy(), [DHIG*900, DHIG*700])
               else:
                   C_SCL = DWID
                   edi_screen = pygame.transform.scale(screen.copy(), [DWID*900, DWID*700])
               display_screen.blit(edi_screen, [(display_screen.get_width()/2)-(edi_screen.get_width()/2), (display_screen.get_height()/2)-(edi_screen.get_height()/2)])
           else:
               display_screen.blit(screen, [0, 0])
           pygame.event.get()
           pygame.display.update()
       else:
           if RFF >= 100:
               RFF = 0
               pygame.event.get()
           else:
               RFF += 1
       CHK_PLAYER()
       time.sleep(0.01)
try:
    import pygame
    import os
    import random
    import time
    import numpy
    from moviepy.editor import *
    from pygame import mixer
    import ctypes
    from moviepy.editor import *
    import cv2
    from datetime import datetime
    from subprocess import call
    import subprocess
    from pynput.keyboard import Key,Controller
    import platform
    PLT = platform.system()
except:
    print("-Library Error-")
    print("You do not have all of the nessisary")
    print("libraries to run this application,")
    print("to run this application please install")
    print("all of the nessisary libraries automatically")
    print("by selecting AUTO by typing AUTO and pressing")
    print("enter/return on your keyboard or by typing")
    print("MANUAL to display the nessisary libraries.")
    print("otherwise type anything else to quit.")
    print("")
    IN = input("> ").lower()
    if IN == "auto":
        print("-Auto Install-")
        print("This application will download files to")
        print("your computer, do you consent to this")
        print("action. Like everything in life there")
        print("are risks if you consent type YES and")
        print("press enter/return.")
        print("")
        IN = input("> ")
        if IN == "YES":
            print("-Auto Installer-")
            NAME = ["pygame", "numpy", "moviepy", "opencv-python", "pynput"]
            ERROR = 0
            for I in range(len(NAME)):
                print("Installing: " + str(NAME[I]))
                try:
                    if PLT == "Windows":
                        os.system('py -m pip install ' + str(NAME[I]))
                    else:
                        bashCommand = "python3 -m pip install " + str(NAME[I])
                        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                        process.communicate()
                except Exception as E:
                    print("Error: " + str(E))
                    input("PRESS ENTER/RETURN TO CONTINUE")
                    ERROR += 1
            if ERROR == 0:
                print("-Auto Installer-")
                print("Install compleated successfully. Fingers")
                print("crossed this program should work when")
                print("reopened.")
                input("PRESS ENTER/RETURN TO EXIT")
            else:
                print("-Auto Installer-")
                print("There were some errors please troubleshoot")
                print("these errors or contact software distributer")
                print("for help or use given helpline for issues.")
                print("Total Errors: " + str(ERROR))
                input("PRESS ENTER/RETURN TO EXIT")
    elif IN == "manual":
        print("-Libraries Required-")
        print("pygame, numpy, moviepy,")
        print("ctypes, cv2, subprocess, pynput")
        print("")
        input("PRESS ENTER/RETURN TO EXIT")
    for I in range(1000):
        quit()
        exit()
keyboard = Controller()
CMD = ""
SET_VOL(0.5)
NEXT = []
pygame.init()
os.system("cls")
MODE = True
SHNEXT = True
LENG = 0
MPOS = 0
EURO = False
SUPSHF = True
CHIME = True
SLEP = True
BEEP = True
NXT = True
ACVR = None
ARTS = None
C_SCL = 1
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
for I in range(random.randint(10, 80)):
    random.randint(1, 100)
if os.path.isfile("Muspl2-Settings.txt"):
    FILE = open("Muspl2-Settings.txt", "r+", encoding = "utf-8")
    try:
        exec(FILE.read(), globals())
    except:
        print("ERR")
if MODE:
    DISPLAY = pygame.display.Info()
    display_screen = pygame.display.set_mode((DISPLAY.current_w, DISPLAY.current_h), pygame.FULLSCREEN, pygame.NOFRAME)
else:
    display_screen = pygame.display.set_mode((900, 700), pygame.RESIZABLE)
screen = pygame.Surface((900, 700))
ICON = pygame.image.load("MUSPL2.png").convert_alpha()
pygame.display.set_icon(ICON)
pygame.display.set_caption("MUSPL2: Starting...")
MFONT = pygame.font.Font("W95FA.OTF", 52)
LFONT = pygame.font.Font("W95FA.OTF", 26)
FONT = pygame.font.Font("W95FA.OTF", 13)
CFONT = pygame.font.Font("W95FA.OTF", 156)
AFONT = pygame.font.Font("W95FA.OTF", 39)
NOFILE = pygame.image.load("NoFile.png").convert_alpha()
NOFILE = pygame.transform.scale(NOFILE, (400, 400))
PROBAR = pygame.image.load("MUSPL_Bar.png").convert_alpha()
PROBAR = pygame.transform.scale(PROBAR, (900, 30))
PBOX = pygame.image.load("MUSPL_Power.png").convert_alpha()
BACK = pygame.image.load("MusicPlayer.png").convert_alpha()
CLK = pygame.image.load("CLKFCE.png").convert_alpha()
CLK0 = pygame.image.load("CLKFCE0.png").convert_alpha()
CLK9 = pygame.image.load("CLKFCE9.png").convert_alpha()
CLK8 = pygame.image.load("CLKFCE8.png").convert_alpha()
CLK7 = pygame.image.load("CLKFCE7.png").convert_alpha()
CLK6 = pygame.image.load("CLKFCE6.png").convert_alpha()
CLK5 = pygame.image.load("CLKFCE5.png").convert_alpha()
CLK4 = pygame.image.load("CLKFCE4.png").convert_alpha()
CLK3 = pygame.image.load("CLKFCE3.png").convert_alpha()
CLK2 = pygame.image.load("CLKFCE2.png").convert_alpha()
CLK1 = pygame.image.load("CLKFCE1.png").convert_alpha()
SRCH = pygame.image.load("Muspl_Search.png").convert_alpha()
SAVE = MUS = pygame.image.load("MUSPL_Save.png").convert_alpha()
MUS = pygame.image.load("MUS.png").convert_alpha()
MUS = pygame.transform.scale(MUS, (300, 300))
mixer.init()
keys = pygame.key.get_pressed()
EXIT = False
SLC = 0
SEARCH = False
LOOKFOR = ""
DWID = 1
RL = 0
VOL = 50
SET_VOL(VOL/100)
PREV = ""
POINT = 0
PLIST = False
RAND = False
PUSH = False
CURR = "Not Playing"
CURL = 0
FIRST = pygame.image.load("MUSPL LOGO.png").convert_alpha()
screen.blit(FIRST, [0,0])
if display_screen.get_width() != 900 or display_screen.get_height() != 700:
   display_screen.fill([0, 0, 0])
   DWID = round(display_screen.get_width()/900-0.5)
   DHIG = round(display_screen.get_height()/700-0.5)
   if DWID == 0 or DHIG == 0:
       DWID = 1
       DHIG = 1
   if DWID == DHIG or DWID > DHIG:
       C_SCL = DHIG
       edi_screen = pygame.transform.scale(screen.copy(), [DHIG*900, DHIG*700])
   else:
       C_SCL = DWID
       edi_screen = pygame.transform.scale(screen.copy(), [DWID*900, DWID*700])
   display_screen.blit(edi_screen, [(display_screen.get_width()/2)-(edi_screen.get_width()/2), (display_screen.get_height()/2)-(edi_screen.get_height()/2)])
else:
   display_screen.blit(screen, [0, 0])
pygame.event.get()
pygame.display.update()
for I in range(12):
    pygame.event.get()
    time.sleep(0.1)
if not os.path.isfile("Readme.txt") and not os.path.isfile("Muspl2-Settings.txt"):
    FILE = open("Muspl2-Settings.txt", "w+", encoding = "utf-8")
    FILE.write("MODE = True\n")
    FILE.write("EURO = False\n")
    FILE.write("SHNEXT = True\n")
    FILE.write("SUPSHF = True\n")
    FILE.write("CHIME = False\n")
    FILE.write("SLEP = True\n")
    FILE.write("BEEP = True\n")
    FILE.write("NXT = True\n")
    FILE.close()
    FILE = open("Readme.txt", "w+", encoding = "utf-8")
    FILE.write("--Customizable Fetures Variable Names--\n")
    FILE.write("MODE: Display Mode, True for Fullscreen, False for Resizable\n")
    FILE.write("SHNEXT: Show Next songs in music player pannel\n")
    FILE.write("EURO: 24h clock in alarm/clock function\n")
    FILE.write("SUPSHF: Supershuffle, super slow on really large playlists >1000 songs\n")
    FILE.write("CHIME: in clock/alarm function chime every hour (bell by default)\n")
    FILE.write("SLEP: past 22/10pm the clock/alarm function will turn off the music untill after the alarm\n")
    FILE.write("BEEP: use beeping alarm or raise music for alarm\n")
    FILE.write("NXT: Show Next songs in clock/alarm function\n")
    FILE.write("You can change the .mp3 files to change certain playfetures ex: alarm/hour chime\n")
    FILE.write("--Standard Formats--\n")
    FILE.write(".plist playlist files, each song is a new line where the file name is given, except the first one\n")
    FILE.write("which is the default image for the 'album' which is indicated by :ALBUM: then the .png file\n")
    FILE.write(".mp3 all songs are formatted in this way ARTIST/BAND - SONG TITLE\n")
    FILE.write("if you name a image the artist/band that a song is from it will display that artist/band art when playing\n")
    FILE.close()
    FIRST = pygame.image.load("MUSPL2 FIRST.png").convert_alpha()
    screen.blit(FIRST, [0,0])
    if display_screen.get_width() != 900 or display_screen.get_height() != 700:
       display_screen.fill([0, 0, 0])
       DWID = round(display_screen.get_width()/900-0.5)
       DHIG = round(display_screen.get_height()/700-0.5)
       if DWID == 0 or DHIG == 0:
           DWID = 1
           DHIG = 1
       if DWID == DHIG or DWID > DHIG:
           C_SCL = DHIG
           edi_screen = pygame.transform.scale(screen.copy(), [DHIG*900, DHIG*700])
       else:
           C_SCL = DWID
           edi_screen = pygame.transform.scale(screen.copy(), [DWID*900, DWID*700])
       display_screen.blit(edi_screen, [(display_screen.get_width()/2)-(edi_screen.get_width()/2), (display_screen.get_height()/2)-(edi_screen.get_height()/2)])
    else:
       display_screen.blit(screen, [0, 0])
    pygame.event.get()
    pygame.display.update()
    for I in range(400):
        pygame.event.get()
        time.sleep(0.1)

MUS_DISPLAY()    
while True:
    try:
        MUS_DISPLAY()
    except Exception as E:
        print(E)
