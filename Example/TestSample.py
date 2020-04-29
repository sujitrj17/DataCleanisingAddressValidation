# https://towardsdatascience.com/data-handling-using-pandas-cleaning-and-processing-3aa657dc9418
# https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
import easypost

import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt

easypost.api_key="EZTKeaeb3b17185d489bb4eff3f20505377065H3f3SXeH0VXvy0gE0dsQ"
plt.style.use('ggplot')

pd.options.mode.chained_assignment = None

# read the data
df = pd.read_excel(r'D:\Data Science\Sumasoft_AIML\extract 4-9.xlsx')
df = df.set_index('Sold-to party')
# print(df.shape)
# print(df.dtypes)
# print('done')
'''
# With this we can find total number of missing values for each column.
print(df.isna().sum())

# Adding another .sum() returns the total number of null values in the data-set.
print(df.isna().sum().sum())

# replacing all nan values.
# Another method to fill the missing value could be ffill method, which propagates last valid observation to the next.
# Similarly bfill method uses next observation to fill gap.
replaced  = df[['Name 2']].fillna(999).values

# replacing na values with string
df['Name 1'].fillna('missing')

# duplicate removal
duplicate_rows_df = df[df.duplicated()]
print ("number of duplicate rows: ", duplicate_rows_df.shape)

duplicated_rows_specificCol= df[df.duplicated(['Name 1'])]
print ("number of duplicate rows for name 1 col: ",duplicated_rows_specificCol.shape)

# finding notna values from full or specific col
notNA_valuesFrom_2rd_col = df['Name 2'].notna()
print(notNA_valuesFrom_2rd_col)


s= pd.Series([1,2,3])
s.loc[0] = None

# creating new column 'indexed' and stores in it.
df['indexed'] = df['Name 2'].str.find('C/O',0)

# df['AddrVerify'] =
'''
print('**************************************************************************************')

# df['IsAddrValid'] = df['Abstract'].apply(lambda text: keywords(text, ratio=0.15, split=True))
# print(address.get("verifications").get("delivery").get("success"))
# print(address.values())
# 417 MONTGOMERY ST FL 5


def addressVerifier(street1,street2,city,state,zip,country,company,phone):
    address = easypost.Address.create(verify=["delivery"],street1=street1,street2=street2,city=city,state=state,zip=zip,country=country,company=company,phone=phone)
    return address

# print("DATA>>",street1,street2,city,state,zip,country,company,phone)

def checker(index_label):
    return index_label

for index_label, row_series in df.iterrows():
    apiOutput = addressVerifier(row_series['Street'],"",row_series['City'],"",row_series['PostalCode'],row_series['Country'],row_series['Name 1'],"")
    df.at[index_label , 'IsAddrValid'] = apiOutput.get("verifications").get("delivery").get("success")
    df.at[index_label,'State'] = apiOutput.get('state')
    df.at[index_label,'CompanyName_Json'] = apiOutput.get('company')
    df.at[index_label, 'JsonOutput'] = apiOutput
    # print(row_series['Street'],"",row_series['City'],"",row_series['PostalCode'],row_series['Country'],row_series['Name 1'],"")
    # df.at[index_label, 'IsAddrValid'] = checker(index_label)

# for index_label, row_series in df.iterrows():
#     print(row_series['Name 1'])

df.to_excel(r'D:\Data Science\Sumasoft_AIML\OTF_AddrValidations78.xlsx',index=False)
