### The Data
We have a real-world dataset from a company that contains information about online purchases. We have 46,152 rows , each of them representing a unique transaction. Specifically, the company operates both a web page and a mobile app, through which users can initiate transactions using any of the following devices;
- desktop (web)
- tablet (web)
- mobile (web)
- android (app)
- ios (app)  

### The Goal: 
The main goal of this project is to provide insights into the performance of different customer segments. Specifically, we will segment users based on the devices they use to make purchases and then investigate different performance metrics to identify which ones must be carefully examined by business stakeholders.

We will begin with a data cleaning and transformation process and then proceed to analyze and visualize our findings.

### Workflow
Our workflow is as follows: 
- **Data Cleaning & Transformation**:          
We have created a python script `clean_transform.py` to clean and transform the data. The `transform` function that is provided creates an extra column based on the segment that each user belongs to.


- **Extracting Insights**: We explore data to answer questions like;
    - what is the number of transactions per device? 
    - how many users use one device and which device?
    - how many use two or more devices? In this case we break down between 'web' only and how many both  'web' and 'android'. 
    
    Additionally, we investigate perfomance metrics such as total Revenue, Transactions, Revenue per User, Transactions per User and Revenue per Transaction.

- **Constructing an Interactive Dashboard**: We will communicate our results through an easy-to-use interactive dashboard. It is important to share the results with individuals from the business sector.


