#!/usr/bin/env python3

import logging

from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL


class CommonLogger:

    def __init__(self, logger_name):
        self._logger_level = logging.DEBUG
        self._format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self._logger_name = logger_name
        self._logger = None
        self._logger = self.__prepare_logger()

    @property
    def file_formatter(self):
        """Create formatter."""
        return logging.Formatter(self._format)

    @property
    def logger_name(self):
        return self._logger_name

    @property
    def logger_level(self):
        return self._logger_level

    @logger_level.setter
    def logger_level(self, value):
        if value in (DEBUG, INFO, WARNING, ERROR, CRITICAL):
            self._logger_level = value
            for handler in self._logger.handlers:
                handler.setLevel(self._logger_level)

    @staticmethod
    def __prepare_handler(file_name, log_level, log_format):
        file_handler = logging.FileHandler(file_name)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(logging.Formatter(log_format))
        return file_handler

    def __prepare_logger(self):
        if self._logger is None:
            logger = logging.getLogger(self.logger_name)
            logger.setLevel(self._logger_level)
            return logger
        return self._logger

    def add_handler(self, file_name, log_level=logging.INFO, log_format=None):
        if log_format is None:
            log_format = self._format
        self._logger.addHandler(self.__prepare_handler(file_name, log_level, log_format))

    def add_handlers_for_each_level(self, file_name):
        self.add_handler(f'debug_{file_name}.log', logging.DEBUG)
        self.add_handler(f'info_{file_name}.log', logging.INFO)
        self.add_handler(f'warning_{file_name}.log', logging.WARNING)
        self.add_handler(f'error_{file_name}.log', logging.ERROR)
        self.add_handler(f'critical_{file_name}.log', logging.CRITICAL)

    # Wrapping methods.
    def debug(self, message):
        self._logger.debug(message)

    def info(self, message):
        self._logger.info(message)

    def warning(self, message):
        self._logger.warning(message)

    def error(self, message):
        self._logger.error(message)

    def critical(self, message):
        self._logger.critical(message)


def main():
    logger = CommonLogger('test_logger')
    logger.add_handlers_for_each_level('simple')
    logger.debug('Debugging now...')
    logger.info('Informing now...')
    logger.warning('Warning now...')
    logger.error('Error now...')
    logger.critical('Critical now...')
    logger.info('Bye cruel world.')


if __name__ == '__main__':
    main()
