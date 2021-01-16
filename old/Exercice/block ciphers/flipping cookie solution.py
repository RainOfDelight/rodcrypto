"""
cookie = 8c377384d931ede06843f74503f3c4ddce6aaed391781e7243c509d36159127739c7328740a4e2b94ee9b7c916b77ec5
iv  =   8c377384d931 ede06843f7 4503f3c4dd  # questa parte andrebbe xorata con la riga di sotto
        a d m i n =  F a l s e

per evitare di avere admin=False, e avere admin=True, devo:
prendere iv, vedere i byte che xorano False, (tanto lo xor con la IV e' la vosa che va fatta per ultima, quindi ho influenza su di essa
iv X crypt = False
iv X crypt X False X True; = False X False X True;
newiv  =   8c377384d931 fff37155a9 4503f3c4dd
fff37155a9
data =  ce6aaed391781e7243c509d36159127739c7328740a4e2b94ee9b7c916b77ec5

"""