from . import variables

class Proj():
  
    def __init__(self, nom: str, description, url, occ):
        self.nom = nom
        self.description = self.suspension(description)
        self.url = url
        self.liste_tech = []        

    def __str__(self):
        return self.nom

    def techs(self, liste: list):
        for elt in liste:
            self.liste_tech.append(elt)

    def suspension(self, texte):
        maxi = 125
        # print(self.nom, maxi, len(texte))
        if len(texte) > maxi:
            nouveau_texte = ""
            for elt in texte:
                
                if len(nouveau_texte) < maxi: 
                    nouveau_texte += elt
                else:
                    nouveau_texte += "..."
                    break   

            return nouveau_texte

        else:
            return texte 

 
          

