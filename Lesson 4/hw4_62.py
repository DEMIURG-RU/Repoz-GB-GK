from itertools import islice, count, cycle

def my_fun(ch_st, ch_stp, ch_rp):
    try:
        ch_st, ch_stp, ch_rp = int(ch_st), int(ch_stp), int(ch_rp)
        m_l = [ch for ch in islice(count(), ch_st, ch_stp + 1)]
        r_l = iter(ch for ch in cycle(m_l))
        rpt_l = [next(r_l) for _ in range(ch_rp)]
        print(m_l)
        return rpt_l
    except ValueError:
        return "Значение ошибочное"
    except TypeError:
        return "Ошибка типа"

print(my_fun(input('Укажите число с которго начнем: '), input('Введите до какого числа: '), input('Количество операций (ограничтель): ')))