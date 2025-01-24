# Описание проекта: программа загадывает слово, а пользователь должен его угадать. Изначально все буквы слова
# неизвестны. # Также рисуется виселица с петлей. Пользователь предлагает букву, которая может входить в это слово.
# Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове.
# Если такой буквы нет, к виселице добавляется круг в петле, изображающий голову. Пользователь продолжает
# отгадывать буквы до тех пор, пока не отгадает всё слово.
# За каждую неудачную попытку добавляется еще одна часть туловища висельника (обычно их 6: голова,
# туловище, 2 руки и 2 ноги).
import random

word_list = ['пиво', 'живоглот', 'сноуборд', 'рік', 'людина', 'час', 'справа', 'життя', 'день', 'рука', 'раз',
             'робота', 'слово', 'місце', 'обличчя',
             'друг', 'оче', 'питання', 'будинок', 'сторона', 'країна', 'світ', 'випадок', 'голова', 'дитина', 'сила',
             'кінець',
             'вид', 'система', 'частина', 'місто', 'ставлення', 'жінка', 'гроші', 'земля', 'машина', 'вода', 'батько',
             'проблема', 'година', 'право', 'нога', 'рішення', 'двері', 'образ', 'історія', 'влада', 'закон', 'війна',
             'бог', 'голос', 'тисяча', 'книга', 'можливість', 'результат', 'ніч', 'стіл', 'ім"я', 'область', 'стаття',
             'число', 'компанія', 'народ', 'дружина', 'група', 'розвиток', 'процес', 'суд', 'умова', 'засіб',
             'початок', 'світло', 'пора', 'шлях', 'душа', 'рівень', 'форма', 'зв"язок', 'хвилина', 'вулиця', 'вечір',
             'якість', 'ідея', 'дорога', 'мати', 'дія', 'місяць', 'держава', 'мова', 'любов', 'погляд',
             'мама', 'століття', 'школа', 'ціль', 'суспільство', 'діяльність', 'організація', 'президент', 'кімната',
             'порядок', 'момент', 'театр', 'лист', 'ранок', 'допомога', 'ситуація', 'роль', 'рубль', 'сенс',
             'стан',
             'квартира', 'орган', 'увага', 'тіло', 'праця', 'син', 'міра', 'смерть', 'ринок', 'програма', 'завдання',
             'підприємство', 'вікно', 'розмова', 'уряд', 'сім"я', 'виробництво', 'інформація', 'становище',
             'центр', 'відповідь', 'чоловік', 'автор', 'стіна', 'інтерес', 'федерація', 'правило', 'управління',
             'чоловік',
             'ідея', 'партія', 'рада', 'рахунок', 'серце', 'рух', 'річ', 'матеріал', 'тиждень', 'почуття', 'глава',
             'наука', 'ряд', 'газета', 'причина', 'плечо', 'ціна', 'план', 'мова', 'точка', 'основа', 'товариш',
             'культура', 'дані', 'думка', 'документ', 'інститут', 'хід', 'проект', 'зустріч', 'директор', 'термін',
             'палець', 'досвід', 'служба', 'доля', 'дівчина', 'черга', 'ліс', 'склад', 'член', 'кількість',
             'подія',
             'об"єкт', 'зал', 'створення', 'значення', 'період', 'крок', 'брат', 'мистецтво', 'структура', 'номер',
             'приклад', 'дослідження', 'громадянин', 'гра', 'начальник', 'зріст', 'тема', 'принцип', 'метод', 'тип',
             'фільм', 'край', 'гість', 'повітря', 'характер', 'боротьба', 'використання', 'розмір', 'освіта',
             'хлопчик', 'кров', 'район', 'небо', 'армія', 'клас', 'представник', 'участь', 'дівчинка', 'політика',
             'герой', 'картина', 'долар', 'спина', 'територія', 'пол', 'поле', 'зміна', 'напрямок', 'малюнок',
             'течі', 'церква', 'банк', 'сцена', 'населення', 'більшість', 'музика', 'правда', 'свобода', 'пам"ять',
             'команда', 'союз', 'лікар', 'договір', 'дерево', 'факт', 'господар', 'природа', 'кут', 'телефон',
             'позиція',
             'двір', 'письменник', 'літак', 'обсяг', 'рід', 'сонце', 'віра', 'берег', 'вистава', 'фірма', 'способ',
             'завод', 'колір', 'журнал', 'керівник', 'фахівець', 'оцінка', 'регіон', 'пісня', 'відсоток',
             'батько',
             'море', 'вимоги', 'підстава', 'половина', 'роман', 'коло', 'аналіз', 'вірші', 'автомобіль',
             'економіка', 'література', 'папір', 'поет', 'ступень', 'пан', 'надія', 'предмет', 'варіант',
             'міністр', 'кордон', 'дух', 'модель', 'операція', 'пара', 'сон', 'назва', 'розум', 'привід', 'старий',
             'мільйон', 'успіх', 'щастя', 'хлопці', 'кабінет', 'магазин', 'простір', 'вихід', 'удар', 'база',
             'знання', 'текст', 'захист', 'керівництво', 'площа', 'свідомість', 'вік', 'учасник', 'ділянка',
             'пункт', 'лінія', 'бажання', 'тато', 'лікар', 'губа', 'дочка', 'середовище', 'голова', 'подання',
             'солдат', 'художник', 'волос', 'зброя', 'відповідність', 'вітер', 'хлопець', 'зір', 'генерал', 'вогонь',
             'поняття', 'будівництво', 'вухо', 'груди', 'ніс', 'страх', 'послуга', 'зміст', 'радість',
             'безпека', 'продукт', 'комплекс', 'бізнес', 'сад', 'співробітник', 'літо', 'курс', 'пропозиція', 'рот',
             'технологія', 'реформа', 'відсутність', 'собака', 'камінь', 'майбутнє', 'оповідання', 'контроль', 'річка',
             'продукція', 'сума', 'техніка', 'будівля', 'сфера', 'необхідність', 'фонд', 'підготовка', 'лист',
             'республіка', 'господарство', 'воля', 'бюджет', 'сніг', 'село', 'мужик', 'елемент', 'обставина',
             'німець', 'перемога', 'джерело', 'зірка', 'вибір', 'маса', 'підсумок', 'сестра', 'практика', 'проведення',
             'кишеню', 'слава', 'кухня', 'визначення', 'функція', 'військо', 'комісія', 'застосування', 'капітан',
             'працівник', 'забезпечення', 'офіцер', 'прізвище', 'межа', 'вибори', 'вчений', 'пляшка', 'бій', 'теорія',
             'зона', 'відділ', 'зуб', 'розробка', 'особа', 'гора', 'товар', 'метр', 'свято', 'вплив',
             'читач', 'задоволення', 'актор', 'сльоза', 'відповідальність', 'вчитель', 'акт', 'біль', 'множина',
             'особливість', 'показник', 'корабель', 'звук', 'враження', 'приватність', 'дитинство', 'висновок',
             'професор', 'частка', 'норма', 'минуле', 'командир', 'коридор', 'підтримка', 'рамка', 'ворог', 'етап',
             'чорт', 'дід',
             'збори', 'прийом', 'хвороба', 'клітина', 'шкіра', 'заява', 'спроба', 'порівняння', 'розрахунок', 'депутат',
             'комітет', 'знак', 'дядько', 'облік', 'хліб', 'чай', 'режим', 'ціле', 'вірус', 'вираз', 'здоров"я',
             'зима', 'десяток', 'глибина', 'мережа', 'студент', 'секунда', 'швидкість', 'пошук', 'сутність', 'податок',
             'помилка',
             'дохід', 'режисер', 'поверхня', 'відчуття', 'карта', 'клуб', 'станція', 'революція', 'коліно',
             'міністерство', 'скло', 'поверх', 'висота', 'бабуся', 'трубка', 'газ', 'майстер', 'поведінка', 'столиця',
             'механізм', 'передача', 'здатність', 'підхід', 'енергія', 'існування', 'виконання', 'кіно',
             'жаль', 'заступник', 'ресурс', 'акція', 'народження', 'адміністрація', 'вартість', 'усмішка',
             'артист',
             'сусід', 'фраза', 'фігура', 'суб"єкт', 'реакція', 'список', 'фотографія', 'журналіст', 'травень',
             'порушення',
             'засідання', 'натовп', 'лікарня', 'істота', 'властивість', 'борг', 'покоління', 'тварина', 'схема',
             'зусилля', 'відмінність', 'острів', 'противник', 'хвиля', 'реалізація', 'сторінка', 'формування', 'житель',
             'краса', 'птах', 'рослина', 'тінь', 'явище', 'храм', 'запах', 'горілка', 'наявність', 'жах', 'одяг',
             'крісло', 'хворий', 'поїзд', 'університет', 'традиція', 'адреса', 'грудень', 'долоня', 'зведення',
             'квітка',
             'лідер', 'жовтень', 'заняття', 'вересень', 'приміщення', 'січень', 'глядач', 'редакція', 'стиль', 'весна',
             'фактор', 'серпень', 'відомість', 'залежність', 'охорона', 'обладнання', 'концерт', 'відділення',
             'витрата',
             'виставка', 'міліція', 'перехід', 'епоха', 'захід', 'твір', 'батьківщина', 'власність', 'таємниця',
             'трава', 'табір', 'майно', 'ліжко', 'апарат', 'середина', 'березень', 'клієнт', 'дама', 'фронт',
             'галузь', 'стілець', 'бесіда', 'законодавство', 'продаж', 'підвищення', 'музей', 'слід', 'полковник',
             'сумнів', 'розуміння', 'квітень', 'князь', 'риба', 'дума', 'кодекс', 'добу', 'диво', 'шия', 'суддя',
             'дах', 'настрій', 'потік', 'посада', 'злочин', 'мозок', 'честь', 'пост', 'єврей', 'червень',
             'сотня', 'дощ', 'сходи', 'дача', 'установка', 'поява', 'отримання', 'зразок', 'труба', 'головне',
             'осінь', 'костюм', 'баба', 'цінність', 'обов"язок', 'п"єса', 'таблиця', 'вино', 'спогад', 'конь',
             'колега', 'організм', 'учень', 'установа', 'відкриття', 'том', 'чорта', 'характеристика', 'виконання',
             'оборона', 'виступ', 'температура', 'перспектива', 'подруга', 'наказ', 'жертва', 'ресторан',
             'кілометр', 'спор', 'смак', 'ознака', 'промисловість', 'американець', 'лоб', 'висновок', 'схід',
             'виключення', 'ключ', 'постанова', 'шар', 'бік', 'липень', 'переклад', 'секретар', 'шматок', 'слух',
             'користь', 'дзвінок', 'обстановка', 'чиновник', 'угода', 'деталь', 'російський', 'тиша', 'зарплата',
             'квиток', 'подарунок', 'в"язниця', 'ящик', 'конкурс', 'книжка', 'вивчення', 'прохання', 'цар', 'публіка',
             'сміх', 'повідомлення', 'загроза', 'біда', 'блок', 'досягнення', 'призначення', 'реклама', 'портрет',
             'олія', 'стакан',
             'урок', 'годинник', 'крик', 'творчість', 'телевізор', 'інструмент', 'концепція', 'лейтенант', 'екран',
             'дно',
             'реальність', 'канал', 'м"ясо', 'знайомий', 'щока', 'конфлікт', 'переговори', 'запис', 'вагон',
             'майданчик',
             'наслідок', 'співпраця', 'дзеркало', 'тон', 'академія', 'палата', 'потреба', 'листопад',
             'збільшення', 'дурень', 'поїздка', 'обід', 'втрата', 'лютий', 'захід', 'парк', 'прийняття',
             'пристрій', 'речовина', 'категорія', 'сезон', 'готель', 'видання', 'об"єднання', 'темрява',
             'людство', 'колесо', 'небезпека', 'дозвіл', 'вплив', 'колектив', 'камера', 'запас',
             'слідство', 'довжина', 'крило', 'округ', 'фон', 'кандидат', 'родич', 'тиск', 'присутність',
             'взаємодія', 'дошка', 'партнер', 'двигун', 'шум', 'гідність', 'гріх', 'ніж', 'політ', 'пристрасть',
             'випробування', 'істина', 'оплата', 'різниця', 'водій', 'пакет', 'зниження', 'формула', 'живот', 'капітал',
             'міст', 'новина', 'ефект', 'вхід', 'губернатор', 'доповідь', 'зміна', 'вбивство', 'експерт', 'автобус',
             'сукня', 'кадр', 'тітка', 'спілкування', 'психологія', 'лев', 'поріг', 'перевірка', 'процедура', 'робочий',
             'ремонт', 'звернення', 'навчання', 'очікування', 'пам"ятник', 'корінь', 'спостереження', 'літера',
             'доказ', 'визнання', 'ліжко', 'штаб', 'власник', 'комп"ютер', 'інженер', 'стара', 'човен',
             'ракета', 'серія', 'жарт', 'вершина', 'випуск', 'кулак', 'лід', 'торгівля', 'нафта', 'молодь', 'цифра',
             'корпус', 'недолік', 'чобіт', 'сутність', 'талант', 'ефективність', 'кава', 'смуга', 'основне',
             'розгляд', 'збір', 'штат', 'слідчий', 'житло', 'мішок', 'опис', 'кущ', 'відмова', 'замок',
             'редактор', 'палац', 'піклування', 'пиво', 'диван', 'столик', 'експеримент', 'друк', 'кільце', 'пістолет',
             'виховання', 'начальство', 'професія', 'ворота', 'добро', 'дружба', 'спокій', 'ризик', 'закінчення', 'дим',
             'шлюб', 'величина', 'записка', 'ініціатива', 'совість', 'активність', 'кістка', 'спорт', 'кредит',
             'господь', 'майор', 'конференція', 'стеля', 'бібліотека', 'помічник', 'конструкція', 'відпочинок', 'ручка',
             'метал',
             'молоко', 'прокурор', 'транспорт', 'поезія', 'з"єднання', 'фарба', 'відстань', 'мрія', 'село', 'їжа',
             'зло', 'підрозділ', 'сюжет', 'кордон', 'сигнал', 'атмосфера', 'хрест', 'вага', 'вибух', 'контакт',
             'сигарета', 'захват', 'золото', 'грунт', 'премія', 'король', 'під"їзд', 'шанс', 'автомат', 'замовлення',
             'хлопчисько', 'окуляри', 'мить', 'штука', 'читання', 'селище', 'свідок', 'ставка', 'сумка', 'здивування',
             'хвіст', 'пісок', 'поворот', 'повернення', 'миттєвість', 'статус', 'озеро', 'буд', 'параметр', 'казка',
             'тенденція', 'вина', 'дихання', 'версія', 'масштаб', 'монастир', 'господиня', 'дочка', 'танець',
             'експлуатація', 'комуніст', 'пенсія', 'приятель', 'пояснення', 'набір', 'виробник', 'пил',
             'філософія', 'потужність', 'зобов"язання', 'догляд', 'горло', 'криза', 'вказівка', 'плата', 'яблуко',
             'препарат', 'дійсність', 'москвич', 'залишок', 'зображення', 'угода', 'твір',
             'покупець', 'танк', 'витрата', 'рядок', 'одиниця']


