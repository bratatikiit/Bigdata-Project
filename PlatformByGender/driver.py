import csv
from platform_by_gender import PlatformByGender
from mrjob.job import MRJob

# Function to run the MapReduce job
def run_mrjob(input_file, output_file):
    mr_job = PlatformByGender(args=[input_file])

    with mr_job.make_runner() as runner:
        runner.run()

        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Gender', 'Platform', 'Count'])

            for key, value in mr_job.parse_output(runner.cat_output()):
                gender, platform = key
                count = value
                writer.writerow([gender, platform, count])

if __name__ == '__main__':
    input_file = 'input.csv'  # Your input CSV file
    output_file = 'output_gender.csv'  # Your output CSV file
    run_mrjob(input_file, output_file)

