import logging

# Setup logging
logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_and_print(msg):
    print(msg)
    logging.info(msg)
