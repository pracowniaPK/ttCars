import matplotlib.pyplot as plt

from data_handling import unpack_all, unpack_multiple
from charts import *
from stuff import week_day_names, h_list_subs, h_list


if __name__ == "__main__":
    # data = unpack_all('data')
    data = unpack_multiple(h_list, 'data')
    try:
        tesla = data.pop('tesla')
    except KeyError as e:
        print('No Tesla to pop. \n{}'.format(e))
    brands = data.keys()
    print(brands)
    
    fig = plt.figure()
    plot_stuff(data, get_hour, 24, [i for i in range(0,25,4)], 341, 
        'tweets/hour')
    plot_stuff(data, get_weekday, 7, [i for i in range(0, 8)], 342, 
        'tweets/weekday', week_day_names)
    plot_stuff_per_tweet(data, get_likes, 333, 'likes/tweet')

    plot_stuff_per_period(data, get_hour, get_likes, 24, 
        [i for i in range(0,25,4)], 345, 'likes/tweet/hour')
    plot_stuff_per_period(data, get_weekday, get_likes, 7, 
        [i for i in range(0, 8)], 346, 'likes/tweet/weekday', week_day_names)
    # plot_subs_vs_likes(data, h_list_subs, subs vs likes)
    plot_last_n_periods(data, get_months_back, get_likes, 6, 
        [i for i in range(0, 6)], 336, 'Likes, last 6 months')

    data['Tesla'] = tesla
    plot_stuff_per_period(data, get_hour, get_likes, 24, 
        [i for i in range(0,25,4)], 349, 'likes/tweet/hour', log=True)
    plot_stuff_per_period(data, get_weekday, get_likes, 7, 
        [i for i in range(0, 8)], 341, 'likes/tweet/weekday', week_day_names, 
        log=True, position3=(3,4,10))
    plot_last_n_periods(data, get_months_back, get_likes, 6, 
        [i for i in range(0, 6)], 000, 'Likes, last 6 months', 
        log=True,position3=(3,3,9))
    

    plt.savefig('plot.png', dpi=300)
    plt.show()

