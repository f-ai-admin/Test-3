import pandas as pd

config = {
    'account_types': {
        'ASSET': {'balance_type': 'DEBIT'},
        'EXPENSE': {'balance_type': 'DEBIT'},
        'INCOME': {'balance_type': 'CREDIT'},
        'LIABILITY': {'balance_type': 'CREDIT'},
        'CAPITAL':{'balance_type': 'CREDIT'},
        
    },
    

    'accounts': {
        'Cash': {'type':{'CurrentAsset':{'type':'ASSET'}}},
        'CashEquivalents': {'type':{'CurrentAsset':{'type':'ASSET'}}},
        'ShortTermDeposits': {'type':{'CurrentAsset':{'type':'ASSET'}}},
        'AccountsReceivables': {'type':{'CurrentAsset':{'type':'ASSET'}}},
        'Inventory': {'type':{'CurrentAsset':{'type':'ASSET'}}},
        'MarketableSecurities':{'type':{'CurrentAsset':{'type':'ASSET'}}},
        'OfficeSupplies':{'type':{'CurrentAsset':{'type':'ASSET'}}},
        'PrepaidExpenses':{'type':{'CurrentAsset':{'type':'ASSET'}}},

        'Land':{'type':{'FixedAsset':{'type':'ASSET'}}},
        'Building':{'type':{'FixedAsset':{'type':'ASSET'}}},
        'Machinery':{'type':{'FixedAsset':{'type':'ASSET'}}},
        'Equipment':{'type':{'FixedAsset':{'type':'ASSET'}}},
        'Patents':{'type':{'FixedAsset':{'type':'ASSET'}}},
        'Trademarks':{'type':{'FixedAsset':{'type':'ASSET'}}},
        'Goodwill':{'type':{'FixedAsset':{'type':'ASSET'}}},
        'Brand':{'type':{'FixedAsset':{'type':'ASSET'}}},
        'Copyrights':{'type':{'FixedAsset':{'type':'ASSET'}}},
        'Trade secrets':{'type':{'FixedAsset':{'type':'ASSET'}}},
        'Licenses And Permits':{'type':{'FixedAsset':{'type':'ASSET'}}},
        'Corporate Intellectual Property':{'type':{'FixedAsset':{'type':'ASSET'}}},


        'Accounts Payable':{'type':{'Current_Liability':{'type':'LIABILITY'}}},
        
        'Principal  & Interest ':{'type':{'Current_Liability':{'type':'LIABILITY'}}},
        'Outstanding_Salaries':{'type':{'Current_Liability':{'type':'LIABILITY'}}},
        'Wages':{'type':{'Current_Liability':{'type':'LIABILITY'}}},
        'Notes Payable':{'type':{'Current_Liability':{'type':'LIABILITY'}}},
        'Income Tax dues':{'type':{'Current_Liability':{'type':'LIABILITY'}}},
        'Mortagage':{'type':{'Current_Liability':{'type':'LIABILITY'}}},
        'Payroll':{'type':{'Current_Liability':{'type':'LIABILITY'}}},
        'Unearned income':{'type':{'Current_Liability':{'type':'LIABILITY'}}},
        'Accrued expenses':{'type':{'Current_Liability':{'type':'LIABILITY'}}},
        'Short Term Debt':{'type':{'Current_Liability':{'type':'LIABILITY'}}},

        'Principal':{'type':{'Long_Term_Liability':{'type':'LIABILITY'}}},
        'Bonds':{'type':{'Long_Term_Liability':{'type':'LIABILITY'}}},
        'Debentures':{'type':{'Long_Term_Liability':{'type':'LIABILITY'}}},
        'Long term loans':{'type':{'Long_Term_Liability':{'type':'LIABILITY'}}},
        'Deffered tax':{'type':{'Long_Term_Liability':{'type':'LIABILITY'}}},
        'Lease Payments':{'type':{'Long_Term_Liability':{'type':'LIABILITY'}}},
        'Pensions':{'type':{'Long_Term_Liability':{'type':'LIABILITY'}}},
        'Mortagage':{'type':{'Long_Term_Liability':{'type':'LIABILITY'}}},

        'Sales':{'type':{'Operating':{'type':'REVENUE'}}},
        'Rent revenue':{'type':{'Operating':{'type':'REVENUE'}}},
        'Dividend revenue':{'type':{'Operating':{'type':'REVENUE'}}},
        'Interest revenue':{'type':{'Operating':{'type':'REVENUE'}}},
        'Contra revenue':{'type':{'Operating':{'type':'REVENUE'}}},

        'Interest Income':{'type':{'Non-Operating':{'type':'REVENUE'}}},
        'Dividend Income':{'type':{'Non-Operating':{'type':'REVENUE'}}},
        'Rental Income':{'type':{'Non-Operating':{'type':'REVENUE'}}},
        'Gain on Sale of Assets':{'type':{'Non-Operating':{'type':'REVENUE'}}},
        'Royalty Income':{'type':{'Non-Operating':{'type':'REVENUE'}}},
        'Insurance Proceeds':{'type':{'Non-Operating':{'type':'REVENUE'}}},
        'Foreign Exchange Gains':{'type':{'Non-Operating':{'type':'REVENUE'}}},
        'Legal Settlements':{'type':{'Non-Operating':{'type':'REVENUE'}}},
        'Miscellaneous Income':{'type':{'Non-Operating':{'type':'REVENUE'}}},

        'Salaries':{'type':{'Operating':{'type':'EXPENSE'}}},
        'Wages':{'type':{'Operating':{'type':'EXPENSE'}}},
        'Marketing':{'type':{'Operating':{'type':'EXPENSE'}}},
        'Advertising':{'type':{'Operating':{'type':'EXPENSE'}}},
        'Promotion':{'type':{'Operating':{'type':'EXPENSE'}}},
        'Selling':{'type':{'Operating':{'type':'EXPENSE'}}},
        'general, and administrative (SG&A)':{'type':{'Operating':{'type':'EXPENSE'}}},
        'Rent and insurance':{'type':{'Operating':{'type':'EXPENSE'}}},
        'Depreciation and amortization':{'type':{'Operating':{'type':'EXPENSE'}}},
        'Other':{'type':{'Operating':{'type':'EXPENSE'}}},
        'Interest':{'type':{'Operating':{'type':'EXPENSE'}}},
        'Taxes':{'type':{'Operating':{'type':'EXPENSE'}}},
        'Impairment charges':{'type':{'Operating':{'type':'EXPENSE'}}},
        
        'Rent':{'type':{'Fixed':{'type':'EXPENSE'}}},
        'Salaries, benefits, and wages (sometimes fixed and sometimes variable)':{'type':{'Fixed':{'type':'EXPENSE'}}},

        'Transaction fees':{'type':{'Variable':{'type':'EXPENSE'}}},
        'Commissions':{'type':{'Variable':{'type':'EXPENSE'}}},
        'Marketing and advertising (sometimes fixed and sometimes variable)':{'type':{'Variable':{'type':'EXPENSE'}}},

        
}}

