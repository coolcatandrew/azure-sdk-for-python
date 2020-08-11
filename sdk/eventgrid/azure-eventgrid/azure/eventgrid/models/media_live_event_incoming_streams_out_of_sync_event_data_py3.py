# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MediaLiveEventIncomingStreamsOutOfSyncEventData(Model):
    """Incoming streams out of sync event data.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar min_last_timestamp: Gets the minimum last timestamp received.
    :vartype min_last_timestamp: str
    :ivar type_of_stream_with_min_last_timestamp: Gets the type of stream with
     minimum last timestamp.
    :vartype type_of_stream_with_min_last_timestamp: str
    :ivar max_last_timestamp: Gets the maximum timestamp among all the tracks
     (audio or video).
    :vartype max_last_timestamp: str
    :ivar type_of_stream_with_max_last_timestamp: Gets the type of stream with
     maximum last timestamp.
    :vartype type_of_stream_with_max_last_timestamp: str
    :ivar timescale_of_min_last_timestamp: Gets the timescale in which
     "MinLastTimestamp" is represented.
    :vartype timescale_of_min_last_timestamp: str
    :ivar timescale_of_max_last_timestamp: Gets the timescale in which
     "MaxLastTimestamp" is represented.
    :vartype timescale_of_max_last_timestamp: str
    """

    _validation = {
        'min_last_timestamp': {'readonly': True},
        'type_of_stream_with_min_last_timestamp': {'readonly': True},
        'max_last_timestamp': {'readonly': True},
        'type_of_stream_with_max_last_timestamp': {'readonly': True},
        'timescale_of_min_last_timestamp': {'readonly': True},
        'timescale_of_max_last_timestamp': {'readonly': True},
    }

    _attribute_map = {
        'min_last_timestamp': {'key': 'minLastTimestamp', 'type': 'str'},
        'type_of_stream_with_min_last_timestamp': {'key': 'typeOfStreamWithMinLastTimestamp', 'type': 'str'},
        'max_last_timestamp': {'key': 'maxLastTimestamp', 'type': 'str'},
        'type_of_stream_with_max_last_timestamp': {'key': 'typeOfStreamWithMaxLastTimestamp', 'type': 'str'},
        'timescale_of_min_last_timestamp': {'key': 'timescaleOfMinLastTimestamp', 'type': 'str'},
        'timescale_of_max_last_timestamp': {'key': 'timescaleOfMaxLastTimestamp', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(MediaLiveEventIncomingStreamsOutOfSyncEventData, self).__init__(**kwargs)
        self.min_last_timestamp = None
        self.type_of_stream_with_min_last_timestamp = None
        self.max_last_timestamp = None
        self.type_of_stream_with_max_last_timestamp = None
        self.timescale_of_min_last_timestamp = None
        self.timescale_of_max_last_timestamp = None