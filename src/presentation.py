import matplotlib.pyplot as plt


def tell_story_about_lifetimevalue_comparing_devices(iphone, ipad):
    plt.bar([1, 2], [iphone, ipad], tick_label=['iPhone', 'iPad'])
    plt.savefig('../OPENME/ltv-iphone-ipad.png')
    plt.show()