data = []

for account, details in config['accounts'].items():
    account_type = list(details['type'].values())[0]['type']
    C2  = (list(details['type'].keys())[0])
   
    # balance_type = config['account_types'][account_type]['balance_type']

    data.append({
        'C1': account_type,
        'C2':C2,
        'C3': account
        # 'Balance Type': balance_type
    })

df = pd.DataFrame(data)
df['C4'] = df['C5'] = 'NONE'
df['G_CODE'] = df['C1'].map({'ASSET': 'G1', 'LIABILITY': 'G2','EXPENSE':'G4','REVENUE':'G5'})
# df['G2'] = df['Account Type'].apply(lambda x: 'G1' if x == 'ASSET' else 'G2')

config2 = {

    'accounts':{
        "Owner's Capital Account":{'type':'Capital'},
        "Partner's Capital Account":{'type':'Capital'},
        "Common Stock Account":{'type':'Capital'},
        "Retained Earnings Account":{'type':'Capital'},
        "Treasury Stock Account":{'type':'Capital'},
        "Contributed Surplus Account":{'type':'Capital'},
        "Legal Reserve Account":{'type':'Capital'},
        "Preferred Stock Account":{'type':'Capital'},
        "Partner's Drawing Account":{'type':'Capital'},
        "Member's Capital Account (LLC)":{'type':'Capital'}


    }
    }


data = []

for account, details in config2['accounts'].items():
   
    c = list(details.values())[0]

    data.append({
        'C1': c,
        'C2':account,
        
    })

    df2 = pd.DataFrame(data)
    df2['C3'] = 'NONE'
    df2['C4'] = df2['C5'] = 'NONE'
    df2['G_CODE'] = df2['C1'].map({'Capital':'G3'})
    # df['G2'] = df['Account Type'].apply(lambda x: 'G1' if x == 'ASSET' else 'G2')



main_df = pd.concat([df, df2], ignore_index=True
main_df.to_excel('main_df.xlsx')



