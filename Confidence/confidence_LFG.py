import openai
import pandas as pd
import math
import numpy as np
import itertools
import warnings
import re

# 禁止显示所有警告
warnings.filterwarnings('ignore')

openai.api_key = "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"

def contains_characters(string,t_ans):
    if re.search(t_ans, string, re.IGNORECASE):
        return True
    else:
        return False

def confidence(text):
  response1 = []
  score = []
  count = 1
  while count <= 10:
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=text,
      temperature=1,
      max_tokens=100,
      logprobs=3,
      top_p = 1)
    response1.append(response.choices[0].text.strip())
    logits = sum(response['choices'][0]['logprobs']['token_logprobs'])/max(1,len(response['choices'][0]['logprobs']['token_logprobs']))
    score.append(logits)
    count += 1
  df = pd.DataFrame({'Answer': response1, 'Score': score})
  grouped = df.groupby('Answer')
  min_values = grouped['Score'].max().reset_index(name='HigestValue')
  min_values['Count'] = grouped['Score'].count().reset_index(name='Count')['Count']
  min_values = min_values.sort_values(by=['Count', 'HigestValue'], ascending=[False, False]).head(4)
  min_values['confidence'] = 0
  for index, value in min_values.iterrows():
      min_values['confidence'].loc[index]= np.e**(min_values['HigestValue'].loc[index])/sum(np.e**(min_values['HigestValue']))
  return min_values

df = pd.read_csv('CARE-MI-10.csv')
for i,value in df.iterrows():  
    result = confidence(df['LFG'].loc[i])
    print(result)
    ll = result.groupby('Answer').sum().sort_values(by=['confidence'], ascending=False).reset_index()[['Answer','confidence']]
    print(ll)
    df['LFG_L'].loc[i] = ll['Answer'].loc[0]
    df['LFG_C'].loc[i] = ll['confidence'].loc[0]
    df.to_csv('CARE-MI-10.csv',index = False,encoding='utf_8_sig')
    