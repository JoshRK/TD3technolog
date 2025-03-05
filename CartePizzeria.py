from CartePizzeriaException import CartePizzeriaException  # Importer l'exception

class CartePizzeria:
    def __init__(self):
        self.pizzas = []
    
    def is_empty(self):
        """Retourne True si la carte est vide, sinon False."""
        return len(self.pizzas) == 0
    
    def nb_pizzas(self):
        """Retourne le nombre de pizzas dans la carte."""
        return len(self.pizzas)
    
    def add_pizza(self, pizza):
        """Ajoute une pizza à la carte."""
        self.pizzas.append(pizza)
    
    def remove_pizza(self, name):
        """Retire la pizza nommée 'name' de la carte. Lève une exception si elle n'existe pas."""
        pizza_to_remove = None
        for pizza in self.pizzas:
            if pizza.nom == name:
                pizza_to_remove = pizza
                break
        
        if pizza_to_remove is None:
            raise CartePizzeriaException(f"La pizza '{name}' n'existe pas dans la carte.")
        
        self.pizzas.remove(pizza_to_remove)
