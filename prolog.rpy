init:

    # points vaiables
    $ dvPoints = 0 # Алиса
    $ miPoints = 0 # Мику
    $ slPoints = 0 # Славя
    $ unPoints = 0 # Лена
    $ usPoints = 0 # Ульяна

    # day 1 variables
    $ day1_wentToBusStop = False
    $ day1_wentToLibrary = False
    $ day1_wentToSquare = False
    $ day1_wentWithSlavya = False
    $ day1_helpedGosha = False
    $ day1_helpedLena = False
    $ day1_agreedWithUlyana = False
    $ day1_attendMusicClub = False

    # mod name & start tag
    $ mods['interestingNumber'] = u'Интересный номер'

    # additional characters
    $ lx = Character(u'Лёха', color='#B8860B', what_color='#E2C778')
    $ gh = Character(u'Гошан', color='#9E8565', what_color='#E2C778')
    $ cn = Character(u'Саня', color='#A52A2A', what_color='#E2C778')
    $ iv = Character(u'Внутренний голос', color='#ddf9ff', what_color='#E2C778')
    $ unvo = Character(u'Голос', color='#FAFAFA', what_color='#E2C778')

    # images
    image prologue_kitchen = '/interestingNumber/images/prologue/prologue_kitchen.jpg'
    image prologue_lada = '/interestingNumber/images/prologue/prologue_lada.jpg'

