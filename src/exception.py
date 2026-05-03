import sys
import logging
#Error msg details to be displayed when an exception occurs
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
     # for 0,1,2 placeholder in above line

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message
    

# if __name__=="__main__": 

#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e,sys)
#THIS WAS DONE TO TEST EXCEPTION

    # This will be common for the entire Project you can just use this exception wherever you use try-catch block