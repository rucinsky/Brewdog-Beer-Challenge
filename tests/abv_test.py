import logging
from .utils import check_if_value_not_null, check_if_not_empty_string, check_if_value_is_float, check_if_value_higher
from get_logger import get_logger


def abv_test(data:list)->(int,int):
    logger = get_logger('abv-test')
    logger.info(f"Starting ABV test")
    checked = len(data)
    failed = 0
    for beer in data:

        if not check_if_value_not_null(beer.get('abv')):
            logger.error(f"Beer {beer.get('id')}: abv value is null")
            failed = failed + 1
            continue # No need for other tests, we know it's null already, so it's for sure not a double or empty string

        if not check_if_not_empty_string(beer.get('abv')):
            logger.error(f"Beer {beer.get('id')}: abv value is an empty string")
            failed = failed + 1
            continue

        if not check_if_value_is_float(beer.get('abv')):
            logger.warning(f"Beer {beer.get('id')}: abv value is not a float, it's {type(beer.get('abv'))}")
            failed = failed + 1
            continue

        compare_value = float(4.0)
        if not check_if_value_higher(beer.get('abv'), compare_value):
            logger.warning(f"Beer {beer.get('id')}: abv value is lower than {compare_value}")
            failed = failed + 1

    passed = checked - failed

    logger.info(f"Finished ABV test")
    logger.info(f"Tested: {checked}")
    logger.info(f"Passed: {passed}")
    logger.info(f"Failed: {failed}")

    return (passed,failed)




