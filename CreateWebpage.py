#Jason Gupta, Vicki Shaw
#jgupta7@gatech.edu, vshaw3@gatech.edu
#We worked on this homework assignment alone, using only this semester's course materials and resources.

from Myro import *
init("sim")
roboname = getName()

def makeWebPage(numberOfPictures):
    index = 0
    finallist = []
    piclist = []
    while index < numberOfPictures:

        pic = takePicture()
        istring = str(index)
        filename = "pic" + istring + ".jpg"
        piclist.append(filename)
        savePicture(pic, filename)
        lightlist = getLight()
        averagelight = sum(lightlist) / 3
        finallist.append(averagelight)
        turnLeft(.5, .25)
        index = index + 1
    myFile = open("myPage.html", "w")
    top = """<!DOCTYPE html system>
    <html>
    <head>
        <title> Pictures from a Robot! </title>
    </head>
    <body>
    <h1> Welcome to our Picture Page! </h1>"""

    myFile.write(top)
    middle = """<p> Made by Jason Gupta and Vicki Shaw </p>
    """
    myFile.write("Pictures taken by {}".format(roboname))
    myFile.write(middle)

    x = 0
    myFile.write("<table>")
    myFile.write("<tr>")
    while x < numberOfPictures:

        lightaverage = "{}".format(finallist[x])
        if x % 4 == 0 and x != 0:
            myFile.write("</tr>")
            myFile.write("<tr>")
        myFile.write("<td>")
        myFile.write('<img src="{}" alt="pic">'.format(piclist[x]))

        myFile.write("<br>{}".format(lightaverage))
        myFile.write("</td>")


        x = x + 1
    myFile.write("</tr>")
    myFile.write("</table>")

    myFile.write("</body></html>")
    myFile.close()
