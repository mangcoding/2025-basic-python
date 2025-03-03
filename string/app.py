hello_template = "Hello, nama saya %s, Saya dar %s"
print(hello_template % ("Budi","Bandung"))

template_2 = "Hello, nama saya {name}, Saya dari {address}"
print(template_2.format(address="Jakarta",name="Deni"))