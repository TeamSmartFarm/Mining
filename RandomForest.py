import pandas as pd

parameter1 = "release_date"
parameter2 = "genre_ids"
parameter3 = "popularity"
parameter4 = "vote_average"
candidate_param = "id"


def get_quarter(no):
    if 1 <= no <= 4:
        return "Q1"
    elif 5 <= no <= 8:
        return "Q2"
    else:
        return "Q3"


def create_param1_table(param1_series, candidate_series):
    answer = {"Q1": [], "Q2": [], "Q3": []}

    for i in range(len(param1_series)):
        month = str(param1_series[i]).split("/")[0]
        quarter = get_quarter(int(month))
        answer[quarter].append(candidate_series[i])

    final_dict = {"Q1": {}, "Q2": {}, "Q3": {}}
    for q in range(1, 4):
        quarter_no = "Q" + str(q)
        total_length = len(answer[quarter_no])
        for item in answer[quarter_no]:
            final_dict[quarter_no][item] = (answer[quarter_no].count(item) * 100.00) / total_length

    final_df = pd.DataFrame(final_dict)
    # print final_df
    final_df.to_csv("output/" + parameter1 + ".csv")


def create_param2_table(param2_series, candidate_series):
    answer = {}
    index = 0

    for item in param2_series:
        if item not in answer:
            answer[item] = []
        answer[item].append(candidate_series[index])
        index += 1

    final_dict = {}
    for key in answer.keys():
        final_dict[key]={}

        for id in answer[key]:
            final_dict[key][id] = answer[key].count(id)*100.00/len(answer[key])

    final_df = pd.DataFrame(final_dict)
    #print final_df
    final_df.to_csv("output/" + parameter2 + ".csv")


if __name__ == "__main__":
    data = pd.read_csv("raw_data.csv")

    data.dropna().to_csv("clean_data.csv", index=False)
    clean_data = pd.read_csv("clean_data.csv")

    # create_param1_table(clean_data[parameter1], clean_data[candidate_param])
    create_param2_table(clean_data[parameter2], clean_data[candidate_param])

    #  print clean_data
