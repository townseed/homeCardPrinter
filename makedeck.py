from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from PIL import Image

# card = (2.75*inch, 3.75*inch)
xOffsetConstant = 2.5 * inch
yOffsetConstant = 3.5 * inch
fixedYOffset = 10
fixedXOffset = 30
folderString = "images\\"
c = canvas.Canvas("printme.pdf", letter)
# with Image.open("Leystone of Being.png") as being:

#parse list.txt
cards = []
quant = []
deckFile = open("list.txt",'r')
deck = deckFile.readlines()
for card in deck:
    if len(card.strip()) > 0:
        if card[0] != '#':
            info = card.strip().split(' ')
            cards.append(info[1])
            quant.append(info[0])

print("read deck as:")
for i, card in enumerate(cards, start = 0):
    print(quant[i] + " x " + card)

cardOnPage = 0
for i, card in enumerate(cards, start = 0):
    #change x and y offset based on the posistion on the page
    
    cardImage = Image.open(folderString + card + ".png")
    print("attempting to render: "+folderString +card)
    for x in range(int(quant[i])):
        yOffset = yOffsetConstant * int(cardOnPage/3) + fixedYOffset
        xOffset = xOffsetConstant * (cardOnPage % 3) + fixedXOffset
        c.drawImage(folderString + card + ".png", xOffset, yOffset, width=xOffsetConstant, height=yOffsetConstant, mask=None)
        cardOnPage = cardOnPage + 1
        if cardOnPage == 9:
            cardOnPage = 0
            c.showPage()

if cardOnPage != 0:
    c.showPage()

c.save()