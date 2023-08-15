classes = ['0.Музыка', '1.Фотографии', '2.Книги', '3.Фильмы']

dataset_columns = ['post_id', 'class', 'group_activity', 'group_audios', 'group_photos',
                                        'group_videos', 'group_albums', 'group_topics', 'group_docs',
                                        'post_audios', 'post_photos', 'post_videos', 'post_docs', 'post_links', 'post_notes', 
                                        'post_albums', 'post_postponed', 'group_description', 'group_status', 'post_text']

data_args_columns = ['post_id', 'post_text', 'post_audios', 'post_photos', 'post_videos',
                     'post_docs', 'post_links', 'post_notes', 'post_albums', 'post_postponed',
                     'group_id', 'group_activity', 'group_description', 'group_audios', 'group_photos',
                     'group_videos', 'group_albums', 'group_topics', 'group_docs', 'group_status']

data_not_numeric_args = ['post_id', 'post_text', 'group_id', 'group_activity', 'group_description', 'group_status']

post_post_key = 'items'
post_group_key = 'groups'

group_fields = ['id', 'name', 'activity', 'description', 'counters', 'status']

# Group fields enum
GROUP_ID_FIELD = 0
GROUP_NAME_FIELD = 1
GROUP_ACTIVITY_FIELD = 2
GROUP_DESCRIPTION_FIELD = 3
GROUP_COUNTERS_FIELD = 4
GROUP_STATUS_FIELD = 5

post_fields = ['id', 'text', 'attachments', 'marked_as_ads', 'postponed_id']

# Post fields enum
POST_ID_FIELD = 0
POST_TEXT_FIELD = 1
POST_ATTACHMENTS_FIELD = 2
POST_MARKED_AS_ADS_FIELD = 3
POST_POSTPONED_FIELD = 4

# Data fields enums
DATA_POST_ID = 0
# Data post fields
DATA_POST_TEXT = 1
DATA_POST_ATTACHMENTS_AUDIOS = 2
DATA_POST_ATTACHMENTS_PHOTOS = 3
DATA_POST_ATTACHMENTS_VIDEOS = 4
DATA_POST_ATTACHMENTS_DOCS = 5
DATA_POST_ATTACHMENTS_LINKS = 6
DATA_POST_ATTACHMENTS_NOTES = 7
DATA_POST_ATTACHMENTS_ALBUMS = 8
DATA_POST_POSTPONED_FIELD = 9
# Data group fields
DATA_GROUP_ID_FIELD = 10
DATA_GROUP_ACTIVITY_FIELD = 11
DATA_GROUP_DESCRIPTION_FIELD = 12
DATA_GROUP_COUNTERS_AUDIOS = 13
DATA_GROUP_COUNTERS_PHOTOS = 14
DATA_GROUP_COUNTERS_VIDEOS = 15
DATA_GROUP_COUNTERS_ALBUMS = 16
DATA_GROUP_COUNTERS_TOPICS = 17
DATA_GROUP_COUNTERS_DOCS = 18
DATA_GROUP_STATUS_FIELD = 19


# data types
TYPE_AUDIO = "audio"
TYPE_PHOTO = "photo"
TYPE_VIDEO = "video"
TYPE_DOC   = "doc"
TYPE_LINK  = "link"
TYPE_NOTE  = "note"
TYPE_ALBUM = "album"

data_types = {
    TYPE_AUDIO: None,
    TYPE_PHOTO: None,
    TYPE_VIDEO: None,
    TYPE_DOC:   None,
    TYPE_LINK:  None,
    TYPE_NOTE:  None,
    TYPE_ALBUM: None,
}

# counter types
COUNTER_AUDIOS = "audios"
COUNTER_PHOTOS = "photos"
COUNTER_VIDEOS = "videos"
COUNTER_DOCS   = "docs"
COUNTER_TOPICS = "topics"
COUNTER_ALBUMS = "albums"

counters = {
    COUNTER_AUDIOS: None,
    COUNTER_PHOTOS: None,
    COUNTER_VIDEOS: None,
    COUNTER_DOCS:   None,
    COUNTER_TOPICS: None,
    COUNTER_ALBUMS: None,
}
