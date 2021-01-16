import PIL

from usefulfunc import *
from PIL import Image



lemur = PIL.Image.open("other/lemur_ed66878c338e662d3473f0d98eedbd0d.png")
lemurPixels = list(lemur.getdata())

flag = PIL.Image.open("other/flag_7ae18c704272532658c10b5faad06d74.png")
flagPixels = list(flag.getdata())
print(flag.size)
print(lemur.size)
newPixels=[]
for index in range(0, len(lemurPixels)):
    newPixels.append((lemurPixels[index][0]^flagPixels[index][0],lemurPixels[index][1]^flagPixels[index][1],lemurPixels[index][2]^flagPixels[index][2]))


print(len(newPixels))
# SECND SOLUTION
im = Image.new("RGB", (582,327))
im.putdata(newPixels)
im.save("other/daaaaje.png", "PNG")