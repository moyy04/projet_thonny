import tkinter as tk
from math import *
(Hauteur,Largeur) = (500,700)
root = tk.Tk()
root.title('Aidez la fille de rentrer chez elle avec votre souris!')
Dessin = tk.Canvas(root,height=Hauteur,width=Largeur,bg='#B2D9EA')
Dessin.pack()

#Le soleil
def disque(x,y,r,couleur):
    p=(x+r,y+r)
    q=(x-r,y-r)
    return Dessin.create_oval(p,q,fill=couleur,outline=couleur)
disque(670,30,60,'#FDCF76')
Dessin.create_line((560,30),(600,30),width=2,fill='#E08963',cap='round')
Dessin.create_line((610,60),(575,80),width=2,fill='#E08963',cap='round')
Dessin.create_line((637,90),(620,115),width=2,fill='#E08963',cap='round')
Dessin.create_line((680,97),(680,125),width=2,fill='#E08963',cap='round')

#La rue
Dessin.create_rectangle((0,82),(480,123),fill='#AA7B6F',outline='#AA7B6F')
Dessin.create_line((75,230),(480,173),width=40,fill='#AA7B6F',cap='round')
Dessin.create_oval((400,82),(530,193),outline='#AA7B6F',fill='#AA7B6F')
Dessin.create_line((350,143),(450,140),width=43,fill='#B2D9EA',cap='round')
Dessin.create_line((75,265),(380,300),width=40,fill='#AA7B6F',cap='round')
Dessin.create_oval((45,210),(130,284),outline='#AA7B6F',fill='#AA7B6F')
Dessin.create_line((97,247),(235,250),width=12,fill='#B2D9EA',cap='round')
Dessin.create_line((90,380),(380,340),width=40,fill='#AA7B6F',cap='round')
Dessin.create_rectangle((90,439),(700,439),width=40,fill='#AA7B6F',outline='#AA7B6F')
Dessin.create_oval((354,283),(440,357),outline='#AA7B6F',fill='#AA7B6F')
Dessin.create_line((300,320),(365,320),width=13,fill='#B2D9EA',cap='round')
Dessin.create_oval((40,361),(130,460),outline='#AA7B6F',fill='#AA7B6F')
Dessin.create_line((100,408),(190,404),width=21,fill='#B2D9EA',cap='round')

#La maison
Dessin.create_rectangle((560,320),(680,445),outline='#E18D96',fill='#F4AFB3')
q1 = (560,319)
q2 = (680,319)
q3 = (620,270)
triangle=[560,319,680,319,620,270]
Dessin.create_polygon(triangle,fill='#8EC9BB')
Dessin.create_line(q1,q2,fill='#619196')
Dessin.create_line(q2,q3,fill='#619196')
Dessin.create_line(q3,q1,fill='#619196')
Dessin.create_rectangle((600,370),(640,445),outline='#BC85A3',fill='#9799BA')
disque(630,410,3,'#D3C0F9')

class Etat():
    def __init__(self):
        self.commencer=False
        self.souris_presse=False

