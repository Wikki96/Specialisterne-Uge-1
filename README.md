Opgave 1:
Kør navnesorteing.py. Den tager Navne_liste.txt og skriver den sorteret i sorted_list.txt og bogstavsfrekvenserne i letter_frequency.txt.
Jeg ville have fortsat ved at lave de ekstra opgaver.

Opgave 2:
Kør logfile_analysis.py. Den uplukker warnings og errors fra app_log.txt og putter dem i hhv. warnings.txt og errors.txt.
Jeg ville have fortsat opgaven ved at implementere en måde at specificere hvilke logs du ville sortere fra.

Opgave 3:
Kør data_cleanup.py og specificér i konsollen hvilke stier der skal bruges til source og destination. 
Jeg var i tvivl om hvor data-specifikt jeg skulle lave programmet. Som det er nu virker det kun til data i samme format med de samme kolonner som i source_data.csv.
Er der en måde at skrive koden på, når man har mange filer åbne, så man ikke er dybt nede i enten nogle with eller try/except statements?

Opgave 4:
Kør pandasBasics.py.
Det var svært at finde ud af at få plot til at virke ordentligt når der var multiindeks i den serie man får ud efter at have grupperet efter to ting

Northwind Foods:
ER-diagram.pdf indeholder ER diagrammet. uge3_opgave4.sql indeholder sql commandoerne fra del 2. For del 3 kør northwind_analysis.py og input dine credentials til MySQL i konsollen. 
Jeg bøvlede lidt med at få SQLite3 til at virke - hvilket tilsyneladende ikke kan lade sig gøre. Jeg valgte så MySQL-connector, men det er ikke understøttet af pandas. Pandas foreslår selv SQAlchemy - jeg nåede ikke at se på om det virkede med MySQL.
