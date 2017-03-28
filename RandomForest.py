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
    final_df.to_csv("output/" + parameter1 + ".csv",index_label="id")


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
        final_dict[key] = {}

        for id in answer[key]:
            final_dict[key][id] = answer[key].count(id) * 100.00 / len(answer[key])

    final_df = pd.DataFrame(final_dict)
    # print final_df
    final_df.to_csv("output/" + parameter2 + ".csv",index_label="id")


def get_popularity(no):
    if 0.0 <= no < 1.5:
        return 1.0
    elif 1.5 <= no < 2:
        return 1.5
    elif 2 <= no < 2.5:
        return 2.0
    elif 2.5 <= no < 3.0:
        return 2.5
    elif 3.0 <= no < 3.5:
        return 3.0
    elif 3.5 <= no < 4.0:
        return 3.5
    elif 4.0 <= no < 4.5:
        return 4.0
    elif 4.5 <= no < 5.0:
        return 4.5
    else:
        return 5


def create_param3_table(param3_series, candidate_series):
    answer = {}

    for i in range(len(param3_series)):
        vote_avg = get_popularity(float(param3_series[i]))
        if vote_avg not in answer:
            answer[vote_avg] = []
        answer[vote_avg].append(candidate_series[i])

    final_dict = {}
    for key in answer.keys():
        final_dict[key] = {}

        for id in answer[key]:
            final_dict[key][id] = answer[key].count(id) * 100.00 / len(answer[key])

    final_df = pd.DataFrame(final_dict)
    # print final_df
    final_df.to_csv("output/" + parameter3 + ".csv",index_label="id")


def get_vote_avg(no):
    if 0.0 <= no <= 3.0:
        return "Bad"
    elif 3.0 <= no <= 5.0:
        return "Average"
    elif 5.0 <= no <= 7.0:
        return "Good"
    else:
        return "Great"


def create_param4_table(param4_series, candidate_series):
    answer = {"Bad": [], "Average": [], "Good": [], "Great": []}

    for i in range(len(param4_series)):
        vote_avg = get_vote_avg(float(param4_series[i]))
        answer[vote_avg].append(candidate_series[i])

    final_dict = {}
    for key in answer.keys():
        final_dict[key] = {}

        for id in answer[key]:
            final_dict[key][id] = answer[key].count(id) * 100.00 / len(answer[key])

    final_df = pd.DataFrame(final_dict)
    # print final_df
    final_df.to_csv("output/" + parameter4 + ".csv",index_label="id")


if __name__ == "__main__":
    # data = pd.read_csv("input/raw_data.csv")

    # data.dropna().to_csv("clean_data.csv", index=False)
    clean_data = pd.read_csv("input/clean_data.csv")

    create_param1_table(clean_data[parameter1], clean_data[candidate_param])
    create_param2_table(clean_data[parameter2], clean_data[candidate_param])
    create_param3_table(clean_data[parameter3], clean_data[candidate_param])
    create_param4_table(clean_data[parameter4], clean_data[candidate_param])

    #  print clean_data
