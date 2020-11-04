from datetime import date
import os


def autolabel(ax, rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def filepath(kind):
    directory_path = f"/home/marco/Documenti/coronavirus-plots/{date.today()}"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    return f"{directory_path}/{kind}.png"
