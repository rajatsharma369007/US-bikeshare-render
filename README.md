# US Bikeshare 

***

## Description
This project utilizes Python to analyze bike share data from Chicago, New York City, and Washington. It includes both a command-line interface for interactive data exploration and a web application built with Flask to present these statistics visually.
***



## Project Files
- **bikeshare.py** - Script for analyzing bikeshare data
- **chicago.zip** - Dataset for Chicago (zipped CSV file)
- **new_york_city.zip** - Dataset for New York City (zipped CSV file)
- **washington.zip** - Dataset for Washington (zipped CSV file)
- **app.py** - Flask application for visualizing bikeshare data
- **templates/master.html** - Main page template for the Flask app
- **templates/go.html** - Results page template for the Flask app
***

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/US-bikeshare-render.git
   cd US-bikeshare-render
2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
4. **Unzip the dataset files:**
    ```bash
    unzip chicago.zip -d data/
    unzip new_york_city.zip -d data/
    unzip washington.zip -d data/
5. **Run the Flask application:**
    ```bash
    python app.py
6. **Access the web application: Open your web browser and go to:**
http://127.0.0.1:5000/

***

## Render Deployment
You can access the deployment of this app. Visit here: https://us-bikeshare-render.onrender.com/

*** 

## Acknowledgment

We would like to thank the following resources and individuals for their contributions and support:

- **Udacity** - For providing the project idea and initial dataset.
- **Plotly** - For the powerful data visualization library used in this project.
- **Flask** - For the web framework that made building the web application possible.
- **Pandas** - For the data manipulation and analysis library.
- **Render** - For providing the platform to deploy the web application.

Special thanks to all the contributors and the open-source community for their invaluable tools and libraries.

