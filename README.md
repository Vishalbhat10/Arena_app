# Arena_app
Built a Flask application to explore GIS(Geography information system).
Used PostgreSQL with postgis database components.
# Procedure to run the application:
Step1: Install required packages

Command:Pip install -r requirements.txt

step2: Download Shape files for constructing map.

links

Arena shape file : https://www.sciencebase.gov/catalog/item/4f4e4a0ae4b07f02db5fb54d

Congressinal districts shape files :  https://www.sciencebase.gov/catalog/item/4f4e4a06e4b07f02db5f8b58

States shape files : https://www.sciencebase.gov/catalog/item/4f4e4783e4b07f02db4837ce

County shape files : https://www.sciencebase.gov/catalog/item/4f4e4a2ee4b07f02db615738


step3: Run the database_1.py and database_2.py to create the schema and table associated.

Command: python database_1.py/database_2.py

step4: Run Flask application.

Command : python app.py

Open the browser and go to http://localhost:5000/ to run the application.
