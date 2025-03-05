# -*- coding:utf-8 -*-
##############################################################
# Author: Fang (Alicia) Tang
# Email: fangt@asu.edu
# Date: 03/04/2025
##############################################################


import pandas as pd

path_in = "./inputs/berlin-center_trips.tntp"


def read_tntp_file(path_in: str) -> pd.DataFrame:
    # read tntp file
    with open(path_in, "r") as f:
        data_tntp = f.readlines()

    # delete empty lines
    data_without_empty_lines = [line for line in data_tntp if line != "\n"]

    # replace "\t" with ""  and ";" with "," for each line of data
    data_replaced = [line.replace(" \t", "").replace(";", ",") if "\t" in line else line for line in data_without_empty_lines]

    # prepare final list
    final_list = []
    col_name = ["o_zone_id", "d_zone_id", "volume"]

    for line in data_replaced:
        if "," not in line:
            # get o id
            o_id = line.split(" ")[1]
        else:
            # get d ind and value
            d_and_volume = line.split(",")
            for volume in d_and_volume:
                if volume != "\n":
                    d_id = volume.split(":")[0]
                    volume_val = volume.split(":")[1]
                    final_list.append([o_id, d_id, volume_val])

    # convert to dataframe
    df_tntp = pd.DataFrame(final_list, columns=col_name)

    df_tntp.to_csv("./outputs/demand.csv", index=False)

    return df_tntp


if __name__ == "__main__":
    read_tntp_file(path_in)
