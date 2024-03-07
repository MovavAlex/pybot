TELEGRAM_TOKEN = '6778306341:AAFYby3VUIrRrlZobU1JLOmjeTJaNpC26Us'

count = {'count_man_nature': 1, 'count_man_man': 2, 'count_man_tech': 1, 'count_man_sign_system': 3,
         'count_man_artist_image': 1}

q = sum(count.values())
print(count['count_man_nature']/(q/100))