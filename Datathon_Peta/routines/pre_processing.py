
##########
# File: pre_processing.py
# Description:
#    Rotina de preprocessamento
##########



import sys
sys.path.append('../libraries/')


from pre_processing_vendas import pre_vendas
from pre_processing_macro import pre_macro
from merge_datasets import merge_df

from holidays import get_holidays
from adjust_datetime import next_holiday



def pre_proc(df_vendas, df_macro):
    
    
    df_vendas = pre_vendas(df_vendas)
    df_macro = pre_macro(df_macro)
    df = merge_df(df_vendas, df_macro)
    
    #holidays = get_holidays()
    #last_holiday = filter(lambda x: x>df.index[-1], holidays)[0]
    df['Next_holiday'] = next_holiday(df)
    
    #keep_cols
    return df



