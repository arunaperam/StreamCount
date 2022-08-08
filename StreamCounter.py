import datetime
from datetime import timedelta
from MessageGenerator import create_messages


def round_to_hour(s_dt,e_dt):
    """
    rounding the datetimes to the nearst hours.
    for start_time, if the video started after the nth hour, will be rounded to upper hour
    example: start_time '2022-08-12 07:35:00' will be rounded to '2022-08-12 08:00:00'
    for end_time ,if the video ended before nth hour,will rounding down to lower hour
    example: end_time '2022-08-12 11:30:00' will be rounded to  '2022-08-12 11:00:00'
    :param s_dt: start time
    :param e_dt: end time
    :yields: yields list of start_time and end_time for each video
    """

    dt_start_of_hour_s = s_dt.replace(minute=0, second=0, microsecond=0)
    dt_start_of_hour_e =e_dt.replace(minute=0, second=0, microsecond=0)

    if s_dt > dt_start_of_hour_s:
        # round up
        s_dt = dt_start_of_hour_s + datetime.timedelta(hours=1)

    if e_dt > dt_start_of_hour_e:
        # round down
        e_dt = dt_start_of_hour_e
    yield [s_dt,e_dt]


def get_max_value(time_dict):
    """
    this function returns the final result of max video count
    :param time_dict: final dictionary to count the max number videos at an instance
    :return: max count
    """
    return max(time_dict.values())


def generate_hours_dict(rounded_list):
    """
    example output format : {datetime:count}  {'2022-08-09 11:00:00': 2}
    :param rounded_list:this is a list of start and end times for each video rounded to nearest hours
    :return: a dictionary with datetimes as key and count as value
    """
    time_dict={}
    for i in rounded_list:
        start = i[0]
        end = i[1]
        while start <= end:
            if start not in time_dict:
                time_dict[start] = 1
            else:
                time_dict[start] = time_dict[start]+1
            start += timedelta(hours=1)
    return time_dict


if __name__ == '__main__':
    # step 1: get video stream data
    videostream = create_messages()
    # step 2: rounding start_time and end_time to the nearest hours
    rounded_list = []
    for i in videostream.VideoPlay:
        # step 3: convert strings to datetime
        start_time = datetime.datetime.strptime(i.start_time, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.datetime.strptime(i.end_time, '%Y-%m-%d %H:%M:%S')
        for i in round_to_hour(start_time, end_time):
            rounded_list.append(i)
    # step 3: converting and expanding the rounded hours as dictionary by assigning value for each hour
    time_dict = generate_hours_dict(rounded_list)
    # step 4: get the final max count of concurrent videos .
    max_video_count = get_max_value(time_dict)
    # just adding this print statements for demonstration purposes,will be using log statements in production.
    print(time_dict)
    print(max_video_count)






