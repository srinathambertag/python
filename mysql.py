import git
import pandas as pd
from sqlalchemy import create_engine, types


# Pull Code
repo = git.Repo('../python')
git_dir = "https://github.com/srinathrajath/python.git"
g = git.cmd.Git(git_dir)
g.pull('origin', 'main')
print('Code pulled')

# Dump Data
engine = create_engine('mysql://admin:Admin@123@54.158.102.120/films')
df = pd.read_csv("/home/srinath/PycharmProjects/Mysql Dump/python/data.csv", sep=',', quotechar='\'', encoding='utf8')
df.to_sql('movies', con=engine, index=False, if_exists='replace')
print('Data Dump Completed')

# Push Code
repo.index.add("data.csv")
repo.index.commit('Initial commit.')
print('code commited')
print(repo.remotes.origin.push())
