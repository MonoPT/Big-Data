import sparknlp

class LoadData:
    def __init__(self, path: str):
        self.spark = sparknlp.start()

        self.application_categories = spark.read.csv('/content/data/application_categories.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.application_developers = spark.read.csv('/content/data/application_developers.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.application_genres = spark.read.csv('/content/data/application_genres.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.application_platforms = spark.read.csv('/content/data/application_platforms.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.application_publishers = spark.read.csv('/content/data/application_publishers.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.applications = spark.read.csv('/content/data/applications.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.categories = spark.read.csv('/content/data/categories.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.developers = spark.read.csv('/content/data/developers.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.genres = spark.read.csv('/content/data/genres.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.platforms = spark.read.csv('/content/data/platforms.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.publishers = spark.read.csv('/content/data/publishers.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.reviews = spark.read.csv('/content/data/reviews.csv', header=True, inferSchema=True, multiLine=True, escape='"')