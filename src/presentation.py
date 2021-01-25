import matplotlib.pyplot as plt


def present_ltv_compare_between_iphone_and_ipad(iphone, ipad):
    plt.bar([1, 2], [iphone, ipad], tick_label=['iPhone', 'iPad'])
    plt.savefig('../OPENME/ltv-iphone-ipad.png')
    plt.show()
