import matplotlib.pyplot as plt


def tell_story_about_lifetimevalue_comparing_devices(iphone, ipad):
    plt.bar([1, 2], [iphone, ipad], tick_label=['iPhone', 'iPad'])
    plt.savefig('../OPENME/ltv-iphone-ipad.png')
    plt.show()


def tell_story_about_classical_retention_rate_as_line(retention):
    xticks = ['trial'] + ['sub ' + str(i) for i in range(1, len(retention))]
    x = [i for i in range(len(retention))]

    plt.xticks(x, xticks)
    plt.xlabel('Weeks for install')

    plt.plot(x, retention)
    plt.savefig('../OPENME/classical-retention-rate-as-line.png')
    plt.show()


def tell_story_about_lifetimevalue_comparing_countries(ltv, countries):
    coord = [i for i in range(1, len(countries) + 1)]

    plt.title('Lifetime Value by Countries')
    plt.ylabel('Money')

    plt.bar(coord, ltv, tick_label=countries)
    plt.savefig('../OPENME/ltv-countries.png')
    plt.show()
