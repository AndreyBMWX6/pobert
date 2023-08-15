import psycopg2
from psycopg2 import Error
from config import *


def save_data(data, class_id):
    conn = init_db()
    insert_data(conn, data, class_id)
    get_data(conn)


def connect():
    try:
        conn = psycopg2.connect(host=config.DB_HOST, 
                                port=config.DB_PORT, 
                                database=config.DB_NAME,
                                user=config.DB_USER,
                                password=config.DB_PASS)
    except (Exception, Error) as err:
        conn.close()
        print(err)
        return err
    
    return conn

def init_db():
    try:
        conn = connect()
    except Exception:
        return Exception

    prepare_table(conn)
    
    return conn


def prepare_table(conn):
    # 'qufiwefefwoyn.inline-sql-syntax' vscode extension installed
    query = """--sql
        CREATE TABLE IF NOT EXISTS public.data(
            id                TEXT NOT NULL,
            class             INTEGER,
            -- post fields
            post_text         TEXT,
            post_audios       INTEGER,
            post_photos       INTEGER,
            post_videos       INTEGER,
            post_docs         INTEGER,
            post_links        INTEGER,
            post_notes        INTEGER,
            post_albums       INTEGER,
            post_postponed    BOOLEAN,
            -- group fields
            group_id          TEXT NOT NULL,
            group_activity    TEXT,
            group_description TEXT,
            group_audios      INTEGER,
            group_photos      INTEGER,
            group_videos      INTEGER,
            group_albums      INTEGER,
            group_topics      INTEGER,
            group_docs        INTEGER,
            group_status      TEXT,
            UNIQUE (id, group_id)
        );
        """

    with conn.cursor() as curs:
        curs.execute(query)
        conn.commit()


def insert_data(conn, data, class_id):
    query = """--sql
    INSERT INTO public.data (class, id, post_text, post_audios, post_photos, post_videos, 
                             post_docs, post_links, post_notes, post_albums, post_postponed,
                             group_id, group_activity, group_description, group_audios, group_photos, 
                             group_videos, group_albums, group_topics, group_docs, group_status)
                     VALUES (%s, %s, %s, %s, %s, %s,
                             %s, %s, %s, %s, %s,
                             %s, %s, %s, %s, %s, 
                             %s, %s, %s, %s, %s)
    ON CONFLICT (id, group_id) DO UPDATE SET class             = excluded.class,
                                   post_text         = excluded.post_text, 
                                   post_audios       = excluded.post_audios,
                                   post_photos       = excluded.post_photos, 
                                   post_videos       = excluded.post_videos, 
                                   post_docs         = excluded.post_docs, 
                                   post_links        = excluded.post_links, 
                                   post_notes        = excluded.post_notes, 
                                   post_albums       = excluded.post_albums, 
                                   post_postponed    = excluded.post_postponed,
                                   group_activity    = excluded.group_activity,
                                   group_description = excluded.group_description,
                                   group_audios      = excluded.group_audios, 
                                   group_photos      = excluded.group_photos, 
                                   group_videos      = excluded.group_videos, 
                                   group_albums      = excluded.group_albums, 
                                   group_topics      = excluded.group_topics, 
                                   group_docs        = excluded.group_docs, 
                                   group_status      = excluded.group_status
    """

    args = [class_id]
    args = args + data.get_args()
    args = (args)

    with conn.cursor() as curs:
        curs.execute(query, args)
        conn.commit()
        print('data inserted')

    return


def get_data(conn):
    query = """--sql
    SELECT id,
           class,
           post_audios,
           post_photos,
           post_videos,
           post_docs,
           post_links,
           post_notes,
           post_albums,
           post_postponed,
           group_id,
           group_activity,
           group_audios,
           group_photos,
           group_videos,
           group_albums,
           group_topics,
           group_docs,
           group_description,
           group_status,
           post_text
    FROM public.data
    """

    with conn.cursor() as curs:
        curs.execute(query)
        rows = curs.fetchall()

    return rows
