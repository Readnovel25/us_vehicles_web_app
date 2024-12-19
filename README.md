# us_vehicles_web_app

This project takes a look at a dataset on used vehicles advertisements and produces a web application using `streamlit` to display what factors affect the listed price most. It primarily utilizes the following libraries throughout:
* `streamlit`
* `pandas`
* `plotly`

You can find all imported libraries for this project [here](requirements.txt)

## Exploratory Data Analysis
The dataset provided contains missing values and implicit duplicate values in the `'model'` column so it was necessary to explore and analyze the data before building the web application. This was done in a Jupyter notebook to better illustrate why/how missing values were filled, you may utilize a separate python script for this purpose as well.

After exploring the data and ensuring that it was in an acceptable state for data visualization in the app, the next step is to build some plots to display in the app and think about how to make them interactive. This was also done in the Jupyter notebook with the help of the `plotly-express` library.

[EDA Notebook](notebooks\EDA.ipynb)

## Data Visualization
For this project, a histogram of the price distribution by transmission, type, fuel type, cylinder engine, condition, or paint color was chosen as the first plot. The category to plot against the price can be chosen by the user with a dropdown.

Secondly, a scatterplot of the price vs the odometer value or days since vehicle was listed by age category was chosen as the second and final interactive visual. Similarly to the histogram, users can chose which variable they want to plot against price.

## Web App
Once you've cleaned up the data and chosen the plots/visuals, you can start building the application using streamlit. For this project, the app was deployed using Render, but you can deploy it locally with `streamlit`.

To deploy your app locally, run the `streamlit run app.py` command from the terminal.

[Script for app](app.py)
[Live web app](https://us-vehicles-web-app.onrender.com)
