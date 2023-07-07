from get_data import get_data

from tests.abv_test import abv_test
from tests.name_test import name_test
from tests.image_url_test import image_url_test
from tests.ibu_test import ibu_test
from tests.utils import check_if_value_higher_or_equal


if __name__ == '__main__':
    json_data = get_data()
    passed, failed = abv_test(json_data)
    passed,failed = name_test(json_data)
    passed, failed = image_url_test(json_data)
    passed, failed = ibu_test(json_data)





