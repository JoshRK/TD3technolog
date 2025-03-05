class Pizza:
    def __init__(self, nom, ingredients, prix):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix
    
    def __repr__(self):
        return f"Pizza({self.nom}, {self.ingredients}, {self.prix}€)"
