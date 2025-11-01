# 🛍️ E-Commerce Data Warehouse & Sales Dashboard

This project focuses on building a complete data warehouse and analytics pipeline for an e-commerce business that sells across multiple sales channels such as website, app, and physical stores.  
The goal was to consolidate all this data into a single, reliable source of truth and visualize key insights using Tableau.

## 💡 Project Motivation

In real businesses, sales data is often scattered across multiple systems namely store POS databases, online transaction logs, and third-party apps.  
This makes it difficult to get a unified view of performance, customer behavior, or inventory movement.  

I wanted to replicate that real-world challenge by:
- Designing a data warehouse schema (Star Schema)
- Building a simple ETL (Extract, Transform, Load) flow to clean and connect data
- Finally, visualizing everything with Tableau to analyze overall performance

## ⚙️ Tech Stack

- Python + Pandas : for generating and cleaning CSV data  
- Star Schema Design : for data modeling (Fact & Dimension tables)  
- Tableau : for visualization and dashboard creation  

## 🧱 Data Warehouse Schema

The data warehouse was structured using a Star Schema with one fact table and three dimensions:

| Table | Type | Description |
|--------|------|-------------|
| `fact_sales` | Fact | Core sales transactions including quantities, prices, and links to dimensions |
| `dim_customer` | Dimension | Customer demographics, locations, and channels |
| `dim_product` | Dimension | Product categories and subcategories |
| `dim_date` | Dimension | Calendar hierarchy (year, month, day) |

Each table is linked by primary and foreign keys (`customer_id`, `product_id`, `date_id`).

## 📊 Visualization using Tableau

After cleaning and linking the datasets, I designed an interactive Tableau dashboard to visualize:

1. Total Sales
2. Total Orders
3. Unique Customers
4. Date & Category-wise Trends
5. Top Performing Products

The dashboard provides a consolidated view of online and offline sales channels and can easily be expanded to handle larger datasets (e.g., 5M+ records).

## 🧠 Challenges Faced

This project was a real learning experience. Some challenges included:

1. Dataset Linking Confusion in Tableau
   
   Initially, Tableau created multiple copies of the same tables and didn’t recognize relationships. I had to delete extra tables, manually define logical relationships (using `product_id`, `customer_id`, etc.), and rebuild the schema properly.

2. KPI Formatting & Decimal Display Issues
   
   While building KPI cards, Tableau showed long or unformatted numbers. I corrected this by adjusting the “Number Format” (setting decimals, currency format, etc.).

3. Visualization Layout

   Getting all five visualizations neatly aligned in the dashboard was tricky. I learned to use horizontal and vertical containers to organize the layout professionally.

4. Tool Restrictions
   
   Power BI required a Microsoft account and didn’t allow personal logins, so I switched to Tableau Public. Tableau Public also lacked a “Save As” option until publishing once online, which I learned through trial and error.

5. Establishing Joins on Tableau
   
   I was not aware of the difference between logical relationships and physical joins. This took me sometime to understand after which I implemented left join between the tables.

## 🔍 Insights Gained

- Online sales contributed the majority of revenue, but store sales had higher average order values.  
- Customer activity spiked during seasonal periods (especially near end-of-quarter months).  
- Top-selling categories varied by channel — electronics online, apparel in stores.  

## 🔧 Improvements & Next Steps

If I extend this project further, I’d like to:

1. Integrate Cloud Storage - Host the data warehouse on AWS Redshift or Google BigQuery for scalability.

2. Enhanced Visuals - Add filters by region, product category, and channel to make the dashboard more interactive.


