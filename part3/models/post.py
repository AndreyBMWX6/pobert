import enums


class Post:
    def __init__(self, args) -> None:
        self.id            = args[enums.POST_ID_FIELD]
        self.text          = args[enums.POST_TEXT_FIELD]
        self.attachments   = args[enums.POST_ATTACHMENTS_FIELD]
        self.marked_as_ads = args[enums.POST_MARKED_AS_ADS_FIELD]
        self.postponed     = args[enums.POST_POSTPONED_FIELD] is not None

    def get_data_args(self):
        args = [self.id, self.text]
        attach_args = self.get_attachments_data()

        return args + attach_args + [self.postponed]

    def get_attachments_data(self):
        counters = {
            enums.TYPE_AUDIO: 0,
            enums.TYPE_PHOTO: 0,
            enums.TYPE_VIDEO: 0,
            enums.TYPE_DOC:   0,
            enums.TYPE_LINK:  0,
            enums.TYPE_NOTE:  0,
            enums.TYPE_ALBUM: 0,
        }

        for attach in self.attachments:
            attach_type = attach["type"]
            if enums.data_types.get(attach_type, False) is not False:
                counters[attach_type] += 1
                
        return list(counters.values())

    def is_advertisment(self):
        return self.marked_as_ads == 1

