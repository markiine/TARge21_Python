onRatas = True
kasSajab = True
temp = int(input("Tänane temperatuur (täisarvuna): "))
if onRatas and (not kasSajab or (25 > temp > 15)):
    print("Täna saab trenni teha!")
else:
    print("Täna ei saa trenni teha!")
