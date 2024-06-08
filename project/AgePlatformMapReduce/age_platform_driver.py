import os

# Define the HDFS input and output paths
input_path = "hdfs:///test_data/input.csv"
output_path = "hdfs:///output_data/"

# Upload the CSV file to HDFS (if not already uploaded)
os.system(f"hdfs dfs -put -f your_csv_file.csv {input_path}")

# Run the Hadoop Streaming job
os.system(f"""
    hadoop jar /path/to/hadoop-streaming.jar \
        -input {input_path} \
        -output {output_path} \
        -mapper 'python3 age_platform_mapreduce.py mapper' \
        -reducer 'python3 age_platform_mapreduce.py' \
        -file age_platform_mapreduce.py
""")

# Print the output
os.system(f"hdfs dfs -cat {output_path}/part-00000")
