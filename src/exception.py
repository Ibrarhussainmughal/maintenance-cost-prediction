"""
Exception classes for the maintenance cost prediction project
"""

class CustomException(Exception):
    """Base exception class for the project"""
    
    def __init__(self, error_message: str, error_detail=None):
        """
        Initialize custom exception
        
        Args:
            error_message: Error message
            error_detail: Additional error details
        """
        super().__init__(error_message)
        self.error_message = error_message
        
        if error_detail:
            import sys
            _, _, exc_tb = sys.exc_info()
            
            if exc_tb:
                file_name = exc_tb.tb_frame.f_code.co_filename
                line_number = exc_tb.tb_lineno
                
                self.error_message = f"Error occurred in script: [{file_name}] at line [{line_number}]: {error_message}"
    
    def __str__(self):
        return self.error_message

class DataIngestionException(CustomException):
    """Exception raised during data ingestion"""
    pass

class DataTransformationException(CustomException):
    """Exception raised during data transformation"""
    pass

class ModelTrainerException(CustomException):
    """Exception raised during model training"""
    pass

class PredictionException(CustomException):
    """Exception raised during prediction"""
    pass
