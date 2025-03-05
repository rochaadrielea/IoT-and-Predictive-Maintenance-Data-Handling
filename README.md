**Scalable ML-Powered Identity Verification Performance Monitoring System**

## Introduction
This document explains the tools and methods used in this project in a simple, easy-to-understand way. Imagine you are cooking a meal. You need ingredients, tools, and a recipe to follow. Similarly, in this project, we need data (ingredients), tools (software and libraries), and steps to follow (workflow) to predict which customers might stop using a service (customer churn).

We will go through each part of the project step by step, explaining it in a way that makes sense, even if you are new to these topics.

## Tools and Technologies Used
### **1. Data Gathering: Kaggle**
- Think of Kaggle as a giant online supermarket where we can get free data.
- We downloaded a dataset from Kaggle that contains customer information, like how long they have been using a service and whether they have left or stayed.

### **2. Data Storage: SQLite**
- SQLite is like a small notebook where we store data in an organized way.
- Instead of keeping loose sheets of paper (raw data files), we use SQLite to store everything neatly.
- It allows us to quickly find, update, and analyze data.

### **3. Data Familiarization: SQL**
- SQL (Structured Query Language) is like asking a librarian for a book instead of searching through shelves yourself.
- We use SQL to:
  - Count how many customers are in our dataset.
  - See what kind of information we have.
  - Find patterns in the data (e.g., do older customers leave more often?).

### **4. Data Cleaning & Preparation**
- Imagine you are making a salad, but some vegetables are spoiled or unnecessary. You need to clean and cut them properly.
- In data cleaning, we:
  - Remove useless information (e.g., CustomerID doesn’t help us predict churn, so we ignore it).
  - Fill in missing values so the data is complete.
  - Convert words into numbers because computers understand numbers better.
  - One-hot encoding: If we have ‘Male’ and ‘Female’, we turn it into two separate columns with 0s and 1s (like turning apples and oranges into separate baskets).

### **5. Exploratory Data Analysis (EDA)**
- This is like detective work where we look at our data to find clues.
- We use Python libraries such as **Pandas**, **Matplotlib**, and **Seaborn**.
  - **Pandas**: Like an Excel spreadsheet inside Python, used to look at rows and columns of data.
  - **Matplotlib**: Like a basic drawing tool that helps create simple graphs.
  - **Seaborn**: A fancy version of Matplotlib that makes graphs easier to read.

Example: If we want to see how many customers are leaving, we make a bar chart. If the red bar (customers leaving) is big, we know there's a problem!

### **6. Model Building**
- This is where we train a machine learning model to predict if a customer will leave.
- Think of it like training a dog: you show it examples, and it learns patterns.
- We use **Scikit-learn**, a Python library that provides tools for machine learning.
- Steps:
  1. **Splitting the data**: We divide our data into training (80%) and testing (20%) sets.
  2. **Choosing a model**: We use **Logistic Regression**, a simple model that works like a decision-making checklist.
  3. **Training the model**: The model looks at past data and learns patterns.
  4. **Making predictions**: The model guesses which customers might leave.
  5. **Evaluating performance**:
     - `accuracy_score`: Checks how many predictions were correct.
     - `confusion_matrix`: Shows where the model made mistakes.
     - `classification_report`: Gives detailed results on how well the model did.

### **7. Dashboard and Reporting: Flask**
- Flask is like a waiter in a restaurant: it takes orders (user inputs) and delivers results (predictions) on a website.
- We build a simple website where users can input customer details and see whether they are likely to leave.
- The website displays:
  - A chart of churn trends.
  - A list of high-risk customers.
  - A summary of business insights.

### **Why We Did NOT Use Apache Airflow**
- Apache Airflow is like an advanced kitchen automation system.
- It is useful when you have a complex process that runs daily.
- Since our project is straightforward, using Airflow would be like using a rocket to deliver a pizza.

## **Summary of Results**
- **Goal Achieved:** Successfully identified customers who are likely to leave.
- **Model Accuracy:** About 85% of predictions were correct.
- **Key Findings:**
  - Customers with payment delays are more likely to leave.
  - Subscription type affects churn rate.
- **Impact:**
  - The dashboard allows businesses to see at-risk customers and take action.
  - It helps improve customer retention strategies.

## **Conclusion**
This project shows how we can use data and machine learning to predict customer behavior. By combining Kaggle, SQLite, SQL, Pandas, Scikit-learn, and Flask, we built a system that transforms raw data into actionable insights in a clear and understandable way.

