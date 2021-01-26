import matplotlib.pyplot as plt


def tell_story_about_total_lifetimevalue(ltv):
    ltv = round(ltv, 2)
    from matplotlib.ticker import FormatStrFormatter

    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax.set_ylim(0, 10)
    plt.bar([1, 2, 3], [0, ltv, 0], 1, tick_label=[''],color = 'red')
    plt.text(1.8, ltv - 1, str(ltv), fontsize=20, color='white')
    plt.title('Total LTV')

    plt.savefig('../OPENME/1) ltv.png')
    plt.show()

def tell_story_about_lifetimevalue_comparing_devices(iphone, ipad):
    plt.bar([1, 2], [iphone, ipad], tick_label=['iPhone', 'iPad'])
    plt.savefig('../OPENME/3) ltv-iphone-ipad.png')
    plt.show()


def tell_story_about_classical_retention_rate_as_line(retention):
    xticks = ['trial'] + ['sub ' + str(i) for i in range(1, len(retention))]
    x = [i for i in range(len(retention))]

    plt.title('User Retention')

    plt.xticks(x, xticks)
    plt.xlabel('Weeks for install')

    plt.plot(x, retention)
    plt.savefig('../OPENME/2) classical-retention-rate-as-line.png')
    plt.show()


def tell_story_about_lifetimevalue_comparing_countries(ltv, countries):
    coord = [i for i in range(1, len(countries) + 1)]

    plt.title('Lifetime Value by Countries')
    plt.ylabel('Money')

    plt.bar(coord, ltv, tick_label=countries)
    plt.savefig('../OPENME/3) ltv-countries.png')
    plt.show()



