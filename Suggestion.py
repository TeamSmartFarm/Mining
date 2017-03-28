import pandas as pd

parameter1 = "release_date"
parameter2 = "genre_ids"
parameter3 = "popularity"
parameter4 = "vote_average"
candidate_param = "id"

all_param_result = pd.DataFrame()


def init_dataframe():
    df = pd.read_csv("output/" + parameter1 + ".csv")
    global all_param_result
    all_param_result = pd.DataFrame(columns=df["id"], index=[parameter1, parameter2, parameter3, parameter4,"average"])


def add_param1(param1):
    df = pd.read_csv("output/" + parameter1 + ".csv")
    global all_param_result
    all_param_result.loc[parameter1] = list(df[param1])
    # print all_param_result


def add_param2(param2):
    df = pd.read_csv("output/" + parameter2 + ".csv")
    global all_param_result
    all_param_result.loc[parameter2] = list(df[param2])
    # print all_param_result


def add_param3(param3):
    df = pd.read_csv("output/" + parameter3 + ".csv")
    global all_param_result
    all_param_result.loc[parameter3] = list(df[param3])
    # print all_param_result


def add_param4(param4):
    df = pd.read_csv("output/" + parameter4 + ".csv")
    global all_param_result
    all_param_result.loc[parameter4] = list(df[param4])
    # print all_param_result


def find_average():
    global all_param_result
    avg_list = []
    for col_name in all_param_result.columns.values:
        avg_list.append(all_param_result[col_name].sum() / 4)
    all_param_result.loc["average"] = avg_list


if __name__ == "__main__":
    param1, param2, param3, param4 = raw_input("Enter The 4 Parameter Value").split()
    # print param1, param2, param3, param4
    # Q1 35.0 2.0 Great

    init_dataframe()
    add_param1(param1)
    add_param2(param2)
    add_param3(param3)
    add_param4(param4)

    global all_param_result
    all_param_result.fillna(0, inplace=True)
    find_average()

    suggestion_list =  all_param_result.columns[all_param_result.ix[all_param_result.last_valid_index()].argsort()[::-1]]
    # all_param_result.sort(columns=["average"],axis=1,inplace=True)

    print suggestion_list[:10]
    all_param_result.to_csv("Save.csv")
