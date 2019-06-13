import datetime
from math import floor

import matplotlib.pyplot as plt


def plot_stuff(data, extractor, xrange, ticks, position, label, labels=None):
    stuff = {}
    plt.subplot(position)
    plt.title(label)
    if labels:
        plt.xticks(ticks=ticks, labels=labels)
    else:
        plt.xticks(ticks=ticks)
    for brand in data.keys():
        stuff[brand] = {}
        for h in range(xrange):
            stuff[brand][h] = 0
        for t in data[brand]:
            h = extractor(t)
            stuff[brand][h] += 1
        plt.plot(list(stuff[brand].values()))

def plot_stuff_per_period(data, extractor, extractor2, xrange, ticks, position, label, labels=None, log=False, position3=None):
    stuff = {}
    tts = {}
    if position3:
        s = plt.subplot(*position3)
    else:
        s = plt.subplot(position)
    plt.title(label)
    if log:
        plt.yscale('log')
    if labels:
        plt.xticks(ticks=ticks, labels=labels)
    else:
        plt.xticks(ticks=ticks)

    for brand in data.keys():
        stuff[brand] = {}
        tts[brand] = {}
        for h in range(xrange):
            stuff[brand][h] = 0
            tts[brand][h] = 0
        for t in data[brand]:
            h = extractor(t)
            tts[brand][h] += 1
            q = extractor2(t)
            stuff[brand][h] += q
        for h in range(xrange):
            try:
                stuff[brand][h] = stuff[brand][h]/tts[brand][h]
                # print('{} {} {}'.format(brand, h, stuff[brand][h]))
            except ZeroDivisionError:
                stuff[brand][h] = 0
        mx = max(list(stuff[brand].values()))

        plt.plot(list(stuff[brand].values()))

def plot_stuff_per_tweet(data, extractor, position, label):
    stuff = {}
    tts = {}
    plt.subplot(position)
    plt.title(label)
    for brand in data.keys():
        stuff[brand] = 0
        tts[brand] = 0
        for t in data[brand]:
            q = extractor(t)
            tts[brand] += 1
            stuff[brand] += q
        try:
            stuff[brand] = stuff[brand]/tts[brand]
        except ZeroDivisionError:
            stuff[brand] = 0
    plt.barh([i for i in range(len(data))], list(stuff.values()), align='center', height=0.5, tick_label=list(data.keys()))
    # plt.plot(list(stuff.values()))
    plt.legend()
    
# def plot_subs_vs_likes(data, subs_data, position, label):
#     plt.subplot(position)
#     plt.title(label)

def plot_last_n_periods(data, extractor, extractor2, xrange, ticks, position, label, labels=None, log=False, position3=None):
    stuff = {}
    if position3:
        s = plt.subplot(*position3)
    else:
        s = plt.subplot(position)
    if log:
        plt.yscale('log')
        # s.set_ylim(ymin=1)
    plt.title(label)
    plt.xticks(ticks=ticks)
    for brand in data.keys():
        stuff[brand] = {}
        for d in range(xrange):
            stuff[brand][d] = 0
        for t in data[brand]:
            d = extractor(t)
            try:
                stuff[brand][d] += extractor2(t)
            except KeyError:
                pass
        plt.plot(list(stuff[brand].values()), label=brand)
    s.set_xticklabels([i for i in range(0, -6, -1)])
    plt.legend(loc=2, bbox_to_anchor=(-0.6, 1))


def get_hour(item):
    return item['time'].hour

def get_weekday(item):
    return item['time'].weekday()

def get_likes(item):
    return item['likes']

def get_months_back(item, offset=0):
    days_diff = (datetime.date.today() - item['time'].date()).days
    return floor((days_diff + offset)/30)





#   words = {}
#   for t in data:
#     wds = t['text'].split(' ')
#     for w in wds:
#       try:
#         words[w] += 1
#       except KeyError as _:
#         words[w] = 1

#   print(sorted(words.items(), key=lambda kv: kv[1]))
#   plt.subplot(122)
#   plt.plot(words.values())
#   plt.savefig('plot.png')