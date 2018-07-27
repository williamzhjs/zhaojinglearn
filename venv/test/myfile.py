# e
import matplotlib.pylab as plt


def mytime():
    print("my name is ZHAOJING")
    squence_x = list(range(1, 20))
    squence_y = [i**2 for i in squence_x]
    # plt.figure(figsize=(10,6))
    # 设置标题信息
    plt.title("ZHAOJING", fontsize=24)
    plt.xlabel("value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.axis([0, 20, 0, 1000])
    # 设置刻度标记大小
    plt.plot(squence_x, squence_y)
    plt.show()


if __name__ == "__main__":
    mytime()
