
introduction = "first out of many!"
centering = introduction.center(80)
print(centering)




cores = 8

class pc:
    gpu = "Gt1030"
    cpu = "i5-3550 4 cores"
    ram = f"{cores}GB ram"

Main_pc = pc()

print(f"  You have like, uh, {pc.ram} running with a {pc.gpu} and finally a {pc.cpu}.\n Yep, that's all.💔")