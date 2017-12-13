def Tiime(time):
    hours = time / 3600
    minutes = ((time % 3600) / 60)
    seconds = ((time % 3600) % 60)
    print('%d hour : and %d minute : and %d second' % (hours, minutes, seconds))
while True:
    time = int(input('Please enter the time in seconds : '))
    Tiime(time)
