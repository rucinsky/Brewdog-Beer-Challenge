import logging
from .utils import check_if_value_not_null, check_if_not_empty_string, check_if_value_is_int, check_if_value_higher_or_equal
from get_logger import get_logger


def ibu_test(data:list)->(int,int):
    logger = get_logger('ibu-test')
    logger.info(f"Starting IBU test")
    checked = len(data)
    failed = 0
    for beer in data:
        if not check_if_value_not_null(beer.get('ibu')):
            logger.error(f"Beer {beer.get('id')}: ibu value is null")
            failed = failed + 1
            continue # No need for other tests, we know it's null already, so it's for sure not a double or empty string

        if not check_if_not_empty_string(beer.get('ibu')):
            logger.error(f"Beer {beer.get('id')}: ibu value is an empty string")
            failed = failed + 1
            continue

        if not check_if_value_is_int(beer.get('ibu')):
            logger.warning(f"Beer {beer.get('id')}: ibu value is not an int, it's {type(beer.get('ibu'))}")
            failed = failed + 1
            continue

        compare_value = 0
        if not check_if_value_higher_or_equal(beer.get('ibu'), compare_value):
            logger.warning(f"Beer {beer.get('id')}: ibu value is lower than {compare_value}")
            failed = failed + 1

    passed = checked - failed

    logger.info(f"Finished ABV test")
    logger.info(f"Tested: {checked}")
    logger.info(f"Passed: {passed}")
    logger.info(f"Failed: {failed}")

    return (passed,failed)




