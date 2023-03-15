from voiture import Voiture

from datetime import datetime 

class Agence:

    def __init__(self,voitures= []):
        self.voitures= voitures
    
    def afficher_voitures(self):
        if self.voitures:
            for i in range(len(self.voitures)):
                print(self.voitures[i].afficher())
        else:
            print('Pas de voiture')
        
    def rechercher_voiture_par_mat(self,matricule):
        trouve = False
        for v in self.voitures:
            if v.matricule == matricule:
                trouve = True
                break
        return trouve

    def ajouter_voiture(self):
        r = input ("Voulez-vous ajouter une voiture? Y for yes | N for no ")
        while True:
            if r == "Y":
                mat = input('Entrez matricule')
                if self.rechercher_voiture_par_mat(mat)==False:
                    print(" Ajouter une voiture ")
                    v= Voiture()
                    v.saisir()
                    self.voitures.append(v)
                    r= input("Voulez-vous rajouter une autre voiture? Y for yes | N for no")           
                else:
                    print(" Cette Voiture existe déjà ! ")
            elif r == "N":
                print('Aucune voiture ajouté')
                break

    def supprimer_voiture(self):    
        r = input ("Voulez-vous supprimer une voiture? Y for yes | N for no ")
        while True:
            if r == "Y":
                mat = input('Entrez matricule')
                if self.rechercher_voiture_par_mat(mat)==True:
                    for v in self.voitures:
                        if v.matricule == mat:
                            i=self.voitures.index(v)
                            del self.voitures[i]
                            r= input("Voulez-vous supprimer une autre voiture? Y for yes | N for no")           
                else:
                    print(" Cette Voiture n'existe pas! ")
            elif r == "N":
                print('Aucune voiture ne va être supprimer')
                break

    def trier_selon_date_circulation(self):
        
        self.voitures.sort(key=lambda v: v.date_circulation)

    def get_voiture_plus_recente(self):
        self.trier_selon_date_circulation()
        print("La voiture la plus récente est:")
        self.voitures[-1].afficher_voiture()

    def get_voiture_plus_ancienne(self):
         self.trier_selon_date_circulation()
         print("La voiture la plus ancienne est:")
         self.voitures[0].afficher_voiture()

    def calcul_distances(self,Voiture):
            pass

    def trier_voitures(self,distance):
            pass

    def afficher_tri(self,indice):
            pass

    def rechercher_voitures_par_similarite(self):
            pass


if __name__=='__main__':
    a=Agence()
    a.ajouter_voiture()
    #a.supprimer_voiture()
    a.trier_selon_date_circulation()
    a.afficher_voitures()
  
    
