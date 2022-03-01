import tkinter, random
canvas = tkinter.Canvas(background="black", width=510, height=510)
canvas.pack()

pole = [[0 for x in range(17)] for y in range(17)]
had = [[0, 5], [1, 5], [2, 5]]
jedlo = []
pohyb = [1, 0]
hra_sa = True
mozes_zmenit = True


def kresli_plochu():
	global pole
	for y in range(17):
		for x in range(17):
			canvas.create_rectangle(30 * x, 30 * y, 30 * x + 30, 30 * y + 30, width=2, outline="white")


def kresli_hada():
    global had
    canvas.delete('had')
    for i, sur in enumerate(had):
        if i == (len(had) - 1):
            canvas.create_rectangle(30 * sur[0], 30 * sur[1], 30 * sur[0] + 30, 30 * sur[1] + 30, fill="white", width=0, tags="had")
        else:
            canvas.create_rectangle(30 * sur[0], 30 * sur[1], 30 * sur[0] + 30, 30 * sur[1] + 30, fill="white", width=0, tags="had")
        

def hra():
    global had, pohyb, mozes_zmenit, hra_sa
    if not hra_sa:
        return
    # Pridaj novy blok
    nova_hlava = [had[-1][0] + pohyb[0], had[-1][1] + pohyb[1]]

    if nova_hlava[0] >= 17:
        nova_hlava[0] = 0
    elif nova_hlava[0] < 0:
        nova_hlava[0] = 17 - 1
    elif nova_hlava[1] >= 17:
        nova_hlava[1] = 0
    elif nova_hlava[1] < 0:
        nova_hlava[1] = 17 - 1

    if nova_hlava in jedlo:
        vytvor_jedlo()
    elif nova_hlava in had:
        hra_sa = False
    else:
        had.pop(0)
    had.append(nova_hlava)
    kresli_hada()
    mozes_zmenit = True
    canvas.after(300, hra)


def vytvor_jedlo():
    global jedlo
    jedlo = []
    canvas.delete('jedlo')

    # Generuj nove jedlo
    je_v_hadovi = True
    while je_v_hadovi:
        nove_jedlo = [random.randint(0, 17 - 1), random.randint(0, 17 - 1)]
        if nove_jedlo not in had:
            jedlo.append(nove_jedlo)
            je_v_hadovi = False
    canvas.create_rectangle(30 * nove_jedlo[0], 30 * nove_jedlo[1], 30 * nove_jedlo[0] + 30, 30 * nove_jedlo[1] + 30, tags="jedlo", fill="yellow", width=0)
    

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