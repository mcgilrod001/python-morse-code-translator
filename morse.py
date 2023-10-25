import alphebet

plain_text = input("enter you message: ")
decoded_text = []
#turns plain text into list
parse_text = list(plain_text)
print(parse_text)
for i in range(len(parse_text)):
    if parse_text[i] == "a":
        # appends the morse code for a to the list decoded_text
        decoded_text.append(alphebet.a)
        decoded_text.append(" ")
    elif parse_text[i] == "b":
        decoded_text.append(alphebet.b)
        decoded_text.append(" ")
    elif parse_text[i] == "c":
        decoded_text.append(alphebet.c)
        decoded_text.append(" ")
    elif parse_text[i] == "d":
        decoded_text.append(alphebet.d)
        decoded_text.append(" ")
    elif parse_text[i] == "e":
        decoded_text.append(alphebet.e)
        decoded_text.append(" ")
    elif parse_text[i] == "f":
        decoded_text.append(alphebet.f)
        decoded_text.append(" ")
    elif parse_text[i] == "g":
        decoded_text.append(alphebet.g)
        decoded_text.append(" ")
    elif parse_text[i] == "h":
        decoded_text.append(alphebet.h)
        decoded_text.append(" ")
    elif parse_text[i] == "i":
        decoded_text.append(alphebet.i)
        decoded_text.append(" ")
    elif parse_text[i] == "j":
        decoded_text.append(alphebet.j)
        decoded_text.append(" ")
    elif parse_text[i] == "k":
        decoded_text.append(alphebet.k)
        decoded_text.append(" ")
    elif parse_text[i] == "l":
        decoded_text.append(alphebet.l)
        decoded_text.append(" ")
    elif parse_text[i] == "m":
        decoded_text.append(alphebet.m)
        decoded_text.append(" ")
    elif parse_text[i] == "n":
        decoded_text.append(alphebet.n)
        decoded_text.append(" ")
    elif parse_text[i] == "o":
        decoded_text.append(alphebet.o)
        decoded_text.append(" ")
    elif parse_text[i] == "p":
        decoded_text.append(alphebet.p)
        decoded_text.append(" ")
    elif parse_text[i] == "q":
        decoded_text.append(alphebet.q)
        decoded_text.append(" ")
    elif parse_text[i] == "r":
        decoded_text.append(alphebet.r)
        decoded_text.append(" ")
    elif parse_text[i] == "s":
        decoded_text.append(alphebet.s)
        decoded_text.append(" ")
    elif parse_text[i] == "t":
        decoded_text.append(alphebet.t)
        decoded_text.append(" ")
    elif parse_text[i] == "u":
        decoded_text.append(alphebet.u)
        decoded_text.append(" ")
    elif parse_text[i] == "v":
        decoded_text.append(alphebet.v)
        decoded_text.append(" ")
    elif parse_text[i] == "w":
        decoded_text.append(alphebet.w)
        decoded_text.append(" ")
    elif parse_text[i] == "x":
        decoded_text.append(alphebet.x)
        decoded_text.append(" ")
    elif parse_text[i] == "y":
        decoded_text.append(alphebet.y)
        decoded_text.append(" ")
    elif parse_text[i] == "z":
        decoded_text.append(alphebet.z)
        decoded_text.append(" ")
    else:
        decoded_text.append("   ")
decoded_text = "".join(decoded_text)
print(decoded_text)