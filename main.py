import pandas as pd

# 데이터 로드
title_basics = pd.read_csv('C:/Users/2446_/PycharmProjects/PythonProject/tsv/title.basics.tsv', sep='\t', low_memory=False)
#Index(['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession','knownForTitles'], dtype='object')
title_ratings = pd.read_csv('C:/Users/2446_/PycharmProjects/PythonProject/tsv/title.ratings.tsv', sep='\t', low_memory=False)
#Index(['tconst', 'averageRating', 'numVotes'], dtype='object')

# 'tconst'를 기준으로 두 데이터셋을 병합
merged_data = pd.merge(title_basics, title_ratings, on='tconst')

# 결과 확인
print(merged_data.head(10))
