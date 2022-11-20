# Felix´s Weihnachts-Schrank

Felix´s Schrank kann über [den Telegram Bot](https://t.me/FelixsSpassBot) gesteuert werden.

Wenn du eine vorgefertigte Sequenz auf dem Weihnachtsbaum ausführen willst, wähle einen der Befehle aus dem Telegram Bot aus.
Nachrichten die mit / starten, werden als Befehl interpretiert.

Willst du dem Baum deine eigene Sequenz von Licht-Farben schicken, kannst du einfach eine eigene erstellen und diese als Nachricht an den Bot schicken.

Licht-Sequenzen bestehen aus verschachtelten Listen, die wie folgt aufgebaut sind:
- Die RGB Werte der einzelnen Lampen sind als Tuple anzugeben
  - (0, 255, 0)
- Alle RGB Werte der Lampen zu einem Zeitpunkt werden als Liste zusammengefasst 
  - [(0, 255, 0), ..., (255, 0, 0)]
- Da sich die RGB Werte mit der Zeit verändern sollen, müssen diese als Sequenz angegeben werden, z.B. 
  - [[(0, 255, 0), ..., (255, 0, 0)], ..., [(0, 0, 0), ..., (255, 255, 255)]]
    
> :warning: Achtung:
> 
> Pixel Werte dürfen nur zwischen 0 und 255 liegen.
> 
> Die Anzahl der gesetzten Lampen-Tuple muss immer 100 betragen
> 
> Jeder Zeitschritt der Sequenz beträgt 0,5 Sekunden. Und aufgrund eines Problems mit dem Aufteilen von zu langen Nachrichten, können derzeit nur Sequenzen mit zwei Zeitschritten dargestellt werden, alle anderen erzeugen derzeit viele Error messages-

Adresse des Bots:
![Bot QR Code](images/qr_tmp.jpg)
