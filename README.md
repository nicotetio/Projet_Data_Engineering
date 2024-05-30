Data Engineering Project

Installation :
- 'git clone https://github.com/nicotetio/Projet_Data_Engineering.git'
- cd Projet_Data_Engineering

Download the dataset on : https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

cd DataPreparation and run the SentimentAnalysis.py
You will get another csv file call reviewDataCleaned.csv
Copy this file on the others folders (Web and MLmodel)

Build the Machine Learning model with docker:
- cd MLmodel
- docker build -t {name of the image} .

Run the application :
- cd Web
- docker build -t {name of the image} .
- docker run -p 5000:5000 {name of the image}
- it will run on localhost:5000/
- docker compose up to link the application
- test the application by tap : python test_app.py or python -m unittest test_app
- Install the gnome terminal : sudo apt-get install gnome-terminal
- and then run the shell: bash ./run.sh

Pipeline
