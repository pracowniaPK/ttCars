import matplotlib.pyplot as plt

from data_handling import unpack_all
from charts import *
from stuff import week_day_names, h_list_subs

if __name__ == "__main__":
    data = unpack_all('data')
    print(data.keys())
    data.pop('Tesla')
    brands = data.keys()
    
    plot_stuff(data, get_hour, 24, [i for i in range(0,25,4)], 241, 'tweets/hour')
    plot_stuff(data, get_weekday, 7, [i for i in range(0, 8)], 242, 'tweets/weekday', week_day_names)
    plot_stuff_per_hour(data, get_hour, get_likes, 24, [i for i in range(0,25,4)], 245, 'likes/tweet/hour')
    plot_stuff_per_hour(data, get_weekday, get_likes, 7, [i for i in range(0, 8)], 246, 'likes/tweet/weekday', week_day_names)
    plot_stuff_per_tweet(data, get_likes, 233, 'likes/tweet')
    # plot_subs_vs_likes(data, h_list_subs, subs vs likes)
    
    plt.show()

    plt.savefig('chart.png', dpi=300)


