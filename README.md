# Задача № 36

## Условие задачи
У преподавателя есть список заданий, каждое из который имеет тип (теория/практика), тематику и уровень сложности. Постройте алгоритм для генерации списка билетов, такой, чтобы одновременно выполнялись условия:
1) в зависимости от внешних условий состав билетов меняется;
2) билет содержит ровно 2 задачи (1 теория и 1 практика) из разных тем;
3) уровень сложности всех билетов приблизительно одинаковый.

## Как работает программа

### Немного о корректности работы
На вход программы подается input.txt файл , в котором пользователь составляет пул вопросов, задает колличество сдающих экзамен и допустимое отличие одного билета от всех остальных по сложности. Важно понимать, что честность экзамена, то есть сложность каждого вопроса по равноценности будет сильно зависить от того, как пользователь подберет пул вопросов. Например, может выпасть сложность 34 4,  где первое числобудет сложность теор. вопроса, а последнее сложность практического вопроса. Эта комбинация является не честной, т.к сложности вопросв в билете очень сильно отличаются. Так же насколько по тому, сколько в пуле будет вопросов, будет сильно зависить повторяемость вопросов в билетов. Если вопросо в пуле мало, то будет много повторяющихся вопросов в каждом билет. 
В общем, честность экзамена и гарантированность то,что удастся составить экзамен по пулу вопросов полностью ложится на плечи тому, кто этот пул вопросов состовлял. 

### Немного об одинаковости по сложности билетов
Итак, программа после начала работы разбивает из пула вопросы отдельно в массив вопросов по теории и отдельно в массив по практики.
Далее для каждого массва выбираем медиану. Медиана-это элемент  массива который находится в его середине. Затем получается вес медианы по сумме медиан двух массивов. Для веса медианы считаем интервал в виде:
[вес медианы - дельта(%), вкс медианы + дельта(%)]
Дельта - отклонение от в процентах от веса билета(сумма сложностей двух вопросов в билете)

Потом программа по заданному интерваллу подбирает первый билет  так, чтобы по весу билет попал в интервал сложности медианы. 
Затем идет уточнение границ интервала. Считается дельта отклонение уже от первого билета. Если вес билета - дельта(%) > вес медианы - дельта(%) тогда левая граница интервала билета обновляется до вес билета - дельта(%). Аналогично идет уточнение для верхней граници билета если вес билета + дельта(%) < веса медианы - дельта(%) тогда левая граница интервала билета обновляется до вес билета - дельта(%) . Данное уточнение границ сложности билетов гарантирует, что все остальные билеты при следующих уточнениях интервала при добавлении 2 , 3 и ... билетов будут отличаться друг от друга по сложности не более чем на дельту.

### Как программа выбирает билет с учетом того, что вес билета должен обязательно попасть в интервал? 
Сначала выбирается вопрос из теории функцией рандома такой, что вес самого вопроса меньше левой границы интревала. Затем в билет добирается вопрос по практике такой, что сумма сложностей теор вопроса и практики попадала в интервал. Причем практический вопрос выбирается следующим образом, идет проход по всему массиву до перого элемента, которой удовлетворяет условию описанному выше. Если удовлетворяет условию, то добавляем его в билет.
Если нет такого практического вопроса, чтобы условие вхождения в интервал выполнялось, то билет расформировывается и собирается заного до тех пор, пока не собирется билет подхододящий под условия вхождения в интервал.


