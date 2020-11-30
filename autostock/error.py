class AutoStockException(Exception):
    """Base exception class for autostock
    """
    pass
class FileNotFoundException(AutoStockException):
    """Exception that's thrown When a file fails to load or there is no file
    """
    pass
class StockNameNotFoundException(AutoStockException):
    """Exception that's thrown When a stock is not found'
    """
    pass
