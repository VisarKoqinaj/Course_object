#import of num2words lib
from num2words import num2words

#calculate the wage without taxes
def kalkulo_rrogen(emri:str, hour:float, rate:float=10)->None:
    """ This function calculates weekly wages.
        Emri is string, hour is float,
        returns a NoneType"""
    pay = hour * rate
    res_str = f'{emri} {pay}'
    return res_str

#calculate the taxes
def kalkulo_tatimin(rroga:str)->float:
    tatimin = float(rroga)* 0.1
    return tatimin

#calculate and return wage after taxes
def rroga_neto(emri, hour, rate, print_lang=0):
    resultati = kalkulo_rrogen(emri, hour, rate)
    rroga_bruto = resultati.split()[1]
    rroga_rroga = float(rroga_bruto) - kalkulo_tatimin(rroga_bruto)
    if print_lang==1:
        return emri, rroga_rroga,num2words(rroga_rroga)
    return emri, rroga_rroga

def main():
    while True:
        input_var = input('Please enter a name hours rate: ')
        if input_var=='stop':
            break
        print_var = input('Do you want to print numbers in text (0 or 1) ')

        input_var = input_var.split()
        name = input_var[0]
        hours = float(input_var[1])
        rate = float(input_var[2])

        print(rroga_neto(name,hours, rate, int(print_var)))
        
if __name__=='__main__':
    main()