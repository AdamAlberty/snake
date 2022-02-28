import tkinter, random
canvas = tkinter.Canvas(background="skyblue")
canvas.pack()

# Config
VELKOST_POLICKA = 30
POCET_POLICOK = 10 # Strana
FPS = 10
FARBA_HADA = 'green'
FARBA_JEDLA = 'red'
canvas["width"] = VELKOST_POLICKA * POCET_POLICOK
canvas["height"] = VELKOST_POLICKA * POCET_POLICOK

pole = [[0 for x in range(POCET_POLICOK)] for y in range(POCET_POLICOK)]
had = [[0, 5], [1, 5], [2, 5]]
jedlo = []
pohyb = [1, 0]
mozes_zmenit = True

def kresli_plochu():
	global pole
	for y in range(POCET_POLICOK):
		for x in range(POCET_POLICOK):
			canvas.create_rectangle(VELKOST_POLICKA * x, VELKOST_POLICKA * y, VELKOST_POLICKA * x + VELKOST_POLICKA, VELKOST_POLICKA * y + VELKOST_POLICKA)

def kresli_hada():
    global had
    canvas.delete('had')
    for sur in had:
        canvas.create_rectangle(VELKOST_POLICKA * sur[0], VELKOST_POLICKA * sur[1], VELKOST_POLICKA * sur[0] + VELKOST_POLICKA, VELKOST_POLICKA * sur[1] + VELKOST_POLICKA, fill=FARBA_HADA, tags="had")


def hra():
    global had, pohyb, mozes_zmenit
    nova_hlava = [had[-1][0] + pohyb[0], had[-1][1] + pohyb[1]]

    if nova_hlava[0] >= POCET_POLICOK:
        nova_hlava[0] = 0
    elif nova_hlava[0] < 0:
        nova_hlava[0] = POCET_POLICOK - 1
    elif nova_hlava[1] >= POCET_POLICOK:
        nova_hlava[1] = 0
    elif nova_hlava[1] < 0:
        nova_hlava[1] = POCET_POLICOK - 1


    had.append(nova_hlava)
    
    if nova_hlava in jedlo:
        vytvor_jedlo()
    else:
        had.pop(0)



    
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

    canvas.create_rectangle(VELKOST_POLICKA * nove_jedlo[0], VELKOST_POLICKA * nove_jedlo[1], VELKOST_POLICKA * nove_jedlo[0] + VELKOST_POLICKA, VELKOST_POLICKA * nove_jedlo[1] + VELKOST_POLICKA, fill=FARBA_JEDLA, tags="jedlo")
    

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
    

    
    
kresli_plochu()
kresli_hada()
vytvor_jedlo()
hra()

canvas.bind_all('w', lambda x: zmen_pohyb(0, -1))
canvas.bind_all('a', lambda x: zmen_pohyb(-1, 0))
canvas.bind_all('s', lambda x: zmen_pohyb(0, 1))
canvas.bind_all('d', lambda x: zmen_pohyb(1, 0))

canvas.mainloop()