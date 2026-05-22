from scraper import convert_rating

def test_convert_rating():
    assert convert_rating("One") == 1
    assert convert_rating("Three") == 3
    assert convert_rating("Five") == 5
