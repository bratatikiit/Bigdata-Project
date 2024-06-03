import csv
from dominant_emotion import DominantEmotion

def run_mrjob(input_file, output_file):
    mr_job = DominantEmotion(args=[input_file])

    with mr_job.make_runner() as runner:
        runner.run()

        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Gender', 'Emotion', 'Count'])

            for key, value in mr_job.parse_output(runner.cat_output()):
                gender = key
                emotion_counts = value
                for emotion, count in emotion_counts.items():
                    writer.writerow([gender, emotion, count])

if __name__ == '__main__':
    input_file = 'input.csv'  # Your input CSV file
    output_file = 'output.csv'  # Your output CSV file
    run_mrjob(input_file, output_file)

