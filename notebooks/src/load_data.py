import sparknlp
from pyspark.sql import SparkSession

class LoadData:
    def __init__(self, path: str):
        self.spark = SparkSession.getActiveSession()

        if spark is None:
            # Nenhuma sessão ativa, criar uma nova
            self.spark = sparknlp.start()
        
        self.application_categories = self.spark.read.csv(f'/content/data/application_categories.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.application_developers = self.spark.read.csv('/content/data/application_developers.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.application_genres = self.spark.read.csv('/content/data/application_genres.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.application_platforms = self.spark.read.csv('/content/data/application_platforms.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.application_publishers = self.spark.read.csv('/content/data/application_publishers.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.applications = self.spark.read.csv('/content/data/applications.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.categories = self.spark.read.csv('/content/data/categories.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.developers = self.spark.read.csv('/content/data/developers.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.genres = self.spark.read.csv('/content/data/genres.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.platforms = self.spark.read.csv('/content/data/platforms.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.publishers = self.spark.read.csv('/content/data/publishers.csv', header=True, inferSchema=True, multiLine=True, escape='"')
        self.reviews = self.spark.read.csv('/content/data/reviews.csv', header=True, inferSchema=True, multiLine=True, escape='"')