label ourrday2:
    $ backdrop = "days"
    $ new_chapter(2, u"Интересный номер. День второй.")
    $ persistent.sprite_time = 'day'
    $ day_time()
    "Глаза еще не открылись, но уши уже работали. {w}Вместо пения птиц или простой тишины, я слышал какой-то голос."
    "Я не мог узнать, кто это говорит, но было понятно, что этот голос был чем-то недоволен."
    "Через пару секунд, я понял кто это был…"
    scene bg int_house_of_mt_day
    mt "АЛЕКСЕЙ, А НУ КА БЫСТРО ВСТАВАЙ, ИНАЧЕ, Я ПОЙДУ ЗА ВОДОЙ И ТЕБЕ НЕСДОБРОВАТЬ!" with vpunch
    "Это был голос очень злой Ольги."
    "Взяв все силы в кулак, я сел на кровать, на большее, пока что не хватало."
    show blinking
    $ renpy.pause(1)
    show blinking
    "Немного поморгав, я сначала посмотрел на вожатую, а потом на часы."
    th "Семь часов утра! Какого черта?!"
    "От шока мои глаза стали круглые, как колеса. {w}Ольга Дмитриевна все также не довольно на меня смотрела."
    lx "Зачем так рано?"
    "Только и смог сказать мой сонный мозг."
    mt "Линейка. Не волнуйся, не каждый день. А еще мы опаздываем, так что быстро одевайся!"
    "Почесав подбородок, и потянувшись за штанами, я пробубнил."
    lx "Хорошо, хорошо. Как будто к первой паре встаю."
    "Я начал одеваться. {w}Ольга смотрела на меня оценивающим взглядом."
    mt "Так, вот тебе пакет с средствами гигиены. Ты все-таки - пионер, а пионер не может быть грязнулей. {w}Но воспользуешься ими после линейки, времени нет. Одевайся быстрее."
    "Я лишь кивнул и начал быстрее одеваться."
    scene bg ext_house_of_mt_day with dissolve
    "Я кое-как оделся, после чего вожатая схватила меня за руку и чуть ли не бегом вышла из дома."
    scene bg ext_square_day with dissolve
    "До площади мы добрались практически за минуту, и только тогда вожатая отпустила меня и показала, куда мне встать."
    "Кивнув, я побрел в указанное место."
    
    