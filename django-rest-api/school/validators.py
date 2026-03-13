import re
from validate_docbr import CPF

def invalid_cpf(cpf_number):
    cpf = CPF()
    valid_cpf = cpf.validate(cpf_number)
    return not valid_cpf
    
def invalid_first_name(first_name):
    return not first_name.isalpha()

def invalid_last_name(last_name):
    return not last_name.isalpha()

def invalid_cell_phone_number(cell_phone_number):
    # Assuming cell phone number should be 13 digits long
    # 86 99999-9999 (including area code)
    pattern = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    result = re.findall(pattern, cell_phone_number)
    return not result