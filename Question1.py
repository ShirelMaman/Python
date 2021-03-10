import pandas as pd

pfile = pd.read_csv('Shirel&Matan.csv', index_col='id')
# print(pfile)

def averageByProfession():
    avg = pfile.mean()
    return avg


def bestGrade():
    col = pfile.loc[:, 'java':'phisics']
    maxG = col.max()
    return maxG


def id():
    fail = pfile[pfile['java'] <= 59]
    return fail.index


def programingAverage():
    pfile['programingAverage'] = (pfile['java'] + pfile['python']) / 2
    return pfile


def idProgramingAverage():
    pfile2 = programingAverage()
    agv = pfile2.loc[:, 'programingAverage'].max()
    agv_max = pfile2.loc[(pfile2['programingAverage'] == agv), ['programingAverage']]
    return agv_max


def mpAverage():
    pfile['mathPhisicsAverage'] = (pfile['math'] + pfile['phisics']) / 2
    return pfile


def weightedAverage():
    pfile2 = programingAverage()
    pfile2 = mpAverage()
    pfile2['WeightedAverage'] = pfile2['programingAverage'] * 0.7 + pfile2['mathPhisicsAverage'] * 0.3
    return pfile2


def sortWeightedAverage():
    pfile3 = weightedAverage()
    sort_col = pfile3.groupby(['WeightedAverage']).min()
    return sort_col


def jmGrades():
    id = pfile.loc[(pfile['java'] > 80) & (pfile['math'] < 70), :]
    return id.index


def averageByStudent():
    pfile['average'] = (pfile['java'] + pfile['python'] + pfile['math'] + pfile['phisics']) / 4
    return pfile


def averageByRegion():
    pfile2 = averageByStudent()
    agv_region = pfile2.groupby('region').average.mean()
    return agv_region


def averageByGender():
    pfile2 = averageByStudent()
    agv_gender = pfile2.groupby('gander').average.mean()
    best = agv_gender.nlargest(1)
    return agv_gender, best


switcher = {
    1: averageByProfession,
    2: bestGrade,
    3: id,
    4: programingAverage,
    5: idProgramingAverage,
    6: mpAverage,
    7: weightedAverage,
    8: sortWeightedAverage,
    9: jmGrades,
    10: averageByStudent,
    11: averageByRegion,
    12: averageByGender
}


def switch_demo(argument=int(input("Enter number: "))):
    func = switcher.get(argument)
    return func()


print(switch_demo())
