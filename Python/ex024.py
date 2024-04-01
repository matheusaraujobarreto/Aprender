c = str(input("Diga sua cidade")).strip().upper()
print(c[:5] == "SANTO")
if c[:5] == "SANTO": #apenas brincadeira
    print("\033[36m{}\033[m é santa mesmo".format(c.title()))
else:
    print("\033[31;43mSua cidade não é santa\033[m")
