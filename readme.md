# Мод "Интересный номер"

> Алексей Наумов, студент второго курса из никому неизвестного универа. Благо, только в него я смог попасть на бюджет. Жизнь фонтаном не блещет, но мне много и не надо. Главное, что у меня есть, где жить и с кем общаться. Круг общения небольшой, но в нём находятся люди, которых я знаю ещё со школы. Сегодня, за столь большое время, мы решили встретиться вновь вживую…

<br>


## Прогресс написания мода

|                 | День 1 | День 2 | День 3 | День 4 | Рут Мику | Рут Алисы | Рут Лены | Рут Ульяны | Рут Слави | Рут одиночки |
|-----------------|--------|--------|--------|--------|----------|-----------|----------|------------|-----------|--------------|
|Сценарий         |✅|✅|✅|✅|✅|🔃|🔃|❌|❌|❌|
|Сценарий в коде  |✅|✅|❌|❌|❌|❌|❌|❌|❌|❌|
|Логика           |✅|🔃|❌|❌|❌|❌|❌|❌|❌|❌|
|Музыка           |✅|🔃|❌|❌|❌|❌|❌|❌|❌|❌|
|SFX              |✅|🔃|❌|❌|❌|❌|❌|❌|❌|❌|
|Фоны             |✅|🔃|❌|❌|❌|❌|❌|❌|❌|❌|
|Спрайты          |❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|

<br>

## Техническая документация
<br>

### Переменные действий
---

***Переменные действий*** - булевые переменные, определяющие, произошло в сюжете описываемое ими действие или нет.

Учитывая, что булевые переменные меняются в моде один раз, можно сказать, что место появляния переменной является её местом действия.

* ***day[1-4]_*** - префикс, указывающий, в каком дне мода переменная изменилась в первый раз
* Переменные используют ***camelCase***, когда все слова, кроме первого, начинаются с заглавной буквы без пробелов
* Именование переменных происходит в зависимости от произведённого действия, чтобы сразу был понятен контекст. Желательно использовать прошедшее время, но использование начальной формы глаголов не запрещается


<br>

### Переменные материалов
---

***Переменные материалов*** - переменные, содержащие относительные пути к музыке, фонам, звукам и спрайтам.

* ***ext_*** / ***int_*** - префиксы, указывающие на принадлежность фона относительно общего местоположения. Первый указывает на фон внутри помещения, второй - всё, что не включает в себя первый
* Вся музыка **НЕ** хранится в переменных, для запуска использовать относительный путь до файла

<br>

### Лэйблы
---
***Лэйблы*** - константы для прыжков между частями кода. Правила использования следующие:

* ***_day[1-4]*** - постфикс, указывающий, в какой день происходит событие, описываемое лэйблом
* Названия лэйблов используют ***PascalCase***, когда все слова начинаются с заглавной буквы без пробелов
* Из названия лэйбла должно быть ясно, что будет происходить по сюжету в этой части мода