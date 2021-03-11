import random
import string

POPULATION = string.ascii_lowercase + string.digits
LENGTH = 5

def randomString(population=POPULATION, length=LENGTH):
    return "".join(random.choices(population=population, k=length))