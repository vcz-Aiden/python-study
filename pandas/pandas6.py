import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

def curTime_categorize(curTime) :
    if math.isnan(curTime) :
        return -1
    return math.floor(curTime / 100) * 100

if __name__ == "__main__" :
    data = pd.read_csv('./train.csv', sep=",", index_col=0)  #, usecols=['playbackTime'])
    print(data)

    print(data.info())
    print(data.isna())

    print(data.dropna(subset=['curHP', 'maxHP']))
    print(data.dropna(axis=1))

    print(data['curHP'].fillna(data['curHP'].mean()))

    print(data[data['isDead'] == False]['curHP'].mean())
    print(data[data['isDead'] == True]['curHP'].mean())

    data.loc[data['isDead'] == False, 'curHP'] = data['curHP'].fillna(data[data['isDead'] == False]['curHP'].mean())

    print(data.info())
    data['playbackTime'] = data['playbackTime'].astype(str)
    print(data.info())

    data['curTime'] = data['curTime'].apply(curTime_categorize)
    print(data)

    print(pd.get_dummies(data, columns=['curTime'], drop_first=True))

    class_group = data.groupby('curTime')
    print(class_group.groups)

    print(class_group.count())
    print(class_group.sum())
    print(class_group.mean())
    print(class_group.min())

    test_group = data.groupby(['curTime', "isDead"])
    print(test_group.mean().loc[(100, True)])
    print(test_group.mean()['curHP'])

    print(data.set_index('curTime'))
    print(data.set_index(['curTime', 'isDead']))
    print(data.set_index(['curTime', 'isDead']).reset_index())

    print(data.set_index('curTime').groupby(level=0).mean())
    print(data.set_index('curTime').groupby(curTime_categorize).mean())

    print(data.set_index(['curTime', 'isDead']).groupby(level=[0, 1]).mean())
    print(data.set_index(['curTime', 'isDead']).groupby(level=[0, 1]).aggregate([np.mean, np.sum, np.max]))

    print(data.groupby('curTime').transform(np.mean)['curHP'])
    data['transform'] = data.groupby(['curTime', 'isDead']).transform(np.mean)['curHP']
    print(data)

    print(data.pivot('playbackTime', 'isDead', 'transform'))
    print(pd.pivot_table(data, index='curTime', columns='isDead', aggfunc=np.mean))

    #stack and unstack
    stack_data = data.set_index(['curTime', 'playbackTime'])

    print(stack_data)
    print(stack_data.unstack(level=1))
    print(stack_data.unstack(level=1).stack(0))