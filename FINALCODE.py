# Timothy Lang, Kaleb Getu Gezahegn, Alex McCreight
# Comp - 123
# Lauren Milne
# This file contains all of the code for the actual game itself.

from imageTools2 import *
import random

class firstwindow:

    def __init__(self):
        """
        Initializes several labels, one picture, and two buttons. This is the opening screen of the game.
        """
        self.root = newroot()
        newpic = Picture("Pictures_for_game/mrworldwide.jpg").copy()
        newpic.show()
        testButton = tk.Button(grandmaster[0])
        testButton2 = tk.Button(grandmaster[0])
        testLabel = tk.Label(grandmaster[0], text="Welcome Mr. WorldWide!",
                             font="Arial 40 bold",
                             bg="teal",
                             relief=tk.RIDGE)
        testLabel.grid(row=0, column=0)

        testButton2["text"] = "Start Game"
        testButton2["font"] = "Arial 20"
        testButton2["bg"] = "#189112"
        testButton2["fg"] = "black"
        testButton2.grid(row=1, column=0)
        testButton2["command"] = self.closewindow

        testButton["text"] = "End Game"
        testButton["font"] = "Arial 20"
        testButton["bg"] = "red"
        testButton["fg"] = "black"
        testButton.grid(row=2, column=0)
        testButton["command"] = self.quitCallback

    def run(self):
        """
        Sets NextContinent to False, to make sure that the while part in the function "loop" stops if this window is
        closed in the middle of the game. The function also loops the main window so that the window doesn't close.
        It then assigns the close button on the top level widget to a function called quitcallback().
        """
        NextContinent[0] = False
        grandmaster[0].protocol("WM_DELETE_WINDOW", self.quitCallback)
        self.root.mainloop()

    def quitCallback(self):
        """
        Destroys the main window.
        """
        self.root.destroy()

    def closewindow(self):
        """
        This function will be called when the user clicks the start button. Essentially, this functions purpose is to
        reset all of the global variables back to their original form to reset everything. The game then calls the loop
        function.
        """
        self.root.destroy()
        hiddenscore[0] = 6
        Score[0] = 0
        NextContinent[0] = True
        self.loop()

    def loop(self):
        """
        The loop function creates an accumulator variable first. It will continue to loop until NextContinent turns
        False, which only happens whenever a new window is opened. The only time it is set to True is when the player
        successfully passes to the next level, or if the player starts the game from the first window. Within the while
        loop, the funstion will continue to loop, adding 1 to Continentnumber so that the next continent is called
         until we run out of continents.
        """
        Continentnumber = 0
        while NextContinent[0]:
            if Continentnumber > (len(Continentlist) - 1):
                fourthwindow().run()
                break
            hiddenscore[0] = 0
            secondwindow(Continentnumber).run()
            Continentnumber += 1

