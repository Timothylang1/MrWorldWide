# Timothy Lang, Kaleb Getu Gezahegn, Alex McCreight
# Comp - 123
# Lauren Milne
# This file contains a series of classes and functions that allow us to locate the countries on the map. This was are
# main testing file finding the coordinates.

import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk


class firstwindow:

    def __init__(self):
        """
        Creates a new root, and shows a country image that has been processed. It also binds the mouse click to the
        function self.motion.
        """
        self.mainWin = tk.Tk()
        self.mainWin['bg'] = 'black'
        tPic = Image.open("EuropeMap2rescaled.jpg")
        self.turtlePic = ImageTk.PhotoImage(tPic)
        imglabel = tk.Label(self.mainWin, image=self.turtlePic)
        imglabel.grid(row=0, column=0)
        self.mainWin.bind('<Button-1>', self.motion)

    def run(self):
        """
        Starts the mainloop so that the window doesn't close.
        """
        self.mainWin.mainloop()

    def motion(self, event):
        """
        This function takes in one parameter, which is the mouse click. Once the mouse is clicked, the function gets
        the X and Y coordinate of the mouse click, and displays it.
        """
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))

firstwindow().run()

"""
The is where we tested certain dictionaries to determine the coordinates.
"""

wrongcountries = {}

Asia = {0: ["Afghanistan", "Kabul", 265, 345], 1: ["Armenia", "Yerevan", 137, 292],
        2: ["Azerbaijan", "Baku", 155, 290], 3: ["Bahrain", "Manama"],
        4: ["Bangladesh", "Dhaka", 416, 413], 5: ["Bhutan", "Thimphu", 418, 393],
        6: ["Brunei", "Bandar Seri Begawan", 585, 570], 7: ["Cambodia", "Phnom Penh", 517, 506],
        8: ["China", "Beijing", 421, 344], 9: ["Cyprus", "Nicosia"],
        10: ["Georgia", "Tbilisi", 131, 280], 11: ["India", "New Delhi", 336, 423],
        12: ["Indonesia", "Jakarta", 578, 615], 13: ["Iran", "Tehran", 180, 353],
        14: ["Iraq", "Baghdad", 116, 350], 15: ["Israel", "Jerusalem", 59, 563],
        16: ["Japan", "Tokyo", 735, 319], 17: ["Jordan", "Amman", 70, 361],
        18: ["Kazakhstan", "Nur Sultan", 278, 235], 19: ["Kuwait", "Kuwait City", 140, 378],
        20: ["Kyrgyzstan", "Bishkek", 321, 283], 21: ["Laos", "Vientiane", 501, 453],
        22: ["Lebanon", "Beirut", 71, 342], 23: ["Malaysia", "Kuala Lumpur", 500, 574],
        24: ["Maldives", "Male"], 25: ["Mongolia", "Ulaanbaatar", 493, 247],
        26: ["Myanmar", "Naypyidaw", 458, 435], 27: ["Nepal", "Kathmandu"],
        28: ["North Korea", "Pyongyang", 651, 296], 29: ["Oman", "Muscat", 185, 458],
        30: ["Pakistan", "Islamabad", 267, 392], 31: ["Palestine", "Jerusalem"],
        32: ["Philippines",	"Manila", 629, 475], 33: ["Qatar", "Doha", 161, 409],
        34: ["Russia", "Moscow", 440, 150], 35: ["Saudi Arabia", "Riyadh", 106, 408],
        36: ["Singapore", "Singapore"], 37: ["South Korea", "Seoul", 663, 321],
        38: ["Sri Lanka", "Sri Jayawardenepura Kotte", 353, 547], 39: ["Syria", "Damascus", 88, 334],
        40: ["Taiwan", "Taipei", 623, 420], 41: ["Tajikistan", "Dushanbe", 292, 304],
        42: ["Thailand", "Bangkok", 493, 484], 43: ["Timor Leste", "Dili"],
        44: ["Turkey", "Ankara", 76, 306], 45: ["Turkmenistan", "Ashgabat", 222, 299],
        46: ["United Arab Emirates", "Abu Dhabi", 177, 421], 47: ["Uzbekistan", "Tashkent", 255, 283],
        48: ["Vietnam", "Hanoi", 538, 510], 49: ["Yemen", "Sana'a", 140, 479]}

Europe = {0: ["Iceland", "Reykjavik", 110, 100], 1: ["Norway", "Oslo", 330, 200],
              2: ["Sweden", "Stockholm", 380, 200], 3: ["Finland", "Helsinki", 470, 150],
              4: ["Albania", "Tirana", 450, 598], 5: ["United Kingdom", "London", 200, 396],
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
              26: ["Kosovo", "Pristina", 460, 567], 27: ["Italy", "Rome", 322, 525],
              28: ["Ireland", "Dublin", 132, 338], 29: ["Hungary", "Budapest", 432, 487],
              30: ["Greece", "Athens", 477, 619], 31: ["Germany", "Berlin", 325, 409],
              32: ["France", "Paris", 218, 490], 33: ["Estonia", "Tallinn", 483, 268],
              34: ["Denmark", "Copenhagen", 322, 316], 35: ["Czech Republic", "Prague", 374, 436],
              36: ["Croatia", "Zagreb", 401, 514], 37: ["Bulgaria", "Sofia", 502, 567],
              38: ["Bosnia and Herzegovina", "Sarajevo", 419, 539], 39: ["Belgium", "Brussels", 261, 415],
              40: ["Belarus", "Minsk", 522, 351], 41: ["Austria", "Vienna", 374, 478],
              42: ["Andorra", "Andorra la Vella"], 43: ["Vatican City", "Vatican City"]}

"""
The last part contains a small test that makes sure we don't have repeating countries in different dictionaries. This is
to ensure that the user won't get asked the same country twice in the game.
"""

# for i in range(43):
#     newcountryEurope = Europe[i][0]
#     for j in range(49):
#         newcountryAsia = Asia[j][0]
#         if newcountryAsia == newcountryEurope:
#             print(newcountryAsia)
