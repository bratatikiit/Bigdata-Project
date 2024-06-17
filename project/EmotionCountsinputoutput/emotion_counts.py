from mrjob.job import MRJob
from mrjob.step import MRStep

class EmotionCounts(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_extract_emotion,
                   reducer=self.reducer_count_emotions)
        ]

    def mapper_extract_emotion(self, _, line):
        # Skip the header
        if line.startswith('User_ID'):
            return

        parts = line.split(',')

        # Ensure there are enough parts in the line to avoid index errors
        if len(parts) > 9:
            # Extract dominant emotion
            emotion = parts[9]

            yield emotion, 1

    def reducer_count_emotions(self, emotion, counts):
        yield emotion, sum(counts)

if __name__ == '__main__':
    EmotionCounts.run()
