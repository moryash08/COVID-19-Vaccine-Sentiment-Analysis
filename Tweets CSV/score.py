import pandas as pd
df = pd.read_csv('labelled_tweets_compiled.csv')
correct = 0
incorrect = 0
index = 0
# print(df.shape[0])

for i in range(0,1953):
    if(df.iloc[i]['sentiments'] == df.iloc[i]['sentiments_textblob']):
        correct = correct + 1
    else:
        incorrect = incorrect + 1
    index = i

print(index)
corr_per = ((correct)/(correct + incorrect))*100
print('VADER Accuracy Score : ' + str(corr_per))
print("Correct Labelled : ", correct)
print("Incorrect Labelled : ", incorrect)