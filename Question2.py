import pandas as pd

pfile = pd.read_csv('corona_tested_individuals_ver.csv')
# print(pfile)

# The auxiliary function is intended to facilitate and arrange the content of the work and its complexity

def Auxiliary_function(res, col, o_z):
    return sum(pfile.loc[((pfile['corona_result'] == res) & (pfile[col] == o_z)), [col]].count())


def positiveCought():
    cough_0 = Auxiliary_function('חיובי', 'cough', 0)
    cough_1 = Auxiliary_function('חיובי', 'cough', 1)
    return cough_0, cough_1


def negativeCought():
    cough_0 = Auxiliary_function('שלילי', 'cough', 0)
    cough_1 = Auxiliary_function('שלילי', 'cough', 1)
    return cough_0, cough_1


def cought():
    cough_1 = sum(positiveCought())
    cough_11 = sum(negativeCought())
    res1 = Auxiliary_function('חיובי', 'cough', 1) / cough_1
    res2 = Auxiliary_function('שלילי', 'cough', 1) / cough_11
    if (res1 > 0.7 and res2 < 0.3):
        return True
    return False


def positiveFever():
    fever_0 = Auxiliary_function('חיובי', 'fever', 0)
    fever_1 = Auxiliary_function('חיובי', 'fever', 1)
    return fever_0, fever_1


def negativeFever():
    fever_0 = Auxiliary_function('שלילי', 'fever', 0)
    fever_1 = Auxiliary_function('שלילי', 'fever', 1)
    return fever_0, fever_1


def fever():
    fever_0 = sum(positiveFever())
    fever_11 = sum(negativeFever())
    res1 = Auxiliary_function('חיובי', 'fever', 1) / fever_0
    res2 = Auxiliary_function('שלילי', 'fever', 1) / fever_11
    if (res1 > 0.7 and res2 < 0.3):
        return True
    return False


def positiveSore_throat():
    sore_throat_0 = Auxiliary_function('חיובי', 'sore_throat', 0)
    sore_throat_1 = Auxiliary_function('חיובי', 'sore_throat', 1)
    return sore_throat_0, sore_throat_1


def negativeSore_throat():
    sore_throat_0 = Auxiliary_function('שלילי', 'sore_throat', 0)
    sore_throat_1 = Auxiliary_function('שלילי', 'sore_throat', 1)
    return sore_throat_0, sore_throat_1


def sore_throat():
    sore_throat_0 = sum(positiveSore_throat())
    sore_throat_11 = sum(negativeSore_throat())
    res1 = Auxiliary_function('חיובי', 'sore_throat', 1) / sore_throat_0
    res2 = Auxiliary_function('שלילי', 'sore_throat', 1) / sore_throat_11
    if (res1 > 0.7 and res2 < 0.3):
        return True
    return False


def positiveShortness_of_breath():
    shortness_of_breath_0 = Auxiliary_function('חיובי', 'shortness_of_breath', 0)
    shortness_of_breath_1 = Auxiliary_function('חיובי', 'shortness_of_breath', 1)
    return shortness_of_breath_0, shortness_of_breath_1


def negativeShortness_of_breath():
    shortness_of_breate_0 = Auxiliary_function('שלילי', 'shortness_of_breath', 0)
    shortness_of_breat_1 = Auxiliary_function('שלילי', 'shortness_of_breath', 1)
    return shortness_of_breate_0, shortness_of_breat_1


def shortness_of_breath():
    shortness_of_breath_0 = sum(positiveShortness_of_breath())
    shortness_of_breath_11 = sum(negativeShortness_of_breath())
    res1 = Auxiliary_function('חיובי', 'shortness_of_breath', 1) / shortness_of_breath_0
    res2 = Auxiliary_function('שלילי', 'shortness_of_breath', 1) / shortness_of_breath_11
    if (res1 > 0.7 and res2 < 0.3):
        return True
    return False


