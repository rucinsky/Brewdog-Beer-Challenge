import logging
from .utils import check_if_value_not_null, check_if_not_empty_string
from get_logger import get_logger


def name_test(data:list)->(int,int):
    logger = get_logger('name-test')
    logger.info(f"Starting Name test")
    checked = len(data)
    failed = 0
    for beer in data:
        if not check_if_value_not_null(beer.get('name')):
            logger.error(f"Beer {beer.get('id')}: name is null")
            failed = failed + 1
            continue # No need for other tests, we know it's null already, so it's for sure not an empty string

        if not check_if_not_empty_string(beer.get('name')):
            logger.error(f"Beer {beer.get('id')}: name is an empty string")
            failed = failed + 1
            continue

    passed = checked - failed

    logger.info(f"Finished Name test")
    logger.info(f"Tested: {checked}")
    logger.info(f"Passed: {passed}")
    logger.info(f"Failed: {failed}")

    return (passed,failed)

