from main import text_stat, prime_numbers, roman_numerals_to_int


def test_prime_number():
    assert prime_numbers(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert prime_numbers(50, 100) == [53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert prime_numbers(44, 11) == []
    assert prime_numbers(2, 'f') == []


def test_roman_numerals_to_int():
    assert roman_numerals_to_int('XXIV') == 24
    assert roman_numerals_to_int('LXXXIX') == 89
    assert roman_numerals_to_int('MMXXIII') == 2023
    assert roman_numerals_to_int('ZXC') == None


def test_text_stat():
    assert text_stat('idk') == {'error': 'Ошибка чтения файла'}
    assert text_stat('testtext1.txt') == {'а': (1, 1), 'word_amount': 1, 'paragraph_amount': 1,
                                          'bilingual_word_amount': 0}
    assert text_stat('testtext2.txt') == {'а': (0.5, 1), 'a': (0.5, 1), 'word_amount': 1, 'paragraph_amount': 1,
                                          'bilingual_word_amount': 1}
    assert text_stat('testtext3.txt') == {'е': (0.2, 1.0), 'м': (0.1, 0.5), 'с': (0.1, 0.5), 'в': (0.2, 1.0), 'п': (0.1, 0.5), 'и': (
        0.1, 0.5), 't': (0.1, 0.5), 'р': (0.1, 0.5), 'word_amount': 2, 'paragraph_amount': 1, 'bilingual_word_amount': 1}
    assert text_stat('testtext4.txt') == {'п': (0.0380952380952381, 0.15789473684210525), 'р': (0.06666666666666667, 0.3157894736842105), 'ы': (0.0380952380952381, 0.21052631578947367), 'л': (0.0380952380952381, 0.21052631578947367), 'й': (0.01904761904761905, 0.10526315789473684), 'е': (0.06666666666666667, 0.2631578947368421), 'т': (0.047619047619047616, 0.15789473684210525), 'и': (0.0380952380952381, 0.15789473684210525), 'в': (0.0761904761904762, 0.3684210526315789), 'д': (0.06666666666666667, 0.3684210526315789), 'о': (0.08571428571428572, 0.42105263157894735), 'к': (0.0380952380952381, 0.15789473684210525), 'а': (0.12380952380952381, 0.5789473684210527), 'н': (
        0.05714285714285714, 0.3157894736842105), 'с': (0.01904761904761905, 0.10526315789473684), 'ь': (0.02857142857142857, 0.15789473684210525), 'з': (0.01904761904761905, 0.10526315789473684), 'я': (0.01904761904761905, 0.10526315789473684), 'б': (0.009523809523809525, 0.05263157894736842), 'ж': (0.01904761904761905, 0.10526315789473684), 'г': (0.01904761904761905, 0.10526315789473684), 'ч': (0.009523809523809525, 0.05263157894736842), 'ю': (0.01904761904761905, 0.10526315789473684), 'у': (0.01904761904761905, 0.05263157894736842), 'ш': (0.009523809523809525, 0.05263157894736842), 'м': (0.009523809523809525, 0.05263157894736842), 'word_amount': 19, 'paragraph_amount': 2, 'bilingual_word_amount': 0}