class secondwindow:

    def __init__(self, i):
        """
        Creates the main game window, and a lot of variables that will be accessed in later functions. It also creates
        a frame containing several labels, one text box, and a button.
        """
        self.maxmincoorlist = []
        self.whitemin = (200, 200, 200)
        self.bordercolormin = (50, 50, 50)
        self.bordercolormax = (150, 150, 150)
        self.colormax = (50, 50, 50)
        self.color = (0, 0, 0)
        self.coorlist = []
        self.root = newroot()
        self.Currentcontinent = Continentlist[i]
        self.randomnumberlist = []
        self.copypic = Picture(Picturelist[i]).copy()
        self.copypic.show()
        mainframe = tk.Frame(grandmaster[0],
                             bg="lightblue",
                             bd=5,
                             relief=tk.SUNKEN,
                             padx=10,
                             pady=10)
        mainframe.grid(row=0, column=1)
        self.score = tk.Label(mainframe,
                                     text="Score is: " + str(Score[0]),
                                     relief=tk.RIDGE,
                                     font="Arial 14")
        self.score.grid(row=0, column=0, padx=5, pady=5)
        nameofcountrylabel = tk.Label(mainframe,
                                      text="Capital of this country?",
                                      relief=tk.RIDGE)
        nameofcountrylabel.grid(row=1, column=0, padx=5, pady=5)
        self.nameofcountry1 = tk.Label(mainframe,
                                  text="",
                                  relief=tk.RIDGE)
        self.nameofcountry1.grid(row=2, column=0, padx=5, pady=5)
        self.countryentry = tk.Entry(mainframe,
                                relief=tk.RIDGE)
        self.countryentry.grid(row=3, column=0, padx=5, pady=5)
        self.correctlabel = tk.Label(mainframe,
                                text="Press enter to continue",
                                relief=tk.RIDGE)
        self.correctlabel.grid(row=4, column=0, padx=5, pady=5)
        backtomainscreen = tk.Button(mainframe,
                                     text="Back to main window because it's hopeless...",
                                     relief=tk.RIDGE,
                                     command=self.closewindow)
        backtomainscreen.grid(row=5, column=0, padx=5, pady=5)

    def gameend(self):
        """
        Destroys the main window and directs the user to the third window.
        """
        self.root.destroy()
        thirdwindow().run()

    def continuegame(self):
        """
        Changes NextContinent to True so that the loop from firstwindow continues to work, therefore ensuring that the
        next continent is called.
        """
        NextContinent[0] = True
        self.root.destroy()


    def newcountry(self):
        """
        This function does several things. First, it checks hiddenscore. If the user has gotten 1 / 3 of the countries
        correct on the current continent, then it will delay the window for a bit, and then run the function
        continuegame. Second, if the user has gotten through all of the countries, the function runs gameend after a
        set time. If none of this happens, the function prepares the next country. First, it generates a random number.
        Second, it uses that number to get information from the dictionary about that country. Third, it assigns that
        information to different values. It then calls the function to fill in the country. Finally, it adds different
        values to a list, shows the picture, changes the country label, and binds the enter key to the textbox.
        """
        if hiddenscore[0] == len(self.Currentcontinent) // 3:
            self.root.after(1500, self.continuegame)
            return
        if len(self.randomnumberlist) == len(self.Currentcontinent):
            self.root.after(1500, self.gameend)
            return
        while True:
            randomint = random.randint(0, len(self.Currentcontinent) - 1)
            if randomint not in self.randomnumberlist:
                self.randomnumberlist.append(randomint)
                break
        self.country = self.Currentcontinent[randomint]
        # print(self.country[0]) # Test used to see which country glitched
        for i in range(int(len(self.country) / 2) - 1):
            self.smallX = self.country[2 + i * 2]
            self.smallY = self.country[3 + i * 2]
            self.bigX = self.country[2 + i * 2]
            self.bigY = self.country[3 + i * 2]
            self.colorcountry()
            self.maxmincoorlist.append(self.smallX)
            self.maxmincoorlist.append(self.bigX)
            self.maxmincoorlist.append(self.smallY)
            self.maxmincoorlist.append(self.bigY)
        self.copypic.show()
        self.nameofcountry1["text"] = self.country[0]
        self.countryentry.bind("<Return>", self.entryResponse)

    def colorcountry(self):
        """
        This function first sets up the starting location for filling in the country by moving the center coordinate to
        the edge of the map. It then runs a while loop that loops over the country until the [X, Y] coordinate ends back
        where it started. Each time it loops, it first runs deteremineddirection, then drawline, and then checks and
        updates the biggest and smallest X, Y coordinates that will be used later for the changecolor function.
        """
        StartX = self.smallX
        StartY = self.smallY
        X = StartX
        while self.copypic.getColor(X, StartY - 1) >= self.whitemin:
            StartY -= 1
        Y = StartY
        EndY = StartY
        while self.copypic.getColor(X, StartY) >= self.whitemin:
            self.copypic.setColor(X, StartY, self.color)
            StartY += 1
        self.coorlist = [X, Y]
        self.direction = "downward"
        self.determinedirection()
        self.drawline()
        # for i in range(0): # Used to test if we got the starting point within the function. By changing the number
                             # inside, we could also visually see if the countries borders were solid enough to contain
                             # the draw function to only operate within the border of the country.
        while self.coorlist != [StartX, EndY]:
            self.determinedirection()
            self.drawline()
            if self.coorlist[0] < self.smallX:
                self.smallX = self.coorlist[0]
            if self.coorlist[1] < self.smallY:
                self.smallY = self.coorlist[1]
            if self.coorlist[0] > self.bigX:
                self.bigX = self.coorlist[0]
            if self.coorlist[1] > self.bigY:
                self.bigY = self.coorlist[1]

    def determinedirection(self):
        """
        This function uses a complicated series of algorithms to determine which way the drawline function should draw.
        Essentially, there are eight scenarios, and this function address all of them. I don't care if I lose points,
        I'm not explaining how this works because it would take forever to explain why it works and how I made it. This
        was the single, most hard part. It was what I spent the majority of my time on. All you need to know is it
        determines the direction. The function's second purpose is to set up the starting X and Y values for the
        drawline function. Moving on...
        """
        X = self.coorlist[0]
        Y = self.coorlist[1]
        if self.direction == "downward":
            X += 1
            if self.copypic.getColor(X, Y) >= self.whitemin or self.copypic.getColor(X, Y) <= self.colormax:
                while True:
                    Y -= 1
                    if self.copypic.getColor(X, Y) > self.bordercolormin and self.copypic.getColor(X, Y) < self.bordercolormax:
                        self.coorlist = [X, Y + 1]
                        return
                    if self.copypic.getColor(X - 1, Y) >= self.whitemin or self.copypic.getColor(X - 1, Y) <= self.colormax:
                        self.direction = "upward"
                        self.coorlist = [X - 1, Y]
                        return
            else:
                savedY = Y
                while True:
                    Y += 1
                    if self.copypic.getColor(X, Y) >= self.whitemin or self.copypic.getColor(X, Y) <= self.colormax:
                        if self.copypic.getColor(X - 1, Y) > self.colormax or self.copypic.getColor(X - 1, Y) == (0, 255, 0):
                            X -= 1
                            Y = savedY
                            self.direction = "upward"
                            while self.copypic.getColor(X, Y + 1) <= self.colormax:
                                Y += 1
                            self.coorlist = [X, Y]
                            return
                        else:
                            self.coorlist = [X, Y]
                            return
        if self.direction == "upward":
            X -= 1
            if self.copypic.getColor(X, Y) <= self.colormax or self.copypic.getColor(X, Y) >= self.whitemin:
                while True:
                    Y += 1
                    if self.copypic.getColor(X, Y) > self.bordercolormin and self.copypic.getColor(X, Y) < self.bordercolormax:
                        self.coorlist = [X, Y - 1]
                        return
                    if self.copypic.getColor(X + 1, Y) >= self.whitemin or self.copypic.getColor(X + 1, Y) <= self.colormax:
                        self.direction = "downward"
                        self.coorlist = [X + 1, Y]
                        return
            else:
                savedY = Y
                while True:
                    Y -= 1
                    if self.copypic.getColor(X, Y) <= self.colormax or self.copypic.getColor(X, Y) >= self.whitemin:
                        if self.copypic.getColor(X + 1, Y) > self.colormax or self.copypic.getColor(X + 1, Y) == (0, 255, 0):
                            self.direction = "downward"
                            X += 1
                            Y = savedY
                            while self.copypic.getColor(X, Y - 1) <= self.colormax:
                                Y -= 1
                            self.coorlist = [X, Y]
                            return
                        else:
                            self.coorlist = [X, Y]
                            return

    def drawline(self):
        """
        Based on which direction determineddirection decided, this function draws a line in that direction until it hits
        another black line or the border color.
        """
        X = self.coorlist[0]
        Y = self.coorlist[1]
        if self.direction == "downward":
            while self.copypic.getColor(X, Y) >= self.whitemin:
                self.copypic.setColor(X, Y, self.color)
                Y += 1
        if self.direction == "upward":
            while self.copypic.getColor(X, Y) >= self.whitemin:
                self.copypic.setColor(X, Y, self.color)
                Y -= 1

    def changecolor(self, color):
        """
        This function takes in one parameter, a tuple that will determine the "fill in color" of the country. Based on
        the list of biggest X and Y values, updated from the colorcountry function, it then iterates over those pixels.
        It changes every black pixel it sees to the color value, which will be red if the user is wrong, and green if
        the user is correct. Each time, it also removes the X and Y values from the list so that if a country has
        multiple islands, it can change all of the island colors.
        """
        while len(self.maxmincoorlist) != 0:
            bigY = self.maxmincoorlist.pop()
            smallY = self.maxmincoorlist.pop()
            bigX = self.maxmincoorlist.pop()
            smallX = self.maxmincoorlist.pop()
            for i in range(smallX - 1, bigX + 2):
                for j in range(smallY - 1, bigY + 2):
                    if self.copypic.getColor(i, j) <= self.colormax and self.copypic.getColor(i, j) != (0, 255, 0):
                        self.copypic.setColor(i, j, color)

    def entryResponse(self, event):
        """
        This function occurs when the user clicks enter after they type in what they think the capital name is. This
        function first unbinds the enter key to make sure that if the user clicks enter to fast, the program doesn't
        glitch and cause an error. It then checks if the user got the correct answer or wrong answer and changes the
        color of the country, and the correctlabel accordingly. It then updates the map to display the now colored in
        country. Finally, tt then deletes the entry, and repeats the newcountry function for the next country.
        """
        self.countryentry.unbind("<Return>")
        txt = self.countryentry.get()
        if txt == self.country[1]:
            self.correctlabel["text"] = "Correct!"
            Score[0] += 1
            self.score["text"] = "Score is: " + str(Score[0])
            hiddenscore[0] += 1
            self.changecolor((0, 255, 0))
        else:
            self.correctlabel["text"] = "Idiot... capital of " + self.country[0] + " is " + self.country[1]
            self.changecolor((255, 0, 0))
        self.copypic.show()
        self.countryentry.delete(0, tk.END)
        self.newcountry()

    def closewindow(self):
        """
        This function occurs when the user wants to return back to the main screen. First, it destroys the main window.
        Second, it runs the first window which is the opening screen.
        """
        self.root.destroy()
        firstwindow().run()

    def run(self):
        """
        Sets NextContinent to False, to make sure that the while part in the function "loop" stops if this window is
        closed in the middle of the game. The function then starts the new country function to initialize the questions
        and the game. The function also loops the main window so that the window doesn't close. It then assigns the
        close button on the top level widget to a function called quitcallback().
        """
        NextContinent[0] = False
        grandmaster[0].protocol("WM_DELETE_WINDOW", self.quitCallback)
        self.newcountry()
        self.root.mainloop()

    def quitCallback(self):
        """
        Destroys the main root.
        """
        self.root.destroy()

