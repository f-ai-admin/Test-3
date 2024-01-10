config = {
    'account_types': {
        'ASSET': {'balance_type': 'DEBIT'},
        'INCOME': {'balance_type': 'CREDIT'},
        'LIABILITY': {'balance_type': 'CREDIT'},
        'EXPENSE': {'balance_type': 'DEBIT'},
        'CAPITAL':{'balance_type': 'CREDIT'},
        'REVENUE':{'balance_type': 'DEBIT'}
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


import pandas as pd


asset ,  lia  , exp ,  rev  =  [],[],[],[]
sub_account_asset,  sub_account_lia,  sub_account_exp,  sub_account_rev = [],[],[],[]
asset_balance_type, lia_balance_type, exp_balance_type, rev_balance_type   = [],[],[],[]

for i in config['accounts']:
    if 'ASSET' in list(list(config['accounts'][i].values())[0].values())[0]['type']:
        sub_account_asset.append(list(list(config['accounts'][i].values())[0].keys())[0])
        c = list(list(config['accounts'][i].values())[0].keys())[0]
        asset.append(i+ ' - ' + c)
        asset_balance_type.append(config['account_types']['ASSET']['balance_type'])

    if 'LIABILITY' in list(list(config['accounts'][i].values())[0].values())[0]['type']:
        sub_account_lia.append(list(list(config['accounts'][i].values())[0].keys())[0])
        c = list(list(config['accounts'][i].values())[0].keys())[0]
        lia.append(i+ ' - ' + c)
        lia_balance_type.append(config['account_types']['LIABILITY']['balance_type'])

    if 'EXPENSE' in list(list(config['accounts'][i].values())[0].values())[0]['type']:
        sub_account_exp.append(list(list(config['accounts'][i].values())[0].keys())[0])
        c = list(list(config['accounts'][i].values())[0].keys())[0]
        exp.append(i+ ' - ' + c)
        exp_balance_type.append(config['account_types']['EXPENSE']['balance_type'])

    if 'REVENUE' in list(list(config['accounts'][i].values())[0].values())[0]['type']:
        sub_account_rev.append(list(list(config['accounts'][i].values())[0].keys())[0])
        c = list(list(config['accounts'][i].values())[0].keys())[0]
        rev.append(i+ ' - ' + c)
        rev_balance_type.append(config['account_types']['REVENUE']['balance_type'])


max_len = max(len(asset), len(lia), len(exp))

# Pad the shorter lists with None values to make them of equal length
asset += [None] * (max_len - len(asset))
lia += [None] * (max_len - len(lia))
exp += [None] * (max_len - len(exp))
rev += [None] * (max_len - len(rev))


sub_account_asset+= [None] * (max_len - len(sub_account_asset))
sub_account_lia+= [None] * (max_len - len(sub_account_lia))
sub_account_exp+= [None] * (max_len - len(sub_account_exp))
sub_account_rev+= [None] * (max_len - len(sub_account_rev))

asset_balance_type+= [None] * (max_len - len(asset_balance_type))
lia_balance_type+= [None] * (max_len - len(lia_balance_type))
exp_balance_type+= [None] * (max_len - len(exp_balance_type))
rev_balance_type+= [None] * (max_len - len(rev_balance_type))

pd.DataFrame({
        'ASSET':asset,
        'Asset Balance type':asset_balance_type,
        'LIABILITY':lia,
        'liability Balance type':lia_balance_type,
        'EXPENSE':exp,
        'Expense Balance type':exp_balance_type,
        'REVENUE':rev,
        'Revenue Balance Type':rev_balance_type,
        # 'ASSET Sub Category':sub_account_asset,
        # 'LIABILITY Sub Category': sub_account_lia,
        # 'EXPENSE  Sub Category':sub_account_exp,
        
})









