import enums


class Data:
    def __init__(self, args) -> None:
        # post id
        self.post_id           = args[enums.DATA_POST_ID]
        # post fields
        self.post_text      = args[enums.DATA_POST_TEXT]
        self.post_audios    = args[enums.DATA_POST_ATTACHMENTS_AUDIOS]
        self.post_photos    = args[enums.DATA_POST_ATTACHMENTS_PHOTOS]
        self.post_videos    = args[enums.DATA_POST_ATTACHMENTS_VIDEOS]
        self.post_docs      = args[enums.DATA_POST_ATTACHMENTS_DOCS]
        self.post_links     = args[enums.DATA_POST_ATTACHMENTS_LINKS]
        self.post_notes     = args[enums.DATA_POST_ATTACHMENTS_NOTES]
        self.post_albums    = args[enums.DATA_POST_ATTACHMENTS_ALBUMS]
        self.post_postponed = args[enums.DATA_POST_POSTPONED_FIELD]
        # group fields
        self.group_id          = args[enums.DATA_GROUP_ID_FIELD]
        self.group_activity    = args[enums.DATA_GROUP_ACTIVITY_FIELD]
        self.group_description = args[enums.DATA_GROUP_DESCRIPTION_FIELD]
        self.group_audios      = args[enums.DATA_GROUP_COUNTERS_AUDIOS]
        self.group_photos      = args[enums.DATA_GROUP_COUNTERS_PHOTOS]
        self.group_videos      = args[enums.DATA_GROUP_COUNTERS_VIDEOS]
        self.group_albums      = args[enums.DATA_GROUP_COUNTERS_ALBUMS]
        self.group_topics      = args[enums.DATA_GROUP_COUNTERS_TOPICS]
        self.group_docs        = args[enums.DATA_GROUP_COUNTERS_DOCS]
        self.group_status      = args[enums.DATA_GROUP_STATUS_FIELD]

    def get_args(self):
        return [self.post_id, self.post_text, self.post_audios, self.post_photos, self.post_videos, 
                self.post_docs, self.post_links, self.post_notes, self.post_albums, self.post_postponed,
                self.group_id, self.group_activity, self.group_description, self.group_audios, self.group_photos, 
                self.group_videos, self.group_albums, self.group_topics, self.group_docs, self.group_status]
