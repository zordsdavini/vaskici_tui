# Vaskiči žaidimas | Game Vaskiči to teach my son basics of programing in Lithuanian

# Copyright (c) 2015 zordsdavini@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
# is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
# IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from random import randrange

class vaskici:
    ženklai = ['l', 's', 'z']

    def run(self):
        print("""
        VASKIČI ŽAIDIMAS
        ================

        Taisyklės:
        Įvesk ženklo raidę:
            l - lapas
            s - šulinys
            z - žirklės

        Gero žaidimo :-)
        """)

        ėjimas = 0
        pergalės = 0
        pralaimėjimai = 0

        while True:
            ėjimas = ėjimas + 1
            print("\n%i ----------------------" % ėjimas)
            print("Pergalės %i\nPralaimėjimai %i" % (pergalės, pralaimėjimai))
            spėjimas = input("Įvesk spėjimą (l, s, z): ")
            if spėjimas not in self.ženklai:
                print("Žaidimas baigtas\n")
                break

            # spėjimų logika sukelta po atskiru metodu
            (kompiuteris, rezultatas) = self.ai(spėjimas)

            print("Kompiuteris rodo: %s" % kompiuteris)

            if rezultatas > 0:
                print("Laimėjai :-)")
                pergalės = pergalės + 1
            elif rezultatas < 0:
                print("Pralaimėjai :-(")
                pralaimėjimai = pralaimėjimai + 1
            else:
                print("Lygiosios :-S")

            continue


    def ai(self, spėjimas):
        kompiuteris = self.ženklai[randrange(3)]

        if spėjimas == 'l':
            if kompiuteris == 'l':
                return (kompiuteris, 0)

            if kompiuteris == 's':
                return (kompiuteris, 1)

            return (kompiuteris, -1)

        if spėjimas == 's':
            if kompiuteris == 's':
                return (kompiuteris, 0)

            if kompiuteris == 'z':
                return (kompiuteris, 1)

            return (kompiuteris, -1)

        if kompiuteris == 'z':
            return (kompiuteris, 0)

        if kompiuteris == 'l':
            return (kompiuteris, 1)

        return (kompiuteris, -1)



app = vaskici()
app.run()
