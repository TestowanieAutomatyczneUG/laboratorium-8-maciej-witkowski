import requests


class MealAPI:
    def search_meal_by_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of string type!")
        result = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}').json()
        if result['meals'] is None:
            return None
        return result

    def list_all_meals_by_first_letter(self, letter):
        if not isinstance(letter, str):
            raise TypeError("Letter must be of string type!")
        if len(letter) == 0 or len(letter) > 1:
            raise ValueError("Wrong input length!")
        result = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={letter}').json()
        if result['meals'] is None:
            return None
        return result
