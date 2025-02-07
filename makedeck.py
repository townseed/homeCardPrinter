from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from PIL import Image

# card = (2.75*inch, 3.75*inch)

verbose = False
fixedYOffset = 10
fixedXOffset = 30
folderString = "images\\"
imageExtention = ".png"
c = canvas.Canvas("printme.pdf", letter)
# with Image.open("Leystone of Being.png") as being:
cardSize = 0
#parse list.txt
cards = []
quant = []
deckFile = open("list.txt",'r')
deck = deckFile.readlines()
for card in deck:
    if len(card.strip()) > 0:
        if card[0] != '#':
            info = card.strip().split(' ')
            if info[0] == "small":
                cardSize = 1
            elif info[0] == "standard":
                cardSize = 0
            elif info[0] == "format":
                if len(info) < 2:
                    if verbose:
                        print("provide an image extention after 'format'")
                    exit()
                imageExtention = info[1]
            elif info[0] == "verbose":
                verbose = True
            else:
                # add to the card list everything after the quantity and the space
                cards.append(card.strip()[len(info[0] + " "):])
                quant.append(info[0])

if cardSize == 1:
    xOffsetConstant = 2.25 * inch
    yOffsetConstant = 3.25 * inch

else:
    xOffsetConstant = 2.5 * inch
    yOffsetConstant = 3.5 * inch

if verbose:
    print("read deck as:")
    for i, card in enumerate(cards, start = 0):
        print(quant[i] + " x " + card)

cardOnPage = 0
for i, card in enumerate(cards, start = 0):  
    cardImage = Image.open(folderString + card + imageExtention)
    if verbose:
        print("attempting to render: "+folderString +card)
    for x in range(int(quant[i])):
        yOffset = yOffsetConstant * int(cardOnPage/3) + fixedYOffset
        xOffset = xOffsetConstant * (cardOnPage % 3) + fixedXOffset
        c.drawImage(folderString + card + imageExtention, xOffset, yOffset, width=xOffsetConstant, height=yOffsetConstant, mask=None)
        cardOnPage = cardOnPage + 1
        if cardOnPage == 9:
            cardOnPage = 0
            c.showPage()

if cardOnPage != 0:
    c.showPage()

c.save()