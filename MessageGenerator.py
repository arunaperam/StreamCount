import VideoPlay_pb2

def create_messages():
    """
    This is to create a video stream data in the protobuf format with start_time and end_time
    :return: a videostream with set of protobuf messages
    """
    # step1: creating video stream with the Generated protocol buffer
    videostream = VideoPlay_pb2.stream()

    # step2: adding messages
    t1 = videostream.VideoPlay.add()
    t1.start_time = '2022-08-12 09:00:00'
    t1.end_time = '2022-08-12 10:00:00'

    t2 = videostream.VideoPlay.add()
    t2.start_time = '2022-08-12 07:35:00'
    t2.end_time = '2022-08-12 09:00:00'

    t3 = videostream.VideoPlay.add()
    t3.start_time = '2022-08-12 09:15:00'
    t3.end_time = '2022-08-12 11:00:00'

    t4 = videostream.VideoPlay.add()
    t4.start_time = '2022-08-12 09:30:00'
    t4.end_time = '2022-08-12 11:30:00'

    t5 = videostream.VideoPlay.add()
    t5.start_time = '2022-08-12 06:00:00'
    t5.end_time = '2022-08-12 08:00:00'

    return videostream


