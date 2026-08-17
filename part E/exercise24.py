# extract hashtags
post = "Loving #Python and #Coding at #HordansoAcademy"

words = post.split()

hashtags = [word for word in words if word.startswith("#")]

print("Hashtags:", hashtags)