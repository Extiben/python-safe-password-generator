import random
import string 

longitud = 19

caracteres = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(caracteres) for _ in range (longitud))
print("nueva contraseña segura: ", password)