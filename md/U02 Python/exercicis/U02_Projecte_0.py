import re   #regular expression
import math
import flet as ft
import flet.canvas as cv

# Funció que comprova un color en hexadecimal
def comprovaHEX(hex_string):
  match =re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_string)
  if match:
    return True
  else:
    return False

class Punt():
  pass

class Figura():
  pass

class Linia(Figura):
  pass

class Rectangle(Figura):
  pass

class Cercle(Figura):
  pass
  
# creem el dibuix per defecte
Dibuix={
  "ample":800,
  "alt":600,
  "Figures":[]
}

# mètode que a partir del nom del fitxer de text
# carrega el dibuix en memòria
def loadDibuix(fileName):
  pass

# mètode que guarda el dibuix que està en memòria
# en un arxiu SVG
def saveDibuix(fileName):
  pass

# Funció que pinta el menú principal i retorna la opció escollida
def menu():
  pass


# Funció que pinta el menú de Figura i retorna la opció escollida
def triarFigura():
  pass

# Mètode que pinta el dibuix. Complet. 
# NO MODIFICAR
def dibuixar(page: ft.Page):
  page.window_width = Dibuix["ample"]        
  page.window_height = Dibuix["alt"]       
  page.window_resizable = False  
  page.title = "Les meues figures"
  page.update()

 
  figs=[]
  for f in Dibuix["Figures"]:
    if type(f) is Linia:
      figs.append(cv.Line(f.getPos().getX(),f.getPos().getY(),f.getAltre().getX(),f.getAltre().getY(),
              paint=ft.Paint(stroke_width=1, style=ft.PaintingStyle.STROKE,color=f.getColor())))
    if type(f) is Rectangle:
      figs.append(cv.Rect(f.getPos().getX(),f.getPos().getY(),
                          f.getPos().dist_x(f.getAltre()),
                          f.getPos().dist_y(f.getAltre()),
              paint=ft.Paint(stroke_width=1, style=ft.PaintingStyle.FILL,color=f.getColor())))
    if type(f) is Cercle:
      figs.append(cv.Circle(f.getPos().getX(),f.getPos().getY(),
                          f.getRadi(),
              paint=ft.Paint(stroke_width=1, style=ft.PaintingStyle.FILL,color=f.getColor())))
  cp = cv.Canvas(
        figs,
        width=float("inf"),
        expand=True,
  )
  page.add(cp)


# programa principal
def main():
  pass

# crida al programa principal
if __name__=="__main__":
  main()
