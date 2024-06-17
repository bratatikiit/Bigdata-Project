from mrjob.job import MRJob
from mrjob.step import MRStep

class PostCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_platform,
                   reducer=self.reducer_count_posts)
        ]

    def mapper_get_platform(self, _, line):
        # Skip the header
        if line.startswith('User_ID'):
            return

        parts = line.split(',')

        # Ensure there are enough parts in the line to avoid index errors
        if len(parts) > 3:
            platform = parts[3]
            yield platform, 1

    def reducer_count_posts(self, platform, counts):
        yield platform, sum(counts)

if __name__ == '__main__':
    PostCount.run()
