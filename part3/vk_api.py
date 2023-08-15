import vk
import enums
from models import *
from config import config, secret_config


def connect():
    api = vk.API(access_token=secret_config.VK_ACCESS_TOKEN,
                 v=config.VK_API_VERSION)
    return api


def get_data(post_id):
    # connect to vk api
    api = connect()
    
    try:
        data = get_all_data(api, post_id)
        return data
    except:
        raise Exception


def get_all_data(api, post_id):
    response = api.wall.getById(posts=post_id, extended=1, fields=enums.group_fields)

    post_info = response[enums.post_post_key]
    group_info = response[enums.post_group_key]

    groups = get_groups_data(group_info)
    posts = get_post_data(post_info)

    g = groups[0]
    p = posts[0]

    g_args = g.get_data_args()
    p_args = p.get_data_args()

    args = p_args + g_args 

    d = data.Data(args)

    return d

def get_data_from_group_post(group, post):
    g_args = group.get_data_args()
    p_args = post.get_data_args()

    args = p_args + g_args

    d = data.Data(args)

    return d

def get_groups_data(group_info):
    # contains 1 item
    if len(group_info) < 1:
        print("no group info for post")
        raise ValueError

    groups = []
    args = []
    for item in group_info:
        for field in enums.group_fields:
            arg = item.get(field)
            args.append(arg)

        g = group.Group(args)
        groups.append(g)

    return groups


def get_post_data(post_info):
    # contains 1 item
    if len(post_info) < 1:
        print("no post info for post")
        raise ValueError
    
    posts = []
    for item in post_info:
        args = []
        for field in enums.post_fields:
            arg = item.get(field)
            args.append(arg)
        
        p = post.Post(args)
        posts.append(p)
    
    return posts
 
    
def get_posts_data_by_groups(group_ids):
    api = connect()
    response = api.groups.getById(group_ids=group_ids, fields=enums.group_fields)

    posts_data = {}
    groups = get_groups_data(response)
    for g in groups:
        posts = get_posts_data_by_group(api, g.id)
        posts_data[g.id] = posts

    return groups, posts_data


def get_posts_data_by_group(api, group_id):
    response = api.wall.get(owner_id=-group_id, count=100)
    posts = get_post_data(response['items'])
    return posts
