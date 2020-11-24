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

    def lookup_full_meal_details_by_id(self, index):
        if not isinstance(index, str):
            raise TypeError("Id must be of string type!")
        result = requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={index}').json()
        if result['meals'] is None:
            return None
        return result

    def lookup_a_single_random_meal(self):
        return requests.get('https://www.themealdb.com/api/json/v1/1/random.php').json()

    def list_all_meal_categories(self):
        return requests.get('https://www.themealdb.com/api/json/v1/1/categories.php').json()

    def list_all_categories_area_ingredients(self, option):
        if not isinstance(option, str):
            raise TypeError("Option must be of string type!")
        if option == 'c' or option == 'a' or option == 'i':
            return requests.get(f'https://www.themealdb.com/api/json/v1/1/list.php?{option}=list').json()
        else:
            return None

    def filter_by_main_ingredient(self, ingredient):
        if not isinstance(ingredient, str):
            raise TypeError("Ingredient must be of string type!")
        result = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}').json()
        if result['meals'] is None:
            return None
        return result

    def filter_by_category(self, category):
        if not isinstance(category, str):
            raise TypeError("Category must be of string type!")
        result = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}').json()
        if result['meals'] is None:
            return None
        return result
