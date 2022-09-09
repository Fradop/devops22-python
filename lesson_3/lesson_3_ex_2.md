Övningar i datastrukturer
Uppgift A
Skapa ett nytt python-dokument i din utvecklingsmiljö, glöm inte ändelsen .py. Skriv av
nedanstående program och laborera fram svaret på frågorna nedan. Det är alltså fritt fram
att lägga till nya rader i programmet. Var noga när du skriver av så att till exempel ett ”{“ inte
byts ut mot ett “[“. Det är viktigt att du förstår vad som händer och varför. Tips: Kommandot
type(X) returnerar X:s datatyp.
X = 1
Y = 4
addresses = {"Adam": "Ormvägen 5",
"Bella": "Klockgatan 1",
"Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}
Frågor:
1. Vilken datatyp har variablerna X och Y?
2. Vilken datatyp har variabeln addresses?
3. Hur kan man få ut bellas adress ur variabeln addresses?
4. Vad händer om man skriver addresses[“Daniel”] = “Prinsgränd 2”?
5. Få ditt program att skriva ut hur många keys addresses har.
5.1. Utöka programmet så att adressen skrivs ut till den personen som
kommer sist i bokstavsordning.
5.2. Utöka programmet så att namnet skrivs ut på den personen som bor
på adressen som kommer först i bokstavsordning. Tips: följande rad
byter plats på keys och values i my_dict:
my_dict = {v: k for k, v in my_dict.items()}
Förklaring kommer nästa lektion!
6. Vilken datatyp har variabeln cars?
7. Vad returneras om man skriver cars[X]?
8. Vad returneras om man skriver cars[Y], varför?
9. Vad returneras om man först skriver cars.sort() och på nästa rad skriver
cars[0]?
10. Skapa en ny variabel genom att skriva cars_2 = cars, och på följande rad ska
strängen “Saab” läggas till cars med hjälp av append(). Notera att det alltså
bara är ena variabeln som ska utökas. Vad innehåller variablerna cars_2 och
cars nu? Förklara!
10.1. Skapa ytterligare en variabel cars_3 som får sina element av cars
men som inte påverkas av vad som läggs till i cars.
10.2. Utöka variabeln cars så att den innehåller dubbletter av varje bilmärke
sorterat i omvänd bokstavsordning.
10.3. Från den utökade versionen av cars ifrån förra uppgiften, skapa
variabeln unique_cars som ska vara en lista där varje bilmärke finns
med exakt en gång
11. Vilken datatyp har variablerna numbers1 och numbers2?
12. Vilka värden finns lagrade i variablerna numbers1 och numbers2?
13. Vad är snittet (intersection) mellan variablerna numbers1 och numbers2?
14. Vad är unionen mellan variablerna numbers1 och numbers2?
15. Vilken är den symmetriska differensen mellan numbers1 och numbers2?
Uppgift B
Projektledaren för ditt utvecklingsteam kommer till dig och vill att du ska skriva ett program.
Programmet har en kravspecifikation enligt punkterna 1-4 nedan. Projektledaren kan inte
programmera så för att hen ska kunna läsa din kod ber hen dig att undvika att använda
loopar och if-satser, om du kan.
1. Programmet ska vara icke-case-sensitive. Det ska alltså inte spela någon roll
om användaren använder stora eller små bokstäver. Namn som skrivs ut ska
dock alltid börja med stor bokstav.
2. Programmet ska låta användaren mata in tre personers namn, ålder och
skostorlek. Dessa uppgifter måste sparas under programmets körning.
3. Programmet ska sedan skriva ut namn och skostorlek på den person som är
äldst samt namn och ålder på den som har medianskostorlek.
4. Efter det ska användaren kunna söka efter personer genom att mata in en av
de tre datatyperna. Om programmet hittar någon som matchar ska dennes
kompletta uppgifter skrivas ut.
Du är fri att designa ditt program hur du vill inom ramen för specifikationen men en
exempelkörning kan se ut som följer:
Please enter name for person 1
>ahmed
Please enter age for person 1
>25
Please enter shoe size for person 1
>42
Please enter name for person 2
>DIANA
Please enter age for person 2
>40
Please enter shoe size for person 2
>38
Please enter name for person 3
>Casper
Please enter age for person 3
>30
Please enter shoe size for person 3
>45
The oldest person is Diana who has shoe size 38
The person with median shoe size is Ahmed who is 25 years old
Please enter search value, name, age or size followed by value
>age 30
Found person
Name: Casper
Age: 30
Size: 45