class thirdwindow:

    def __init__(self):
        """
        Creates a new window, several labels displaying information, and a two buttons which close the window or exits
        back to the main window, depending on which one you click. The third window will pop up when a player fails to
        pass to the next continent.
        """
        self.mainwindow = tk.Tk()
        self.mainwindow.title("Mr. Worldwide")
        self.mainwindow['bg'] = 'black'
        backtomainscreen = tk.Button(self.mainwindow,
                                     text="Try again",
                                     font="Arial 20",
                                     relief=tk.RIDGE,
                                     bg = "green",
                                     command=self.closewindow)
        backtomainscreen.grid(row=4, column=3)
        backtomainscreen = tk.Button(self.mainwindow,
                                     text="Exit game",
                                     font="Arial 20",
                                     relief=tk.RIDGE,
                                     bg="red",
                                     command=self.exitgame)
        backtomainscreen.grid(row=3, column=3)
        scorelabel = tk.Label(self.mainwindow,
                              bg="yellow",
                              font="Arial 15",
                              text=("Score:", Score[0]))
        scorelabel.grid(row=0, column=2, pady=5)
        ruleslabel = tk.Label(self.mainwindow,
                              text="You Suck",
                              font="Arial 40 bold",
                              bg="Red")
        ruleslabel.grid(row=1, column=3)
        rulespasslabel = tk.Label(self.mainwindow,
                              text="Need 1/3 of the capitals correct to pass",
                              font="Arial 40 bold",
                              bg="Red")
        rulespasslabel.grid(row=2, column=3)

    def closewindow(self):
        """
        This function occurs when the user clicks the "Try Again" button. First, it destroys the third window, and then
        runs the first window which is the opening window.
        """
        self.mainwindow.destroy()
        firstwindow().run()

    def exitgame(self):
        """
        This function occurs when the user clicks the exit button. It's only purpose is to destroy the game.
        """
        self.mainwindow.destroy()

    def run(self):
        """
        Sets NextContinent to False, to make sure that the while part in the function "loop" stops if this window is
        closed in the middle of the game. The function also loops the main window so that the window doesn't close.
        """
        NextContinent[0] = False
        self.mainwindow.mainloop()

