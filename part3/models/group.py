import enums


class Group:
    def __init__(self, args) -> None:
        self.id          = args[enums.GROUP_ID_FIELD]
        self.name        = args[enums.GROUP_NAME_FIELD]
        self.activity    = args[enums.GROUP_ACTIVITY_FIELD]
        self.description = args[enums.GROUP_DESCRIPTION_FIELD]
        self.counters    = args[enums.GROUP_COUNTERS_FIELD]
        self.status      = args[enums.GROUP_STATUS_FIELD]

    def get_data_args(self):
        args = [self.id, self.activity, self.description]
        counters_args = self.get_counters_data()

        return args + counters_args + [self.status]


    def get_counters_data(self):
        counters = {
            enums.COUNTER_AUDIOS: 0,
            enums.COUNTER_PHOTOS: 0,
            enums.COUNTER_VIDEOS: 0,
            enums.COUNTER_ALBUMS: 0,
            enums.COUNTER_TOPICS: 0,
            enums.COUNTER_DOCS:   0,
        }

        if self.counters is None or len(self.counters) == 0:
            return list(counters.values())

        for key, value in self.counters.items():
            if enums.counters.get(key, False) is not False:
                counters[key] = value
        
        return list(counters.values())
