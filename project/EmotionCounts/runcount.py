import csv
import subprocess
import tempfile
import os
from emotion_counts import EmotionCounts

def run_mrjob(input_file, output_dir):
    # Create a temporary local file to store the intermediate output
    temp_output_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
    temp_output_filename = temp_output_file.name

    try:
        # Remove the existing output directory if it exists
        subprocess.run(['hdfs', 'dfs', '-rm', '-r', output_dir], check=False)

        # Run the MRJob with HDFS input and temporary local output
        mr_job = EmotionCounts(args=['-r', 'hadoop', input_file, '--output-dir', output_dir])

        with mr_job.make_runner() as runner:
            runner.run()

            # Read the intermediate output from HDFS
            subprocess.run(['hdfs', 'dfs', '-getmerge', f'{output_dir}/part-*', temp_output_filename], check=True)

            # Write the final output to the desired HDFS path
            final_output_path = f'{output_dir}/emotion_counts.csv'
            with open(temp_output_filename, 'r') as infile:
                with open('final_output.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['Emotion', 'Count'])

                    for line in infile:
                        emotion, count = line.strip().split('\t')
                        writer.writerow([emotion, count])

            # Put the final output CSV to HDFS
            subprocess.run(['hdfs', 'dfs', '-put', 'final_output.csv', final_output_path], check=True)

    finally:
        # Clean up temporary files
        os.remove(temp_output_filename)
        if os.path.exists('final_output.csv'):
            os.remove('final_output.csv')

if __name__ == '__main__':
    input_file = 'hdfs:///test_data/input.csv'  # Your input HDFS CSV file
    output_dir = 'hdfs:///output_data/'  # Your output HDFS directory
    run_mrjob(input_file, output_dir)
