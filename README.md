# Minesweeper_AI
AI voor minesweeper

# Getting started
## vereisten
Om dit programma te gebruiken moet je de volgende programma's geïnstalleerd hebben
  - Python
  - Threading (library voor python)
  - Tkinter (library voor python)
  - Time (library voor python)

# Algorithm
algoritme in logica uit pagina 20 van https://dash.harvard.edu/bitstream/handle/1/14398552/BECERRA-SENIORTHESIS-2015.pdf
S ← {}
  while game is not over do
    if S is empty then
      x ← Select-Random-Square()
      S ← {x}
    end if
  for x ∈ S do
    probe(x)
    if x = mine then
      return failure
    end if
    Ux ← Unmarked-Neighbors(x)
    if isAFN(x) = True then
      for y ∈ Ux do
        S ← S ∪ {y}
      end for
    else if isAMN(x) = True then
      for y ∈ Ux do
        mark(y)
      end for
    else
      Ignore x
    end if
  end for
end while
![image](https://user-images.githubusercontent.com/90763686/176478986-4feb75e2-36d0-4040-a959-f453d8607dd2.png)

## AFN

## AMN

# requirements