class fourthwindow:

    def __init__(self):
        """
        Does the same exact thing as the third window, but with different text in the labels and different colors.
        """
        self.mainwindow = tk.Tk()
        self.mainwindow.title("Mr. Worldwide")
        self.mainwindow['bg'] = 'beige'
        backtomainscreen = tk.Button(self.mainwindow,
                                     text="Play again",
                                     font="Arial 20",
                                     relief=tk.RIDGE,
                                     bg="green",
                                     command=self.closewindow)
        backtomainscreen.grid(row=2, column=3)
        backtomainscreen = tk.Button(self.mainwindow,
                                     text="Exit game",
                                     font="Arial 20",
                                     relief=tk.RIDGE,
                                     bg="red",
                                     command=self.exitgame)
        backtomainscreen.grid(row=3, column=3)
        scorelabel = tk.Label(self.mainwindow,
                              bg="yellow",
                              text=("Score:", Score[0]),
                              font="Arial 15")
        scorelabel.grid(row=0, column=2, pady=5)
        ruleslabel = tk.Label(self.mainwindow,
                              text="Congrats! You won the game!",
                              font="Arial 40 bold",
                              bg="Teal")
        ruleslabel.grid(row=1, column=3)

    def closewindow(self):
        """
        This function occurs when the user clicks the "Try Again" button. First, it destroys the third window, and then
        runs the first window which is the opening window.
        """
        self.mainwindow.destroy()
        firstwindow().run()

    def exitgame(self):
        """
        Destroys the main root.
        """
        self.mainwindow.destroy()

    def run(self):
        """
        Sets NextContinent to False, to make sure that the while part in the function "loop" stops if this window is
        closed in the middle of the game. The function also loops the main window so that the window doesn't close.
        """
        NextContinent[0] = False
        self.mainwindow.mainloop()

