import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Store the name of the file we're working with in filename.
filename = "C:/Users/rikfah/PycharmProjects/Learning_Python/death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)  # För att skapa ett läsbart objekt av filen
    header_row = next(reader)  # csv-modulen har en next-funktion som ger nästa rad (dvs. första raden)

    for index, column_header in enumerate(header_row):  # Använder enumerate för att ge varje datapunkt ett index
        print(index, column_header)

    # Get dates high and low temperatures from file.
    # Loopen kommer för varje rad att 1) försöka göra om datum till rätt format samt formatera high/low-värden till int.
    # Om något av detta inte går (ex. pga. ej fullständig data kommer Python generera en ValueError-meddelande,
    # Då printas det datumet samt texten "missing data".
    # Annars så appendas resp. värde till rätt lista.

    dates, highs, lows = [], [], []
    for row in reader:  # for-loopen behöver vara inom with-loopen annars är csv-filen "stängd".
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")  # Första kolumnen i csv-filen innehåller info om datum, gör här om textinputen till specifikt datumformat.
            high = int(row[1])  # Behöver göra om till int om matplotlib ska kunna läsa, om inte sparas det som str.
            low = int(row[3])

        except ValueError:
            print(current_date, 'missing data')

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)  # Skickar in listan med högstatemp. och dates, samt definierar färgen till röd.
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
