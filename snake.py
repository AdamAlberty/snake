from email.mime import image
import tkinter, random
canvas = tkinter.Canvas(background="#9ADCFF")
canvas.pack()

# Config
VELKOST_POLICKA = 30
POCET_POLICOK = 20 # Strana
FPS = 5
FARBA_HADA = '#FFB2A6'
FARBA_JEDLA = '#FFB72B'
FARBA_CIARY = "#FFF89A"
FARBA_HLAVY = "#FF8AAE"
canvas["width"] = VELKOST_POLICKA * POCET_POLICOK
canvas["height"] = VELKOST_POLICKA * POCET_POLICOK
pole = [[0 for x in range(POCET_POLICOK)] for y in range(POCET_POLICOK)]
had = [[0, 5], [1, 5], [2, 5]]
jedlo = []
pohyb = [1, 0]
hra_sa = True
mozes_zmenit = True
jablko = tkinter.PhotoImage(file="apple.png")


def kresli_plochu():
	global pole
	for y in range(POCET_POLICOK):
		for x in range(POCET_POLICOK):
			canvas.create_rectangle(VELKOST_POLICKA * x, VELKOST_POLICKA * y, VELKOST_POLICKA * x + VELKOST_POLICKA, VELKOST_POLICKA * y + VELKOST_POLICKA, width=0, outline=FARBA_CIARY)

def kresli_hada():
    global had
    canvas.delete('had')
    
    for i, sur in enumerate(had):
        if i == (len(had) - 1):
            canvas.create_rectangle(VELKOST_POLICKA * sur[0], VELKOST_POLICKA * sur[1], VELKOST_POLICKA * sur[0] + VELKOST_POLICKA, VELKOST_POLICKA * sur[1] + VELKOST_POLICKA, fill=FARBA_HLAVY, width=0, tags="had")
        else:
            canvas.create_rectangle(VELKOST_POLICKA * sur[0], VELKOST_POLICKA * sur[1], VELKOST_POLICKA * sur[0] + VELKOST_POLICKA, VELKOST_POLICKA * sur[1] + VELKOST_POLICKA, fill=FARBA_HADA, width=0, tags="had")
        


def hra():
    global had, pohyb, mozes_zmenit, hra_sa

    if not hra_sa:
        return
    nova_hlava = [had[-1][0] + pohyb[0], had[-1][1] + pohyb[1]]

    if nova_hlava[0] >= POCET_POLICOK:
        nova_hlava[0] = 0
    elif nova_hlava[0] < 0:
        nova_hlava[0] = POCET_POLICOK - 1
    elif nova_hlava[1] >= POCET_POLICOK:
        nova_hlava[1] = 0
    elif nova_hlava[1] < 0:
        nova_hlava[1] = POCET_POLICOK - 1

    if nova_hlava in jedlo:
        vytvor_jedlo()
    elif nova_hlava in had:
        hra_sa = False
    else:
        had.pop(0)
    had.append(nova_hlava)
    kresli_hada()
    mozes_zmenit = True
    canvas.after(int(1 / FPS * 1000), hra)


def vytvor_jedlo():
    global jedlo
    jedlo = []
    canvas.delete('jedlo')

    # Generuj nove jedlo
    je_v_hadovi = True
    while je_v_hadovi:
        nove_jedlo = [random.randint(0, POCET_POLICOK - 1), random.randint(0, POCET_POLICOK - 1)]
        if nove_jedlo not in had:
            jedlo.append(nove_jedlo)
            je_v_hadovi = False

    canvas.create_image(VELKOST_POLICKA * nove_jedlo[0], VELKOST_POLICKA * nove_jedlo[1], image=jablko, tags="jedlo", anchor="nw")
    

def zmen_pohyb(x, y):
    global pohyb, mozes_zmenit
    if not mozes_zmenit:
        return
    if abs(pohyb[0]) == 1 and abs(x) == 1:
        return
    elif abs(pohyb[1]) == 1 and abs(y) == 1:
        return
    pohyb[0] = x
    pohyb[1] = y
    mozes_zmenit == False
    

# Start hry
kresli_plochu()
kresli_hada()
vytvor_jedlo()
hra()

canvas.bind_all('<Up>', lambda x: zmen_pohyb(0, -1))
canvas.bind_all('<Left>', lambda x: zmen_pohyb(-1, 0))
canvas.bind_all('<Down>', lambda x: zmen_pohyb(0, 1))
canvas.bind_all('<Right>', lambda x: zmen_pohyb(1, 0))
canvas.mainloop()