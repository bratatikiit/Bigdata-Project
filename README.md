## Project Overview
# This project leverages Big Data technologies, including Hadoop,Mapreduce ,HBase, Databricks, and Kafka, to analyze the impact of social media usage on emotional well-being. By processing large datasets from Kaggle, we aim to uncover correlations between social media interactions and user sentiment.

# Technologies and Tools
**HBase: A distributed column-oriented database for storing and managing large datasets.**
Databricks: A unified analytics platform that simplifies the development and deployment of data pipelines and machine learning models.
Kafka: A distributed streaming platform for processing real-time data streams.
Python: The primary programming language used for data processing, analysis, and visualization.
Jupyter Notebook: An interactive environment for data exploration and analysis.
Data Pipeline
Data Ingestion:
Kafka: Ingests data streams from various social media platforms and stores them in Kafka topics.
Data Processing:
Databricks: Reads data from Kafka topics, performs data cleaning, feature engineering, and transformation using Spark.
HBase: Stores processed data in HBase for efficient querying and analysis.
Data Analysis:
Databricks: Executes SQL queries, machine learning algorithms, and statistical analysis on the processed data.
Visualization:
Jupyter Notebook: Creates visualizations using libraries like Matplotlib, Seaborn, and Plotly to present insights and findings.
Key Findings
Hadoop: A distributed computing framework for processing large datasets across clusters of computers.
MapReduce: A programming model for processing and generating large datasets.

"A strong correlation was found between the number of daily social media posts and levels of anxiety."

Future Work
Real-time Analysis: Explore real-time data processing using Kafka Streams or Spark Structured Streaming for more timely insights.
Advanced Machine Learning: Experiment with more complex machine learning models, such as deep learning, to improve prediction accuracy.

Project Structure
project_folder/
├── data/
│   ├── raw_data/
│   └── processed_data/
├── notebooks/
│   ├── data_ingestion.ipynb
│   ├── data_processing.ipynb
│   ├── data_analysis.ipynb
│   └── visualization.ipynb
├── src/
│   ├── utils.py
│   └── models.py
├── requirements.txt