if __name__ == "__main__":

    """
    This function runs only when it's the primary function. We create a bunch of global variables, and then fun the 
    first window. Each global variable has a unique purpose that needs to be accessible to all of the classes, such as
    the dictionaries for the countries.
    """

    Europe = {0: ["Iceland", "Reykjavik", 110, 100], 1: ["Norway", "Oslo", 330, 200],
              2: ["Sweden", "Stockholm", 380, 200], 3: ["Finland", "Helsinki", 470, 150],
              4: ["Albania", "Tirana", 450, 598], 5: ["United Kingdom", "London", 200, 396, 153, 317],
              6: ["Ukraine", "Kiev", 564, 415], 7: ["Switzerland", "Bern", 294, 486],
              8: ["Spain", "Madrid", 119, 583], 9: ["Slovenia", "Ljubljana", 374, 507],
              10: ["Slovakia", "Bratislava", 424, 458], 11: ["Serbia", "Belgrade", 458, 540],
              12: ["San Marino", "San Marino"], 13: ["Romania", "Bucharest", 505, 498],
              14: ["Portugal", "Lisbon", 49, 560], 15: ["Macedonia", "Skopje", 473, 584],
              16: ["Poland", "Warsaw", 428, 393], 17: ["Netherlands", "Amsterdam", 268, 392],
              18: ["Montenegro", "Podgorica", 437, 564], 19: ["Monaco", "Monaco"],
              20: ["Moldova", "Chisinau", 547, 470], 21: ["Malta", "Valletta"],
              22: ["Luxembourg", "Luxembourg", 274, 431], 23: ["Lithuania", "Vilnius", 470, 328],
              24: ["Liechtenstein", "Vaduz"], 25: ["Latvia", "Riga", 485, 296],
              26: ["Kosovo", "Pristina", 460, 567], 27: ["Italy", "Rome", 322, 525, 369, 662, 294, 612],
              28: ["Ireland", "Dublin", 132, 338], 29: ["Hungary", "Budapest", 432, 487],
              30: ["Greece", "Athens", 477, 619], 31: ["Germany", "Berlin", 325, 409],
              32: ["France", "Paris", 218, 490, 296, 577], 33: ["Estonia", "Tallinn", 483, 268],
              34: ["Denmark", "Copenhagen", 329, 335, 322, 316, 341, 330], 35: ["Czech Republic", "Prague", 374, 436],
              36: ["Croatia", "Zagreb", 401, 514], 37: ["Bulgaria", "Sofia", 502, 567],
              38: ["Bosnia and Herzegovina", "Sarajevo", 419, 539], 39: ["Belgium", "Brussels", 261, 415],
              40: ["Belarus", "Minsk", 522, 351], 41: ["Austria", "Vienna", 374, 478],
              42: ["Andorra", "Andorra la Vella"], 43: ["Vatican City", "Vatican City"]}

    Asia = {0: ["Afghanistan", "Kabul", 265, 345], 1: ["Armenia", "Yerevan", 137, 292],
            2: ["Azerbaijan", "Baku", 155, 290], 3: ["Bahrain", "Manama"],
            4: ["Bangladesh", "Dhaka", 416, 413], 5: ["Bhutan", "Thimphu", 418, 393],
            6: ["Brunei", "Bandar Seri Begawan", 581, 569], 7: ["Cambodia", "Phnom Penh", 517, 506],
            8: ["China", "Beijing", 421, 344, 550, 456], 9: ["Cyprus", "Nicosia"],
            10: ["Georgia", "Tbilisi", 131, 280], 11: ["India", "New Delhi", 336, 423],
            12: ["Indonesia", "Jakarta", 504, 619, 585, 607, 628, 618, 667, 631, 748, 633, 675, 597, 685, 628, 666, 630, 602, 672, 535, 658], 13: ["Iran", "Tehran", 180, 353],
            14: ["Iraq", "Baghdad", 116, 350], 15: ["Israel", "Jerusalem", 57, 366],
            16: ["Japan", "Tokyo", 745, 269, 731, 322, 686, 352, 700, 344, 730, 275], 17: ["Jordan", "Amman", 70, 361],
            18: ["Kazakhstan", "Nur Sultan", 278, 235], 19: ["Kuwait", "Kuwait City", 140, 378],
            20: ["Kyrgyzstan", "Bishkek", 321, 283], 21: ["Laos", "Vientiane", 501, 453],
            22: ["Lebanon", "Beirut", 71, 342], 23: ["Malaysia", "Kuala Lumpur", 502, 574, 580, 586],
            24: ["Maldives", "Male"], 25: ["Mongolia", "Ulaanbaatar", 493, 247],
            26: ["Myanmar", "Naypyidaw", 458, 435], 27: ["Nepal", "Kathmandu", 368, 381],
            28: ["North Korea", "Pyongyang", 651, 296], 29: ["Oman", "Muscat", 185, 458],
            30: ["Pakistan", "Islamabad", 267, 392], 31: ["Palestine", "Jerusalem"],
            32: ["Philippines", "Manila", 629, 475, 628, 504, 636, 515, 641, 523, 650, 541, 654, 509, 643, 500], 33: ["Qatar", "Doha", 157, 407],
            34: ["Russia", "Moscow", 440, 150, 739, 218], 35: ["Saudi Arabia", "Riyadh", 106, 408],
            36: ["Singapore", "Singapore"], 37: ["South Korea", "Seoul", 663, 321],
            38: ["Sri Lanka", "Sri Jayawardenepura Kotte", 353, 547], 39: ["Syria", "Damascus", 88, 334],
            40: ["Taiwan", "Taipei", 623, 420], 41: ["Tajikistan", "Dushanbe", 292, 304],
            42: ["Thailand", "Bangkok", 493, 484], 43: ["Timor Leste", "Dili"],
            44: ["Turkey", "Ankara", 76, 306], 45: ["Turkmenistan", "Ashgabat", 222, 299],
            46: ["United Arab Emirates", "Abu Dhabi", 177, 421], 47: ["Uzbekistan", "Tashkent", 255, 283],
            48: ["Vietnam", "Hanoi", 538, 510], 49: ["Yemen", "Sanaa", 140, 479]}

    NorthAmerica = {0: ["United States", "Washington D.C.", 398, 400, 222, 171], 1: ["Canada", "Ottawa", 398, 300],
                    2: ["Mexico", "Mexico City", 360, 575], 3: ["Belize", "Belmopan", 453, 592],
                    4: ["Guatemala", "Guatemala City", 440, 615], 5: ["Honduras", "Tegucigalpa", 470, 610],
                    6: ["El Salvador", "San Salvador", 458, 619], 7: ["Nicaragua", "Managua", 480, 619],
                    8: ["Costa Rica", "San Jose", 490, 638], 9: ["Panama", "Panama City", 525, 649],
                    10: ["Cuba", "Havana", 535, 545], 11: ["Dominican Republic", "Santo Domingo", 585, 547],
                    12: ["Haiti", "Port-au-Prince", 572, 549], 13: ["Jamaica", "Kingston", 537, 568]}

    SouthAmerica = {0: ["Argentina", "Buenos Aires", 240, 400], 1: ["Bolivia", "La Paz", 250, 300],
                    2: ["Brazil", "Brasilia", 335, 150], 3: ["Chile", "Santiago", 230, 600, 212, 375],
                    4: ["Colombia", "Bogota", 181, 100], 5: ["Ecuador", "Quito", 100, 160],
                    6: ["Guyana", "Georgetown", 280, 70], 7: ["Paraguay", "Asuncion", 340, 375],
                    8: ["Peru", "Lima", 100, 190], 9: ["Suriname", "Paramaribo", 318, 82],
                    10: ["Uruguay", "Montevideo", 340, 450], 11: ["Venezuela", "Caracas", 181, 50],
                    12: ["French Guiana", "Cayenne", 352, 82]}

    Australia = {0: ["Australia", "Canberra", 177, 444], 1: ["New Zealand", "Wellington", 472, 597, 505, 550],
                 2: ["Papua New Guinea", "Port Moresby", 260, 270]}

    Africa = {0: ["Morroco", "Rabat", 152, 75], 1: ["Ethiopia", "Addis Ababa", 515, 287],
              2: ["Algeria", "Algeirs", 199, 136], 3: ["Angola", "Luanda", 325, 481],
              4: ["Togo", "Lome", 166, 292], 5: ["Egypt", "Cairo", 421, 140],
              6: ["Libya", "Tripoli", 352, 104], 7: ["Eritrea", "Asmara", 498, 225],
              8: ["Djbouti", "Djbouti", 533, 255], 9: ["Somalia", "Mogadishu", 591, 296],
              10: ["Sudan", "Khartoum", 423, 213], 11: ["Tunisia", "Tunis", 256, 41],
              12: ["Kenya", "Nairobi", 489, 349], 13: ["Uganda", "Kampala", 454, 353],
              14: ["Tanzania", "Dar es Salaam", 465, 442], 15: ["Rwanda", "Kigali", 429, 383],
              16: ["Burundi", "Bujumbura", 425, 403], 17: ["Nigeria", "Abuja", 225, 279],
              18: ["Ghana", "Accra", 146, 307], 19: ["Senegal", "Dakar", 49, 226],
              20: ["Eswatini", "Mbabane", 427, 613], 21: ["Niger", "Niamey", 244, 216],
              22: ["Mali", "Bamako", 162, 203], 23: ["South Africa", "Pretoria", 386, 609],
              24: ["Seychelles", "Victoria"], 25: ["Benin", "Porto Novo", 184, 271],
              26: ["Botswana", "Gaborone", 378, 572], 27: ["Cameroon", "Yaounde", 271, 317],
              28: ["Cape Verde", "Praia", ], 29: ["Central African Republic", "Bangui", 359, 299],
              30: ["Chad", "NDjamena", 326, 222], 31: ["Congo", "Brazaville", 306, 371],
              32: ["Ivory Coast", "Abidjan", 114, 295], 33: ["Equatorial Guinea", "Malabo", 252, 349],
              34: ["Gabon", "Libreville", 265, 375], 35: ["Gambia", "Banjul", 28, 239],
              36: ["Guinea", "Conakry", 44, 263], 37: ["Guinea Bissau", "Bissau", 32, 253],
              38: ["Lesotho", "Maseru", 398, 640], 39: ["Liberia", "Monrovia", 79, 301],
              40: ["Madagascar", "Antananarivo", 562, 545], 41: ["Malawi", "Lilongwe", 454, 482],
              42: ["Mauritania", "Nouakchott", 82, 183], 43: ["Mozambique", "Maputo", 490, 491],
              44: ["Namibia", "Windhoek", 313, 551], 45: ["Sao Tome and Principe", "Sao Tome"],
              46: ["Sierra Leone", "Freetown", 58, 285], 47: ["Democratic Republic of Congo", "Kinshasa", 367, 396],
              48: ["Zambia", "Lusaka", 400, 497], 49: ["Zimbabwe", "Harare", 413, 543],
              50: ["Burkina Faso", "Ouagadougou", 159, 242]}

    Continentlist = [Australia, SouthAmerica, NorthAmerica, Europe, Asia, Africa]

    Picturelist = ["Pictures_for_game/AustraliaMap.jpg", "Pictures_for_game/SouthAmericaMap.jpg",
                   "Pictures_for_game/NorthAmericaMap.jpg", "Pictures_for_game/EuropeMap.jpg",
                   "Pictures_for_game/AsiaMap.jpg", "Pictures_for_game/AfricaMap.jpg"]

    NextContinent = [True]

    Score = [0]

    hiddenscore = [0]

    firstwindow().run()


# Hiddengem: If you're playing the game, I strongly recommend listening to "The Other Side of Paradise" while playing.
# It's by the Glass Animals, and it's the coolest song ever, I promise ;)