def positiveHead_ache():
    head_ache_0 = Auxiliary_function('חיובי', 'head_ache', 0)
    head_ache_1 = Auxiliary_function('חיובי', 'head_ache', 1)
    return head_ache_0, head_ache_1


def negativeHead_ache():
    head_ache_0 = Auxiliary_function('שלילי', 'head_ache', 0)
    head_ache_1 = Auxiliary_function('שלילי', 'head_ache', 1)
    return head_ache_0, head_ache_1


def head_ache():
    head_ache_0 = sum(positiveHead_ache())
    head_ache_11 = sum(negativeHead_ache())
    res1 = Auxiliary_function('חיובי', 'head_ache', 1) / head_ache_0
    res2 = Auxiliary_function('שלילי', 'head_ache', 1) / head_ache_11
    if (res1 > 0.7 and res2 < 0.3):
        return True
    return False


def byGender():
    return "Number of sick female is: ", Auxiliary_function('חיובי', 'gender', 'נקבה'), \
           "Number of sick male is: ", Auxiliary_function('חיובי', 'gender', 'זכר'), \
           "Number of healthy female is: ", Auxiliary_function('שלילי', 'gender', 'נקבה'), \
           "Number of healthy male is: ", Auxiliary_function('שלילי', 'gender', 'זכר')


def byAge_60_and_above():
    return "Number of sick age 60 and above: ", Auxiliary_function('חיובי', 'age_60_and_above', 'Yes'), \
           "Number of healthy age 60 and above: ", Auxiliary_function('שלילי', 'age_60_and_above', 'Yes')


def information():
    result_with_cough = \
        pfile.loc[
            ((pfile["age_60_and_above"] == "Yes") & (pfile["gender"] == "זכר") & (pfile["corona_result"] == "שלילי")
             & (pfile["cough"] == 1))].count()["cough"]
    result_with_cough = "--> Result with cough:", result_with_cough

    result_with_fever = \
        pfile.loc[
            ((pfile["age_60_and_above"] == "Yes") & (pfile["gender"] == "זכר") & (pfile["corona_result"] == "שלילי")
             & (pfile["fever"] == 1))].count()["fever"]
    result_with_fever = "--> Result with fever:", result_with_fever

    result_with_sore_throat = \
        pfile.loc[
            ((pfile["age_60_and_above"] == "Yes") & (pfile["gender"] == "זכר") & (pfile["corona_result"] == "שלילי")
             & (pfile["sore_throat"] == 1))].count()["sore_throat"]
    result_with_sore_throat = "--> Result with sore throat:", result_with_sore_throat

    result_with_shortness_of_breath = \
        pfile.loc[
            ((pfile["age_60_and_above"] == "Yes") & (pfile["gender"] == "זכר") & (pfile["corona_result"] == "שלילי")
             & (pfile["shortness_of_breath"] == 1))].count()["shortness_of_breath"]
    result_with_shortness_of_breath = "--> Result with shortness of breath:", result_with_shortness_of_breath

    result_with_head_ache = \
        pfile.loc[
            ((pfile["age_60_and_above"] == "Yes") & (pfile["gender"] == "זכר") & (pfile["corona_result"] == "שלילי")
             & (pfile["head_ache"] == 1))].count()["head_ache"]
    result_with_head_ache = "--> Result with head ache:", result_with_head_ache
    return result_with_cough, result_with_fever, result_with_sore_throat, \
           result_with_shortness_of_breath, result_with_head_ache


switcher = {
    1: positiveCought,
    2: negativeCought,
    3: cought,
    4: positiveFever,
    5: negativeFever,
    6: fever,
    7: positiveSore_throat,
    8: negativeSore_throat,
    9: sore_throat,
    10: positiveShortness_of_breath,
    11: negativeShortness_of_breath,
    12: shortness_of_breath,
    13: positiveHead_ache,
    14: negativeHead_ache,
    15: head_ache,
    16: byGender,
    17: byAge_60_and_above,
    18: information
}


def switch_demo(argument=int(input("Enter number: "))):
    func = switcher.get(argument)
    return func()


print(switch_demo())
