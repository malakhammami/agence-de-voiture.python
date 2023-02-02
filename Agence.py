from datetime import datetime
from voiture import Voiture


class Agence:
    def __init__(self) :
        self.voitures=[]
        
    def afficher_voitures(self):
     for v in self.voitures:
         v.afficher_voiture()
    
    
    
    def ajouter_voiture(self, voiture):
     if self.rechercher_voiture_par_matricule(voiture.matricule):
        print("La voiture avec la matricule " + voiture.matricule + " existe déjà.")
        return
     self.voitures.append(voiture)
     
     
     
    def supprimer_voiture(self, matricule):
        for i, v in enumerate(self.voitures):
            if v.matricule == matricule:
                del self.voitures[i]
                return True
        return False
    
    def afficher_voitures(self):
        for v in self.voitures:
            v.afficher_voiture()
    
    
    
    def rechercher_voiture_par_matricule(self,matricule):
        trouve=False
        for voiture in self.voitures:
            if voiture.matricule == matricule:
                trouve=True
                break
        return trouve
    
    def trier_selon_date_circulation(self):
        self.voitures.sort(key=lambda x: x.date_circulation)
   
   
if __name__ ==  '__main__':
    a=Agence()
   
    voiture1 = Voiture(matricule="789012", marque="Honda", date_circulation=datetime(2019,12,31), kilometrage=20000, cylindrage=2000)
    voiture2 = Voiture(matricule="123456", marque="Toyota", date_circulation=datetime(2020,1,1), kilometrage=10000, cylindrage=1500)
    voiture3 = Voiture(matricule="345678", marque="Ford", date_circulation=datetime(2021,1,1), kilometrage=30000, cylindrage=3000)
    voiture4 = Voiture(matricule="45678", marque="kia", date_circulation=datetime(2021,1,1), kilometrage=30000, cylindrage=3000)
    a.ajouter_voiture(voiture1)
    a.ajouter_voiture(voiture2)
    a.ajouter_voiture(voiture3)
    a.ajouter_voiture(voiture4)
    a.supprimer_voiture("345678")
    a.afficher_voitures()
    a.trier_selon_date_circulation()
    
    
     