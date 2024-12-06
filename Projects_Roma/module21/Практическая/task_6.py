# Задача 6. Быстрая сортировка
# Что нужно сделать
# Реализуйте алгоритм быстрой сортировки (её называют сортировкой Хоара).
#
# За один шаг алгоритма выполните следующие действия:
#
# Выберите один элемент списка (его иногда называют опорным элементом). Сделать это можно разными способами,
# но важно придерживаться одного принципа. В нашем случае опорным элементом всегда будет крайний правый (например,
# в списке [1, 2, 3] это 3). Разбейте текущий список на три части: элементы меньше опорного, равные опорному и больше
# опорного. В списке [5, 8, 9, 4, 2, 9, 1, 8] опорным элементом будет число 8 (крайнее правое), а получить надо три
# списка: [5, 4, 2, 1]; [8, 8]; [9, 9]. Для списка с элементами меньше опорного ([5, 4, 2, 1]) и списка с элементами
# больше опорного ([9, 9]) выполните те же шаги заново — запустите рекурсию. результат_1 = рекурсия([5, 4, 2,
# 1]). результат_2 = [8, 8]. результат_3 = рекурсия([9, 9]). Сложите результаты вызова рекурсий и получите
# отсортированный список: отсортированный_список = результат_1 + результат_2 + результат_3. Пример с разбором
# алгоритма выше (как сработала рекурсия)
#
# С [9, 9] всё просто. Элементов меньше или больше опорного нет, поэтому рекурсия не пойдёт глубже, а вызов рекурсии
# по списку [9, 9] быстро завершится и вернёт этот же список (его и не нужно было сортировать).
#
# С [5, 4, 2, 1] рекурсия пойдёт вглубь:
#
# Первый шаг— [5, 4, 2, 1]:
# опорным элементом выбирается число 1;
# меньше 1 элементов нет (значит, рекурсия по ним продолжаться не будет);
# помимо опорного элемента, других равных нет, получаем список [1];
# больше 1 все остальные элементы [5, 4, 2] — с этим списком будет вызвана рекурсия.
# Второй шаг— [5, 4, 2]:
# опорный элемент — 2;
# меньше опорного — [];
# равные опорному — [2];
# больше опорного — [5, 4].
# Третий шаг— [5, 4]:
# опорный элемент — 4;
# меньше — [];
# равны — [4];
# больше — [5].
# Четвёртый шаг — [5]:
# меньше — [];
# равны — [5];
# больше — [].
# Тут вызовы завершаются, мы соединяем списки и возвращаем список [5] на уровень выше (в вызов с числами [5, 4]).
#
# Там мы соединяем списки [] + [4] + [5] и получаем [4, 5]. Этот список возвращаем ещё на уровень выше (в вызов с
# числами [5, 4, 2]).
#
# Опять складываем списки:
#
# [ ] + [2] + [4, 5] = [2, 4, 5].
#
# Этот список возвращаем в вызов на уровень выше (тот, который был запущен с [5, 4, 2, 1]).
#
# Складываем списки:
#
# [ ] + [1] + [2, 4, 5] = [1, 2, 4, 5].
#
# Возвращаем [1, 2, 4, 5] в самый первый вызов, где мы выполняли следующие вызовы:
#
# результат_1 = рекурсия([5, 4, 2, 1]).
#
# результат_2 = [8, 8].
#
# результат_3 = рекурсия([9, 9]).
#
# В итоге после выполнения всех рекурсий получаем:
#
# результат_1 = [1, 2, 4, 5].
#
# результат_2 = [8, 8].
#
# результат_3 = [9, 9].
#
# Складываем все списки:
#
# [1, 2, 4, 5] + [8, 8] + [9, 9] = [1, 2, 4, 5, 8, 8, 9, 9].
#
# Этот полный список возвращается наружу — туда, где функция была вызвана изначально.
#
# Напишите функцию, которая реализует этот алгоритм. Для удобства добавьте вспомогательную функцию, пусть она
# принимает на вход список, а возвращает три списка (с элементами меньше, равными и больше опорного).
#
# Пример работы такой функции:
#
# числа = [4, 9, 2, 7, 5]
#
# вспомогательная_функция(числа) → [4, 2], [5], [9, 7]
 #
# Эту функцию можно будет использовать в основной-рекурсивной, чтобы код основной функции стал проще и понятнее.
