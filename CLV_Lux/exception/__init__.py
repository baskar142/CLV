# exception/__init__.py

import os
import sys

def error_message_detail(error, error_detail: sys):
    """
    Create a detailed error message with file name, line number, and error content.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error in script: [{file_name}] at line [{line_number}] — {str(error)}"
    return error_message


class CLVException(Exception):
    """
    Custom Exception class for the CLV project
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
