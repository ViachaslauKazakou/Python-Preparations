def luna(card):
    sum = 0
    for i in range(0, len(card), 2):
        sum += int(card[i]) if int(card[i]) < 10 else int(card[i]) - 9
    pass


# if next((p for p in psutil.process_iter() if p.name() == "ffmpeg"), None):
#     exit("Stop")

i=2
i = 1 if i == 2 else 1
print (i)

if __name__ == "__main__":
    card = str(12334567895846348494)
    luna(card)
