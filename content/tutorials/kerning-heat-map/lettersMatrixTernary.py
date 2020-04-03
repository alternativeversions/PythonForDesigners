### Constants
CELL_SIZE = 30

### Variables
glyphNames = 'ABCDE'
isFirstVertical = True

### Instructions
canvasSize = (len(glyphNames)+2) * CELL_SIZE
newPage(canvasSize, canvasSize)
translate(CELL_SIZE, CELL_SIZE)
for jj, glyphY in enumerate(glyphNames):
    for ii, glyphX in enumerate(glyphNames):
        pair = (glyphY, glyphX) if isFirstVertical else (glyphX, glyphY)

        with savedState():
            translate(ii*CELL_SIZE, jj*CELL_SIZE)
            font('.SFNS-Regular', 18)
            fill(0)
            stroke(None)
            text(f'{pair[0]}{pair[1]}', (0, CELL_SIZE*.3))
