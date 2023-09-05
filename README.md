Test for Sarafan LLC
# Test Task: Building a shop project

Background:
Your company is developing a new web application that requires a grocery management system.

Task Overview:
Create a shop project as a web application. The application should consist of backend

## General Requirements:

1. The possibility of creating, editing, deleting categories and subcategories of goods in the admin panel should be implemented.
2. Categories and subcategories must have a name, slug name, image
3. Subcategories must be related to the parent category ***- I use django-mptt here*** 
4. An endpoint must be implemented to view all categories with subcategories. Pagination should be provided.
5. The possibility of adding, changing, deleting products in the admin panel should be implemented.
6. Products must belong to a certain subcategory and, accordingly, the category must have a name, slug-name, image in 3 sizes, price
7. An endpoint for displaying products with pagination should be implemented. Each product in the output must have the following fields: name, slug, category, subcategory, price, image list
8. Implement an endpoint for adding, changing (changing the quantity), deleting a product in the cart.
9. Implement an endpoint for displaying the contents of the basket with the calculation of the number of goods and the sum of the cost of goods in the basket.
10. Implement the ability to completely empty the basket
11. Operations on endpoints of categories and products can be performed by any user
12. Operations on cart endpoints can only be performed by an authorized user and only with their cart
13. Implement authorization by token
14. The project is implemented on the framework: Django Rest Framework

## Installation Instructions
***- Clone the repository:***
```
git clone git@github.com:HukumaBob/test_sarafan.git
```

***- Install and activate the virtual environment:***
- For MacOS/Linux
```
python3 -m venv venv
```
- For Windows
```
python -m venv venv
source venv/bin/activate
source venv/Scripts/activate
```

***- Install dependencies from the requirements.txt file:***
```
pip install -r requirements.txt
```
***- Add .env***
```
copy .env.copy .env
```

***- Apply migrations in the folder with the manage.py file:***
```
python manage.py migrate
```
***- Create superuser:***
```
python manage.py createsuperuser
```

***- Start development server at http://127.0.0.1:8000/admin***

***- For API documentation goto http://127.0.0.1:8000/redoc or http://127.0.0.1:8000/swagger***

***- Write a program that prints the first n elements of the sequence 122333444455555... (the number is repeated as many times as it is equal to)***
in folder triangle_pattern_number - main.py
