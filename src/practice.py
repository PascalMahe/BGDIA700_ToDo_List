
import logging
from string import Template

logging.basicConfig(filename='practice.log',
                    encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s | %(levelname)-8s | %(filename)s.%(funcName)s l.%(lineno)d | %(message)s')


def diviser(a: int, b: int) -> int:
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    logging.debug("Nona")
    logging.info("Paul")
    logging.warning("G1deon")
    logging.error("Duty")
    logging.critical("John")
    return a / b


dct = {'asctime': 'one',
       'levelname': 'end',
       'filename': 'One',
       'funcName': 'flesh'}

# concatenating strings
final_str = "%(filename)12s %(funcName)-12s %(asctime)s %(levelname)s" % dct
print(final_str)

logging.debug("Gideon")
logging.info("Harrowhark")
logging.warning("Sexpal")
logging.error("Mercymorn")
logging.critical("John")
print(diviser(10, 3))
