import logging
from .utils import check_if_value_not_null, check_if_not_empty_string, check_if_website_is_up
from get_logger import get_logger


def image_url_test(data: list) -> (int, int):
    logger = get_logger('image-url-test')
    logger.info(f"Starting Image URL test")
    checked = len(data)
    failed = 0
    for beer in data:

        if not check_if_value_not_null(beer.get('image_url')):
            logger.error(f"Beer {beer.get('id')}: image_url value is null")
            failed = failed + 1
            continue  # No need for other tests, we know it's null already, so it's for sure not a double or empty string

        if not check_if_not_empty_string(beer.get('image_url')):
            logger.error(f"Beer {beer.get('id')}: image_url value is an empty string")
            failed = failed + 1
            continue

        if not check_if_website_is_up(beer.get('image_url')):
            logger.error(f"Beer {beer.get('id')}: image is not accessible")



    passed = checked - failed

    logger.info(f"Finished Name test")
    logger.info(f"Tested: {checked}")
    logger.info(f"Passed: {passed}")
    logger.info(f"Failed: {failed}")

    return (passed, failed)

