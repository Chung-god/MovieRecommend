import pandas as pd
from pyspark.sql import SparkSession

# Spark 세션 시작
spark = SparkSession.builder.appName("MovieRecommendation").getOrCreate()

# 데이터 불러오기
ratings_df = spark.read.csv("C:/Users/2446_/PycharmProjects/PythonProject/tsv/title.ratings.tsv", sep="\t", header=True, inferSchema=True)
basics_df = spark.read.csv("C:/Users/2446_/PycharmProjects/PythonProject/tsv/title.basics.tsv", sep="\t", header=True, inferSchema=True)

# 필요한 열만 선택
ratings_df = ratings_df.select("tconst", "averageRating", "numVotes")
basics_df = basics_df.select("tconst", "primaryTitle", "genres")

ratings_df.show(5)
basics_df.show(5)