class Fille():
    def __init__(self):
        self.etat=Etat()
        self.x=25
        self.y=50
    #La fille
        self.jambe_gauche=Dessin.create_line((27,70),(27,86))
        self.jambe_droite=Dessin.create_line((33,70),(33,86))
        self.main_droite=Dessin.create_line((36,50),(43,47))
        self.main_gauche=Dessin.create_line((25,50),(15,47))
        self.cheveux=Dessin.create_rectangle((22,23),(37,47),outline='black',fill='#F1E0B0')
        self.robe=Dessin.create_polygon([20,70,40,70,30,30],fill='#F26BAA',outline='black')
        self.visage=Dessin.create_oval((30+10,30+10),(30-10,30-10),fill='#FCF0CF')
        self.oeil_gauche=disque(25,30,0.5,'black')
        self.oeil_droite=disque(35,30,0.5,'black')
        self.pied_gauche=Dessin.create_oval((26,86),(31,91),fill='#F26BAA')
        self.pied_droite=Dessin.create_oval((32,86),(37,91),fill='#F26BAA')
        self.affichage()

    def affichage(self,event=None):
        if event != None:
    #la difference entre la position de la souris et la fille
            dx = event.x - self.x
            dy = event.y - self.y
    #Deplacer la fille par rapport à la souris
            Dessin.move(self.robe, dx, dy)
            Dessin.move(self.jambe_gauche, dx, dy)
            Dessin.move(self.jambe_droite, dx, dy)
            Dessin.move(self.visage, dx, dy)
            Dessin.move(self.oeil_gauche, dx, dy)
            Dessin.move(self.oeil_droite, dx, dy)
            Dessin.move(self.main_droite, dx, dy)
            Dessin.move(self.main_gauche, dx, dy)
            Dessin.move(self.cheveux, dx, dy)
            Dessin.move(self.pied_droite, dx, dy)
            Dessin.move(self.pied_gauche, dx, dy)
                
    #Les coordonnees des pieds et de la robe de la fille
            coords_pied_gauche = Dessin.coords(self.pied_gauche)
            coords_pied_droite = Dessin.coords(self.pied_droite)
            coords_visage = Dessin.coords(self.visage)
                
            def texte(x,y,t,f,c):
                Dessin.create_text((x,y),text=t,font=f,fill=c)
                
    #Si la fille est passe ces limites, vous avez perdu
            L=[((0,82),(480,123)),((400, 82), (530, 193)),((75, 169), (480, 240)),((45,210),(130,284)),((75,255),(380,320)),((354,283),(440,357)),((90,330),(440,392)),((40,361),(130,460)),((80,400),(700,480))]

            def est_dans_limite(coords, limites):
                x1, y1, x2, y2 = coords
                (inf_x, inf_y), (sup_x, sup_y) = limites
                return x1 >= inf_x and x2 <= sup_x and y1 >= inf_y and y2 <= sup_y
            
            def bien_limite(coords_pied_gauche,coords_pied_droite,limites):
                for limit in limites:
                    if not(est_dans_limite(coords_pied_gauche, limit) or est_dans_limite(coords_pied_droite, limit)):
                        pass 
                    else: return True

            if bien_limite(coords_pied_gauche, coords_pied_droite,L):
                #Au moins un des pieds de la fille est dans la rue
                pass
            else:
                #La fille est hors de la rue, elle est tombee, vous avez perdu !
                self.etat.souris_presse = False
                self.etat.commencer = False
                texte(Hauteur//1.32,Largeur//3,"Oh non, vous avez perdu !!!",'LinuxLibertine 20 bold','#F24444')
                raise ValueError("Perdu T-T")
                
            if est_dans_limite(coords_visage,((600,370),(640,445))):
                texte(Hauteur//1.32,Largeur//3,"Youpi, vous avez réussi !!!",'LinuxLibertine 20 bold','#0487D9')
                texte(535,375,"Merci beaucoup !",'LatinModernMono 10','#AB6393')
                self.etat.souris_presse = False
                self.etat.commencer = False
                    
    #Mettre à jour les coordonnees de la fille
            self.x = self.x+dx
            self.y = self.y+dy

    def souris_presse(self,event):
        self.etat.souris_presse = True

    def souris_release(self,event):
        self.etat.souris_presse = False
    
    def commencer_jeu(self):
        self.etat.commencer = True
        
    def souris_bouge(self,event):
        if self.etat.souris_presse and self.etat.commencer:
            self.affichage(event)

def tictac():
    if etat.commencer==True and etat.souris_presse==True:
        etat.x = etat.x+dx
        etat.y = etat.y+dy
        etat.affichage()
        Dessin.after(3,tictac)
    
fille=Fille()
etat=Etat()
bouton1=tk.Button(root,text='Start',command=fille.commencer_jeu,width=9)
bouton1.pack()
root.bind("<Button-1>", fille.souris_presse)
root.bind("<ButtonRelease-1>", fille.souris_release)
root.bind("<B1-Motion>", fille.souris_bouge)
root.mainloop()