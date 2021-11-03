# Timothy Lang, Kaleb Getu Gezahegn, Alex McCreight
# Comp - 123
# Lauren Milne
# This file contains a series of functions that allow us to modify the image so that the main code runs more smoothly
# and more predictably.

from imageTools import *
"""
First part contains a series of functions used to change certain parts of the picture slightly to ensure that the main 
code of the game runs smoothly and that countries currently being colored in don't affect neighboring countries.
"""

def makelinethicker(minx, maxx, miny, maxy):
    """
    Takes in two coordinates, and iterates over a box contained created by the two coordinates. This function then
    makes the border thicker where we need it to be to make sure that the colorcountry function doesn't screw up.
    """
    for j in range(miny, maxy):
        for i in range(minx, maxx):
            if newpic.getColor(i, j) > (50, 50, 50) and newpic.getColor(i, j) < (150, 150, 150):
                newpic.setColor(i - 1, j, (100, 100, 100))
    for i in range(minx, maxx):
        for j in range(miny, maxy):
            if newpic.getColor(i, j) > (50, 50, 50) and newpic.getColor(i, j) < (150, 150, 150):
                newpic.setColor(i, j - 1, (100, 100, 100))

def getridofline(minx, maxx, miny, maxy):
    """
    Takes in two coordinates, and iterates over a box contained created by the two coordinates. This function then
    changes any borders in the box to white, effectively deleting them.
    """
    for j in range(miny, maxy + 1):
        for i in range(minx, maxx + 1):
            newpic.setColor(i, j, (255, 255, 255))

def createstraightlinerightward(startX, startY):
    """
    This function takes in two values which put together, create a starting coordinate. The function then iterates over
    the picture, changing all of the pixels to the left and right of the start point (but that are in line with the
    start point) to the border color.
    """
    for i in range(2):
        x = 0
        while newpic.getColor(startX + x, startY) >= (200, 200, 200):
            newpic.setColor(startX + x, startY, (100, 100, 100))
            x += 1
        x = 0
        n = 0
        while newpic.getColor(startX + x - 1, startY) >= (200, 200, 200):
            newpic.setColor(startX + x - 1, startY, (100, 100, 100))
            n += 1
            print(n)
            x -= 1
        startY += 1

"""
The second part takes in an image, and makes all white pixels whiter, and sets all border colors to the same color.
Depending on what value we put for darkcheckcolor, we can change the thickness of the borders to suit our needs.
"""
# newpic = Picture("Asiarescaled.jpg").copy()
newpic = Picture("EuropeMap2rescaled.jpg").copy()
# Special Case for Europe where it has to go before # Europe
# getridofline(0, 52, 641, newpic.getHeight() - 1)
# getridofline(0, 324, 657, newpic.getHeight() - 1)
darkcheckcolor = (175, 175, 175)
# Europe was (175, 175, 175)
# Asia was (175, 175, 175)
# NA was (50, 50, 50)
# Africa was (175, 175, 175)
# SA was (200, 200, 200)
# Australia was (200, 200, 200)

for i in range(newpic.getWidth()):
    for j in range(newpic.getHeight()):
        if i <= 1 or i >= newpic.getWidth() - 2 or j <= 1 or j >= newpic.getHeight() - 2:
            newpic.setColor(i, j, (255, 255, 255))
        elif i == 2 or i == 3 or i == newpic.getWidth() - 3 or i == newpic.getWidth() - 4 or j == 2 or j == 3 or j == newpic.getHeight() - 3 or j == newpic.getHeight() - 4:
            newpic.setColor(i, j, (100, 100, 100))
        elif newpic.getColor(i, j) >= darkcheckcolor:
            newpic.setColor(i, j, (255, 255, 255))
        else:
            newpic.setColor(i, j, (100, 100, 100))


"""
The next part contains all of the countries that we changed slightly.
"""

# # Europe (remember that's there a special case above for Europe
# createstraightlinerightward(838, 288)
# makelinethicker(496, 512, 303, 323) ## For the other border that I totally forgot
# makelinethicker(244, 295, 357, 416) ## For the Netherlands
# getridofline(187, 362, 21, 85)
# newpic.save("EuropeMap.jpg")

# Asia
# makelinethicker(154, 166, 401, 418)
# getridofline(788, 920, 330, 396)

# NorthAmerica
# getridofline(391, 396, 584, 607)

# SouthAmerica
# createstraightlinerightward(358, 90)

# Australia
# getridofline(302, 512, 20, 55)
# getridofline(57, 123, 558, 572)


"""
The last part saves the now updated image to a new filename, shows the image, and continues to show the image until we
type anything into the directory.
"""

# newpic.save("../Pictures_for_game/EuropeMap.jpg")
newpic.show()
input('Press enter to continue...')
