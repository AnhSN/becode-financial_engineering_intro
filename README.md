<h2 align="center"> Forecasting & optimization project </h2>
<p align="center"><a href="https://github.com/AnhSN/becode-financial_engineering_intro.git">
<img src="assets/BeCode_color.png" alt="Logo of BeCode"></a></p>

<h3 align="center">Introduction to financial engineering made during <a href="https://github.com/becodeorg">BeCode</a> training.</h3><br><br>

## Description

[WIP]

The project is divided in x folders:

1. scraper: First, the collect of our data.
2. xx: yyyy

## Installation

1. Clone the repo.
2. If you just wanna deploy the app, install the required libraries using

   ```
   pip install requirements_app.txt
   ```

   * numpy 1.24.2
   * pandas 1.5.3
   * pillow 9.4.0
   * scikit_learn 1.2.1
   * streamlit 1.19.0

   If you wanna run the whole code, install all the required libraries using

   ```
   pip install requirements.txt
   ```

   * imbalanced_learn 0.10.1
   * imblearn 0.0
   * ipympl 0.9.3
   * matplotlib.pyplot 3.7.0
   * numpy 1.24.2
   * pandas 1.5.3
   * pillow 9.4.0
   * pipreqs 0.4.11
   * pipreqsnb 0.2.4
   * plotly.graph_objects
   * plotly.subplots
   * scikit-learn 1.2.1
   * seaborn 0.12.2
   * skimpy
   * sqlite3 5.1.2
   * streamlit 1.19.0
3. Launch our app using

   ```
   streamlit run app.py
   ```

## Usage

#### scraper

[WIP]

#### xx

[WIP]

#### zz

In this folder, we worked on 2 models: one for classification and another one for clustering.
*classification.py* classifies the data between existing customer and attrited customer. 
*clustering.py* defines 6 different profiles of customer and their probability to churn.

<table border="0">
 <tr>
    <td><p style="font-size:1em" align="center">Illustration from classification</b></td>
    <td><p style="font-size:1em" align="center">Illustration from clustering</b></td>
 </tr>
 <tr>
    <td><img src=".streamlit/Confusion_Matrix_Classification.png" alt="confusion matrix from classification" align="center"></td>
    <td><img src=".streamlit/clustering_illu.png" alt="graph from clustering model" align="center"></td>
 </tr>
</table>

#### dd

We used Tableau to create a dashboard which allows us to understand customer's profiles. 
It shows the characteristic parameters of attrited customers and the KPI of the data (in numerical form).

<img src="visualizations/Images/0.2-Dashboard Analytics.png" alt="dashboard analytics" align="center">

## Results

We managed to predict if a specific client is likely to churn. With our models, the accuracy for existing customer is 97% while the accuracy for attrited customer is 71%.

<img src=".streamlit/classification_report.png" align="center">

You can check our deployed app there: [https://churn-prediction-h564.onrender.com]([https://churn-prediction-h564.onrender.com/]()) .

## Contact

project made by [Anh Sophie Noël](https://github.com/AnhSN).
