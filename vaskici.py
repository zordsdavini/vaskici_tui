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
ženklai = ['l', 's', 'z']

while True:
    ėjimas = ėjimas + 1
    print("\n%i ----------------------" % ėjimas)
    print("Pergalės %i\nPralaimėjimai %i" % (pergalės, pralaimėjimai))
    spėjimas = input("Įvesk spėjimą (l, s, z): ")
    if spėjimas not in ženklai:
        print("Žaidimas baigtas\n")
        break

    kompiuteris = ženklai[randrange(3)]
    print("Kompiuteris rodo: %s" % kompiuteris)

    if spėjimas == 'l':
        if kompiuteris == 'l':
            print("Lygiosios :-S")
            continue

        if kompiuteris == 's':
            print("Laimėjai :-)")
            pergalės = pergalės + 1
            continue

        print("Pralaimėjai :-(")
        pralaimėjimai = pralaimėjimai + 1
        continue


    if spėjimas == 's':
        if kompiuteris == 's':
            print("Lygiosios :-S")
            continue

        if kompiuteris == 'z':
            print("Laimėjai :-)")
            pergalės = pergalės + 1
            continue

        print("Pralaimėjai :-(")
        pralaimėjimai = pralaimėjimai + 1
        continue


    if kompiuteris == 'z':
        print("Lygiosios :-S")
        continue

    if kompiuteris == 'l':
        print("Laimėjai :-)")
        pergalės = pergalės + 1
        continue

    print("Pralaimėjai :-(")
    pralaimėjimai = pralaimėjimai + 1
    continue
