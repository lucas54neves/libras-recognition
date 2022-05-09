from constants import COMPLETE_FINGER_LIST


def check_letter(list_markings):
    """
    Function that check a letter by finger positions.
    """
    for _ in COMPLETE_FINGER_LIST:
        # x_20 = list_markings[20][1]
        # x_19 = list_markings[19][1]
        # x_18 = list_markings[18][1]
        # x_17 = list_markings[17][1]
        # x_16 = list_markings[16][1]
        # x_15 = list_markings[15][1]
        # x_14 = list_markings[14][1]
        # x_13 = list_markings[13][1]
        # x_12 = list_markings[12][1]
        # x_11 = list_markings[11][1]
        # x_10 = list_markings[10][1]
        # x_9 = list_markings[9][1]
        # x_8 = list_markings[8][1]
        # x_7 = list_markings[7][1]
        # x_6 = list_markings[6][1]
        x_5 = list_markings[5][1]
        x_4 = list_markings[4][1]
        # x_3 = list_markings[3][1]
        # x_2 = list_markings[2][1]
        # x_1 = list_markings[1][1]
        # x_0 = list_markings[0][1]

        y_20 = list_markings[20][2]
        y_19 = list_markings[19][2]
        y_18 = list_markings[18][2]
        y_17 = list_markings[17][2]
        y_16 = list_markings[16][2]
        y_15 = list_markings[15][2]
        y_14 = list_markings[14][2]
        y_13 = list_markings[13][2]
        y_12 = list_markings[12][2]
        y_11 = list_markings[11][2]
        y_10 = list_markings[10][2]
        y_9 = list_markings[9][2]
        y_8 = list_markings[8][2]
        y_7 = list_markings[7][2]
        y_6 = list_markings[6][2]
        y_5 = list_markings[5][2]
        y_4 = list_markings[4][2]
        # y_3 = list_markings[3][2]
        # y_2 = list_markings[2][2]
        # y_1 = list_markings[1][2]
        # y_0 = list_markings[0][2]

        if y_8 > y_5 > y_4 and y_12 > y_9 and y_16 > y_13 and y_20 > y_17:
            return "A"

        if (
            y_8 < y_7 < y_6 < y_5 < y_4
            and y_12 < y_11 < y_10 < y_9
            and y_16 < y_15 < y_14 < y_13
            and y_20 < y_19 < y_18 < y_17
            and x_4 > x_5
        ):
            return "B"

        return ""
