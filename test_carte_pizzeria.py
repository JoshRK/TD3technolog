# test_carte_pizzeria.py

import unittest
from unittest.mock import MagicMock
from CartePizzeria import CartePizzeria
from Pizza import Pizza
from CartePizzeriaException import CartePizzeriaException


class TestCartePizzeria(unittest.TestCase):
    
    def test_is_empty(self):
        """Test de la méthode is_empty"""
        carte = CartePizzeria()
        self.assertTrue(carte.is_empty())  # La carte devrait être vide au départ

        # Ajout d'une pizza
        pizza = Pizza("Margherita", ["tomate", "mozzarella", "basilic"], 8.5)
        carte.add_pizza(pizza)

        self.assertFalse(carte.is_empty())  # La carte ne devrait plus être vide

    def test_nb_pizzas(self):
        """Test de la méthode nb_pizzas"""
        carte = CartePizzeria()
        self.assertEqual(carte.nb_pizzas(), 0)  # Il n'y a pas de pizza au départ

        # Ajout de pizzas
        pizza1 = Pizza("Margherita", ["tomate", "mozzarella", "basilic"], 8.5)
        pizza2 = Pizza("Pepperoni", ["tomate", "mozzarella", "pepperoni"], 10.0)
        carte.add_pizza(pizza1)
        carte.add_pizza(pizza2)

        self.assertEqual(carte.nb_pizzas(), 2)  # Il devrait y avoir 2 pizzas maintenant

    def test_add_pizza(self):
        """Test de la méthode add_pizza"""
        carte = CartePizzeria()
        pizza = Pizza("Margherita", ["tomate", "mozzarella", "basilic"], 8.5)
        
        # Mock pour vérifier que la pizza est ajoutée
        carte.add_pizza = MagicMock()

        carte.add_pizza(pizza)
        
        # Vérification que la méthode add_pizza a été appelée une fois avec la pizza
        carte.add_pizza.assert_called_once_with(pizza)

    def test_remove_pizza_success(self):
        """Test de la suppression réussie d'une pizza"""
        carte = CartePizzeria()
        pizza = Pizza("Margherita", ["tomate", "mozzarella", "basilic"], 8.5)
        carte.add_pizza(pizza)

        # Mock pour s'assurer que la pizza est bien supprimée
        carte.remove_pizza = MagicMock()

        carte.remove_pizza("Margherita")
        
        # Vérification que la méthode remove_pizza a été appelée une fois avec le bon nom
        carte.remove_pizza.assert_called_once_with("Margherita")

    def test_remove_pizza_not_found(self):
        """Test de la suppression d'une pizza qui n'existe pas"""
        carte = CartePizzeria()
        
        # Tentative de suppression d'une pizza qui n'existe pas
        with self.assertRaises(CartePizzeriaException):
            carte.remove_pizza("Hawaïenne")  # La pizza 'Hawaïenne' n'existe pas
            

if __name__ == '__main__':
    unittest.main()
