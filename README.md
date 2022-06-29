# Minesweeper_AI
AI voor minesweeper

# Getting started

## requirements
Om dit programma te gebruiken heb je een aantal dingen nodig

  - Python
  - Tkinter (Standaard library van python)
  - Threading (Standaard library van python)
  - Time (Standaard library van python)

## gebruik
Om dit programma te gebruiken hoef je alleen maar het main.py script te runnen.


# Algorithm
## logica
algoritme in logica uit pagina 20 van https://dash.harvard.edu/bitstream/handle/1/14398552/BECERRA-SENIORTHESIS-2015.pdf
![image](https://user-images.githubusercontent.com/90763686/176479118-8d5163fe-e1e6-4cd6-b321-7dc179ec49d8.png)

## uitleg algoritme
Op het plaatje valt te zien dat er eigenlijk elke keer over een lijst van cellen wordt gelooped en wordt gekeken of het voldoet aan 1 van 2 eisen, AFN of AMN, maar wat houden deze 2 eisen in, zie hieronder

## AFN
AFN ook wel "All Free Neighbours" betekent dat het aantal gemarkeerde bommen om de cel heen evenveel is als de waarde van de cel (hoeveel bommen er echt om de cel liggen) daardoor weet je dus dat je alle cellen om de cel heen die niet gemarkeerd zijn kan aanklikken.
zie ook het plaatje hieronder 

![image](https://user-images.githubusercontent.com/90763686/176496589-047c8d43-8700-4919-b7bc-33d780939e7a.png)

## AMN
AMN ook wel "All Marked Neighbours" betekend dat het aantal gemarkeerde bommen om een cel + het aantal dichte cellen om een cel heen evenveel is als de waarde van een cel, waardoor je alle cellen om de cel kan markeren als bommen.
zie ook het plaatje hieronder

![image](https://user-images.githubusercontent.com/90763686/176498713-9467036b-a882-4b86-8da0-a5399729efdc.png)
 
## keuze algoritme
Ik heb dit algoritme gekozen omdat het een heel erg duidelijk algoritme is maar het toch best goed/snel werkt. Er hoeven geen grote berekeningen uit te uitgerekend te worden. Het algoritme gebruikt daardoor ook niet veel geheugen, hij hoeft alleen maar een lijst bij te houden van cellen, en eentje van waar de bommen liggen.

Dit algoritme zal een goede ervaren speler niet helpen, maar mijn opdrachtgever (mijn moeder) is dat niet, dus dit algoritme kan haar helpen met het sneller/beter oplossen van minesweeper bord.


