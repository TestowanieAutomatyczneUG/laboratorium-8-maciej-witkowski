import requests


class MealAPI:
    def search_meal_by_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of string type!")
        result = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}').json()
        if result['meals'] is None:
            return None
        return result
