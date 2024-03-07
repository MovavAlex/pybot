import matplotlib.pyplot as plt



def diagram(count):
    labels = {'Человек-природа': 'count_man_nature', 'Человек-человек': 'count_man_man', 'Человек-техника':'count_man_tech', 'Человек-знаковая система':'count_man_sign_system', 'Человек-художественный\n образ': 'count_man_artist_image'}
    print(count['count_man_nature'])
    q = sum(count.values())
    sizes = [count['count_man_nature']//(q/100), count['count_man_man']//(q/100), count['count_man_tech']//(q/100), count['count_man_sign_system']//(q/100), count['count_man_artist_image']//(q/100)]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels.keys(), autopct='%1.1f%%')
    plt.savefig('photos/diagram.png')