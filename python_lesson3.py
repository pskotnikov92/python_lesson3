from re import split

str_1 = 'Все счастливые семьи похожи друг на друга, каждая несчастливая семья несчастлива по-своему.'
str_2 = 'Все смешалось в доме Облонских. Жена узнала, что муж был в связи с бывшею в их доме француженкою-гувернанткой, и объявила мужу, что не может жить с ним в одном доме. Положение это продолжалось уже третий день и мучительно чувствовалось и самими супругами, и всеми членами семьи, и домочадцами. Все члены семьи и домочадцы чувствовали, что нет смысла в их сожительстве и что на каждом постоялом дворе случайно сошедшиеся люди более связаны между собой, чем они, члены семьи и домочадцы Облонских. Жена не выходила из своих комнат, мужа третий день не было дома. Дети бегали по всему дому, как потерянные; англичанка поссорилась с экономкой и написала записку приятельнице, прося приискать ей новое место; повар ушел вчера со двора, во время самого обеда; черная кухарка и кучер просили расчета.'
str_3 = 'На третий день после ссоры князь Степан Аркадьич Облонский — Стива, как его звали в свете, — в обычный час, то есть в восемь часов утра, проснулся не в спальне жены, а в своем кабинете, на сафьянном диване. Он повернул свое полное, выхоленное тело на пружинах дивана, как бы желая опять заснуть надолго, с другой стороны крепко обнял подушку и прижался к ней щекой; но вдруг вскочил, сел на диван и открыл глаза.'
str_4 = '«Да, да, как это было? — думал он, вспоминая сон. — Да, как это было? Да! Алабин давал обед в Дармштадте; нет, не в Дармштадте, а что-то американское. Да, но там Дармштадт был в Америке. Да, Алабин давал обед на стеклянных столах, да, — и столы пели: Il mio tesoro 1 и не Il mio tesoro, а что-то лучше, и какие-то маленькие графинчики, и они же женщины», — вспоминал он.'
str_5 = 'Глаза Степана Аркадьича весело заблестели, и он задумался, улыбаясь. «Да, хорошо было, очень хорошо. Много еще что-то там было отличного, да не скажешь словами и мыслями даже наяву не выразишь». И, заметив полосу света, пробившуюся сбоку одной из суконных стор, он весело скинул ноги с дивана, отыскал ими шитые женой (подарок ко дню рождения в прошлом году), обделанные в золотистый сафьян туфли, и по старой, девятилетней привычке, не вставая, потянулся рукой к тому месту, где в спальне у него висел халат. И тут он вспомнил вдруг, как и почему он спит не в спальне жены, а в кабинете; улыбка исчезла с его лица, он сморщил лоб.'
str_6 = '«Ах, ах, ах! Ааа!..» — замычал он, вспоминая все, что было. И его воображению представились опять все подробности ссоры с женою, вся безвыходность его положения и мучительнее всего собственная вина его.'
str_7 = '«Да! она не простит и не может простить. И всего ужаснее то, что виной всему я, виной я, а не виноват. В этом-то вся драма, — думал он. — Ах, ах, ах!» — приговаривал он с отчаянием, вспоминая самые тяжелые для себя впечатления из этой ссоры.'
str_8 = 'Неприятнее всего была та первая минута, когда он, вернувшись из театра, веселый и довольный, с огромною грушей для жены в руке, не нашел жены в гостиной; к удивлению, не нашел ее и в кабинете и, наконец, увидал ее в спальне с несчастною, открывшею все, запиской в руке.'
str_9 = 'Она, эта вечно озабоченная, и хлопотливая, и недалекая, какою он считал ее, Долли, неподвижно сидела с запиской в руке и с выражением ужаса, отчаяния и гнева смотрела на него.'
str_10 = '— Что это? это? — спрашивала она, указывая на записку.'
str_11 = 'И при этом воспоминании, как это часто бывает, мучало Степана Аркадьича не столько самое событие, сколько то, как он ответил на эти слова жены.'
str_12 = 'С ним случилось в эту минуту то, что случается с людьми, когда они неожиданно уличены в чем-нибудь слишком постыдном. Он не сумел приготовить свое лицо к тому положению, в которое он становился перед женой после открытия его вины. Вместо того чтоб оскорбиться, отрекаться, оправдываться, просить прощения, оставаться даже равнодушным — все было бы лучше того, что он сделал! — его лицо совершенно невольно («рефлексы головного мозга», — подумал Степан Аркадьич, который любил физиологию), совершенно невольно вдруг улыбнулось привычною, доброю и потому глупою улыбкой.'
str_13 = 'Эту глупую улыбку он не мог простить себе. Увидав эту улыбку, Долли вздрогнула, как от физической боли, разразилась, со свойственною ей горячностью, потоком жестоких слов и выбежала из комнаты. С тех пор она не хотела видеть мужа.'

str_total = str_1 + str_2 + str_3 + str_4 + str_5 + str_6 + str_7 + str_8 + str_9 + str_10 + str_11 + str_12 + str_13

    #Скопировали в программу каждую строку отдельно, замем, объединили все строки в одну.

replace = ' '

    #Назначаем пробел символом замены для знаков препинания

str_total = str_total.replace(',', replace)
str_total = str_total.replace('.', replace)
str_total = str_total.replace('-', replace)
str_total = str_total.replace(';', replace)
str_total = str_total.replace('?', replace)
str_total = str_total.replace(':', replace)
str_total = str_total.replace('—', replace)
str_total = str_total.replace('(', replace)
str_total = str_total.replace(')', replace)
str_total = str_total.replace('!', replace)
str_total = str_total.replace('«', replace)
str_total = str_total.replace('»', replace)

    #Перечисляем знаки препинания, которые надо заменить

print(str_total)

    #Выводим текст в виде строки без знаков препинания

new_str_total = str_total.split()
print(new_str_total)

    #Формируем list со словами методом split

new_str_total = list(map(lambda str_total: str_total.lower(), str_total))
print(new_str_total)

    #Приводим все слова к нижнему регистру через функцию map

x_dict = {} #Создаем словарь
for i in range(len(new_str_total)): # len Возвращает число элементов в указанном объекте.
    x_dict[new_str_total[i]] = new_str_total.count(new_str_total[i]) #ключ = значение (count Возвращает количество вхождений указанного значения в список)
print(x_dict)

    #word = (list(sorted(x_dict.values(), reverse=True))) #обращаемся ко всем значениям словаря

sort_list = list(x_dict.items())
sort_list.sort(key = lambda i: i[1],reverse = True)
print(sort_list[:5])

print('Количество уникальных (разных) слов в тексте', len(set(new_str_total))) # set длина списка уникальных слов

