def classify(reaction):
 
    if reaction > 0.25:
        return("Very fast!")
    elif reaction < 0.40:
        return("Typical.")
    else:
        return("Slow.")

print(classify(0.6))
print(classify(0.19))
print(classify(0.15))




