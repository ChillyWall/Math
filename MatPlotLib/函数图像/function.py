def rectangular_coordinate():
    import matplotlib.pyplot as plt
    ax = plt.gca()

    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))

    plt.grid()

    ax.set_aspect(1)


def set_tick(beginning, end, number):
    import matplotlib.pyplot as plt
    import numpy as np
    ticks = np.linspace(beginning, end, number)
    plt.xticks(ticks)
    plt.yticks(ticks)