def get_word(word):
    return random.choice(word).upper()


def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',

        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',

        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',

        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    print('Зіграємо у вгадайку слів!')
    word_letters = ['_' for _ in range(len(word))]
    guessed = True
    guessed_letters = []
    tries = 6

    while guessed:
        print(display_hangman(tries))
        print(' '.join(word_letters))
        if tries == 0:
            print('Ви програли!')
            break
        letter = input('Введіть букву чи слово: ').upper()
        if len(letter) >= 2:
            if letter == word:
                print('Вітаю, ви вгадали слово! Ви виграли!')
                guessed = False
            else:
                continue
        elif letter in word and letter in guessed_letters:
            print('Ви вже називали цю букву, виберіть другу')
        elif letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    word_letters[i] = letter
                    guessed_letters.append(word[i])
            if word_letters.count('_') == 0:
                print('Вітаю, ви вгадали слово! Ви виграли!')
                guessed = False
                print('Слово було: ', ' '.join(word_letters))
                word_list.remove(word.lower())
        else:
            print('Вы помилились')
            tries -= 1


play_again = ''

while True:
    word = get_word(word_list)
    play(word)
    play_again = input('Хочете зіграти ще раз? Введіть y/n або т/н: ').lower()

    if play_again not in ("т", "y"):
        print("Дякую за Гру, удачі Вам")
        break
