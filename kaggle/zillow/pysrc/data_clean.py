import pandas as pd
import numpy as np
import time

def clean_flow(df):
    df = pd.concat([df, ex_nannum_feat(df)], axis=1)
    df = binary_clean(df)
    df = drop_same_feature(df)
    return df

def ex_nannum_feat(df):
    t = time.time()
    print('extract nannum feat ...')
    nannum_feat = pd.DataFrame()
    for i in ['A','H','P','T','N','G','M','F']:
        cols = [c for c in df.columns if i in c]
        nannum_feat['*%s_nannum'%i] = df[cols].T.isnull().sum()
    nannum_feat['*total_nannum'] = nannum_feat.sum(axis=1)
    print('------  cost time %.2f seconds'%(time.time()-t))
    return nannum_feat

def binary_clean(df):
    t = time.time()
    print('binary feature clean ...')
    for c in df.columns:
        if df[c].nunique()==1:
            df.loc[df[c].notnull(),c] = 1
            print('convert %s'%c)
        if c[0] == 'F':
            df.loc[df[c].notnull(),c] = 1
            print('convert %s'%c)
    print('------  cost time %.2f seconds'%(time.time()-t))
    return df

def drop_same_feature(df):
    t = time.time()
    print('drop_same_feature ...')
    cols = df.columns
    cols_len = len(cols)
    for i in range(cols_len-1):
        for j in range(1,cols_len-i):
            try:
                corr = abs(df[[cols[i],cols[i+j]]].corr().iloc[0,1])
                if corr > 0.99:
                    if df[cols[i]].isnull().sum()<df[cols[i+j]].isnull().sum():
                        col = cols[i]
                        col_drop = cols[i+j]
                    else:
                        col = cols[i+j]
                        col_drop = cols[i]
                    df[col] = df[col].fillna(df[col_drop])
                    df = df.drop(col_drop, axis=1)
                    print('leave feature:%s ,drop feature: %s'%(col,col_drop))
            except:
                pass
    print('------  cost time %.2f seconds'%(time.time()-t))
    return df
    
            
    
    