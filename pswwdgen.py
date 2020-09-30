import random

s = "qwertyuiop[]\';lkjhgfdsazxcvbnm,./`1234567890-=~!@#$%^&*()_+|}{}POZXCVBNMIUYTREWQASDFGHJKL:?><MNBVCXZ`"

psswdlen = 16

psswd = "".join(random.sample(s,psswdlen))

print(psswd)
