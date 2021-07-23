#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from requests import get
import termcolor
from colors import light_red


def profiler(user):
    username = bio = url = fullname = id = is_private = is_verified = followers = following = posts = None

    header = {
        'HOST': "www.instagram.com",
        'KeepAlive': 'True',
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'cookie': 'mid=YF93jgALAAE3vLXolGU8TUim3FA5; ig_did=3525CF13-8CA7-4886-8028-5FAC28C60E97; datr=U1VgYLyLNUpoQ6_ODYRFQe7n; csrftoken=llONvsDLwC82YAy8nFRJinhKvISAruxN; ds_user_id=276972397; sessionid=276972397%3AgQKkX8ikrFwQi8%3A7; shbid=14342; shbts=1623538759.6567142; rur=LDC',
        'Accept': "*/*",
        'ContentType': "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX": "missing",
        "X-CSRFToken": "missing",
        "Accept-Language": "en-US,en;q=0.9",
    }

    while True:
        try:
            requests = get(f'https://www.instagram.com/{user}/?__a=1', headers=header).json()
            break
        except:
            return light_red("USERNAME NOT VALID OR COOKIES EXPIRED.")

    try:
        if requests['graphql']['user']['username']: username = requests['graphql']['user']['username']
        if requests['graphql']['user']['biography']: bio = requests['graphql']['user']['biography']
        if requests['graphql']['user']['full_name']: fullname = requests['graphql']['user']['full_name']
        if requests['graphql']['user']['external_url']: url = requests['graphql']['user']['external_url']
        if requests['graphql']['user']['id']: id = requests['graphql']['user']['id']
        if requests['graphql']['user']['is_private']: is_private = requests['graphql']['user']['is_private']
        if requests['graphql']['user']['is_verified']: is_verified = requests['graphql']['user']['is_verified']
        if requests['graphql']['user']['edge_followed_by']['count']: followers = \
            requests['graphql']['user']['edge_followed_by']['count']
        if requests['graphql']['user']['edge_follow']['count']: following = requests['graphql']['user']['edge_follow'][
            'count']
        if requests['graphql']['user']['edge_owner_to_timeline_media']['count']: posts = \
            requests['graphql']['user']['edge_owner_to_timeline_media']['count']

    except:
        pass

    res = f"""└──{termcolor.colored("RESULT", "green")}

    {termcolor.colored('Username', 'cyan')}        : {username}
    {termcolor.colored('ID', 'cyan')}              : {id}
    {termcolor.colored('Full Name', 'cyan')}       : {fullname}
    {termcolor.colored('Biography', 'cyan')}       : {bio}
    {termcolor.colored('External Url', 'cyan')}    : {url}
    {termcolor.colored('Is Private', 'cyan')}      : {is_private}
    {termcolor.colored('Is Verified', 'cyan')}     : {is_verified}
    {termcolor.colored('Followers', 'cyan')}       : {followers}
    {termcolor.colored('Following', 'cyan')}       : {following}
    {termcolor.colored('Posts', 'cyan')}           : {posts}
"""
    return res
