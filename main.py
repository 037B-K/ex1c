# Exercice 1c, faire les * avec while loop
i = 0

#Repeter 11 fois
while i < 11:
    etoile = "*"
    print(etoile * (11 - i))
    # ^ ceci dit au programme de print * 11 fois MOINS le nombre de loop deja faites
    i += 1
    # Ceci dit au programme q'il a fait la loop une foit de plus