label interestingNumber:

    play music '/interestingNumber/sound/skazka.mp3'
    scene bg semen_room with dissolve

    'Я - Алексей Наумов, студент второго курса из никому неизвестного универа. Благо, только в него я смог попасть на бюджет.'
    'Жизнь фонтаном не блещёт, но мне много и не надо. Главное, что у меня есть, где жить и с кем общаться.'
    'Круг общения небольшой, но в нём находятся люди, которых я знаю ещё со школы. Сегодня, за столь большое время, мы решили встретиться вновь вживую…'

    play sound sfx_inhale
    stop music fadeout 0.5
    play music ['<silence .5>', '/interestingNumber/sound/skazka.mp3'] fadein 0.5
    show blinking
    play sound sfx_door_bell

    'Мои раздумья прервал звонок в дверь. Я закрыл ноутбук и с тяжестью поднялся с дивана.'

    stop sound
    play sound sfx_inhale
    play music['everyday_theme'] fadeout 1.5 fadein 1.0

    th 'Чёрт, сколько я так сидел? Всё тело затекло.'

    stop sound

    'Немного размявшись, я пошёл открывать дверь.'
    'На пороге стоял самый пунктуальный из нашей компашки - Саня.'
    'Саня - хороший человек. Иногда меня бесит его правильность, но он надёжный и проверенный временем.'
    'Его \"роль\" в нашей команде - мозгоправ. Так сказать, “Идиот” Достоевского местного разлива.'
    'Ну, ещё он \"мастер\" сарказма и острот.'
    cn 'Лёха, привет! Смотрю, ты ещё живой?'
    'Он ухмыльнулся.'
    cn 'Я, вот, специально пораньше пришёл, чтоб поскорее труп твой найти.'
    th 'Ох, опять его остроты.'
    lx 'Ну, на это ещё вся ночь впереди. Кстати, пока ты шёл сюда, не видел нашего толстого селянина?'
    'Не успел Саня ответить, как мы услышали недовольные звуки вперемешку с одышкой.'

    play sound sfx_inhale

    gh 'Чёрт *вздох* почему *вздох* лифт сломался именно сегодня? *вздох* Девятый, мать его, этаж!'
    cn 'Ну, вспомнил солнце, вот и деревенщина…'
    gh 'Я сейчас поднимусь и убью тебя.'
    cn 'Угу, я скорее поверю, что Гоголь воскреснет и второй том \"Мёртвых душ" напишет.'
    'Гошан наконец-то поднялся и, немного отдышавшись, поднял на нас глаза.'
    gh 'Привет, городские!'
    'Гошан - туповатый человек. За то и любим. Детство провёл в деревне. Оттуда и корни шуток про деревенщину.'
    'Хоть он и неуверенный в себе, а иногда даже пуглив, но ради своих друзей перешагнёт через себя.'
    'У него тоже есть своя \"роль\" - истреблять еду.'
    'Зайдя в квартиру и обменявшись любезностями, мы прошли на кухню.'

    play sound sfx_steps_clubs_nextroom
    show prologue_kitchen with dissolve

    'Спустя пару часов общения о нашей жизни я узнал много нового. Санёк, как никто не был удивлён, вполне сносно учится.'
    'Хотя, я считаю, что в универе мало чему учишься.'
    'Он даже стал старостой группы. Короче говоря, живёт неплохо.'
    'А вот с Гошаном другая история. Когда мы узнали, что он перешёл на бюджет, то у нас чуть челюсти не попадали.'
    'Саня даже подавился своим любимым кофе. Ведь в сети Гошан об этом ни разу не рассказывал.'
    'Дошла очередь до меня. Я молчал.'
    iv '{i}Ну, чё молчишь? Сказать нечего? Так и говори. Ты обиделся на весь мир, а сам один правильный.{/i}'
    th 'И ничего я не обиделся. Просто...'
    iv '{i}Просто, просто. Нашёл причину, чтоб ни хрена не делать.{/i}'
    'Я закипел.'
    th 'Заткнись. Не порти вечер.'
    'Голос затих. Я решил соврать своим друзьям насчёт своей жизни. Благо, они поверили.'
    'Дабы перевести тему, я решил порыться в холодильнике. Найдя пару бутылок пива, я вернулся за стол, прихватив их с собой.'
    gh 'О, а вот и выпивка!'
    cn 'Да, пиво — это хорошо.'
    'Каждый взял по бутылке, и наша пьянка началась. Пока Гошан и Саня о чём-то оживлённо ругались, я, взяв свои сигареты, отправился на балкон.'

    show blinking
    play sound sfx_medpunkt_door_open
    scene bg semen_room_window with dissolve

    'Сделав затяжку и осмотрев мой ночной заснеженный район, я задумался.'
    th 'Хм. А вдруг этот хрен в моей голове прав? Вдруг я лишь всю жизнь искал предлог для того, чтобы просто плыть по течению и ничего не делать?'
    'Я выдохнул дым.'
    th 'Хах. Хорошо живётся фаталистам. Всё у них предначертано, и делать ни хрена не надо. Не жизнь, а сказка.'
    'Мои размышления прервал Гошан.'
    gh 'Эй. Земля вызывает Лёху. Чё залип? Я тебе всегда говорил, что сигареты — зло, от них тупеют. Ты — доказательство.'
    'Я потряс головой и посмотрел на Гошу.'
    lx 'Чёрт, это мне говорит ходячая бочка алкашки.'
    lx 'Тебя, блин, что, Санёк остротами научил разговаривать?'
    'Гошан, видимо, был доволен моей реакцией и, похлопав меня по плечу, повёл обратно на кухню.'

    show blinking
    play sound sfx_close_door_1
    scene prologue_kitchen with dissolve

    'Только мы зашли обратно, как Саня встретил нас очередной колкостью.'

    stop sound

    cn 'О, а я думал, что ты упал. Поэтому Гошана на разведку отправил.'
    lx 'Ха-ха. Не дождёшься. Наша туса только началась.'
    'Тут Гошан обнаружил мою старую акустику.'
    'Достав гитару из-за шкафа, он протянул её мне.'
    gh 'На-ка, сбацай нам что-нибудь.'
    'Я взял в руки гитару.'
    iv '{i}Эх, Лёха. Ты держишь в руках единственную вещь, которую ты, на удивление, не забросил, как всё остальное в своей жизни.{/i}'
    th 'Опять ты? Может, всё же сходить к врачу? Что-то ты меня достал уже.'
    iv '{i}Всё, всё, молчу.{/i}'
    th 'То-то же.'
    gh 'Лёха, чё завис опять? Может, к врачу тебя сводить, а то так и загнёшься?'
    lx 'А? Чё? Не, всё пучком. Я просто песни вспоминал.'
    'Я настроил гитару и первое, что сыграл - мою любимую песню Цоя - \"Троллейбус\".'
    # стеклянный звук бутылки
    'Когда я закончил, то увидел Санька, достающего несколько бутылок водки.'
    'И тут понеслось…'
    'После трёх бутылок мы перестали соображать трезво. И тут Гошан выдал фразу:'
    gh 'Лёха, ты заливал, что у тебя права есть*ик* и ты хороший водитель *ик*, только мне, вот, не верится. Ты блин год пытался их получить *ик*. Слабо доказать?!'
    'Мой пьяный мозг заработал, как мог, чтобы я был способен связать хоть пару слов.'
    lx 'Я вот думаю, *ик* мне сначала тебя ударить, а потом сесть за руль или сначала сесть за руль, а потом ударить?!'
    'Пока мы с Гошаном сверлили друг друга взглядами, Санёк смотрел на это и смеялся.'
    gh 'На словах ты Лев Толстой, а...'
    'Я его прервал.'
    lx 'Пошли, я покажу, как водят мастера.'
    'Я поднялся, взял ключи и отправился к двери. Краем глаза увидел, как с лица Саньки сходит улыбка, а у Гошана, наоборот, делается ещё  шире.'
    'Скорее всего, был бы я не так пьян, то мой голос-шиза сейчас бы бил в колокол. Но его нет, значит, и проблем нет.'

    play sound sfx_intro_bus_stop_steps
    show prologue_lada at truecenter with dissolve:
        xzoom 2.0
        yzoom 2.0

    'Мы вышли на улицу и подошли к моему подарку от родителей - Жигулям. Саня протестовал, а Гошан пытался его успокоить, говоря, что всё будет хорошо.'
    'Я залез в чудо советского автопрома, а за мной мои друганы.'

    stop sound fadeout 1.5

    'Не знаю, как мы стартанули, но последнее, что мы видели — это яркие фары и номер \"410-й\".'

    show blink
    stop music fadeout 0.5

    'В моей голове промелькнула фраза: \"Интересный номер\".'
    'И тут погас свет.'

jump InterestingNumber_day1
