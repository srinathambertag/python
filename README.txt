# import csv
import git
import pandas as pd
from pcardext import cd
from sqlalchemy import create_engine, types

git_dir = "https://github.com/srinathrajath/python.git"
g = git.cmd.Git(git_dir)
g.pull('origin', 'main')
print('Code pulled')

engine = create_engine('mysql://root:password@localhost/movies')
df = pd.read_csv("/home/srinath/Documents/data.csv", sep=',', quotechar='\'', encoding='utf8')
df.to_sql('movies', con=engine, index=False, if_exists='append')
print('Data Dump Completed')
