# Loo funktsioon, mis trükib sellele argumendina ette antud pealinna nime alusel lause "Üks Euroopa pealinnadest on LINNA_NIMI". Kasutades loodud Euroopa pealinnade järjendit, kutsu seda funktsiooni välja iga pealinna puhul.

# Euroopa üks pealinnadest on Amsterdam.
# Euroopa üks pealinnadest on Bern.
# ...

pealinnad = ["Tallinn", "Riia", "Helsingi", "Stockholm"]

def linna_nimi(pealinn):
    print("Euroopa üks pealinnadest on " + pealinn)

for linn in pealinnad:
    linna_nimi(linn)