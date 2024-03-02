from B_Setup.B_1_Ledger_Setup.Customize_Ledger_Library import LedgerManager
import sys
import os

# Assuming LedgerManager is in B_1_Ledger_Setup directory
from B_Setup.B_1_Ledger_Setup.Customize_Ledger_Library import LedgerManager

# Assuming Asset_Expense_Rule and Liability_Capital_Revenue_Rule are in A_Rule_Engine directory
from A_Rule_Engine.A_3_Debit_Credit_Rule import Asset_Expense_Rule, Liability_Capital_Revenue_Rule

class JournalEntryProcessor:
    def __init__(self, df, main_df):
        self.df = df
        self.main_df = main_df
        self.asset_expense = Asset_Expense_Rule()
        self.liability_capital_revenue =  Liability_Capital_Revenue_Rule()
        self.ledger = LedgerManager()

    def process_entries(self,k):
        for i in range(len(self.df)):
            print("Entry Number - " + str(i))
            en = self.df.iloc[i]
            tx = en['Tax']
            date = en['Invoice Date']
            invoice_number = en['Invoice Number']
            journal_number = 'P00' + str(i+1)

            def To_Entry():
                l1 = en['Description']
                print("Ledger Name - ", l1)

                c1, c2, c3 = self.ledger.enter_and_retrieve_ledger(l1.lower())

                if c1 == 'ASSET' or c1 == 'EXPENSE':
                    dr = self.asset_expense.debit_transaction(en['Amount'])
                    cr = 0

                else :
                    dr = self.liability_capital_revenue.debit_transaction(en['Amount'])
                    cr = 0

                
                k['J9 - Description/Narration'].append('purchase')
                k['J3 - Invoice_Ref_Number'].append(invoice_number)
                k['J4 - Ledger_Name'].append(l1)
                k['J2 - Date'].append(date)
                k['J1 - Journal Number'].append(journal_number)

                k['J6 - Dr Amount'].append(dr)
                k['J7 - Cr Amount'].append(cr)

            

            def tax_igst_entry():
                igst_c5 = 'tax igst' + ' ' + str(tx) + '%'
                print("Ledger Name - ", igst_c5)

                c1, c2, c3 = self.ledger.enter_and_retrieve_ledger(igst_c5.lower())

                if c1 == 'ASSET' or c1 == 'EXPENSE':
                    amu = en['IGST']
                    dr = self.asset_expense.debit_transaction(amu)
                    cr = 0

                else:
                    amu = en['IGST']
                    dr = self.liability_capital_revenue.debit_transaction(amu)
                    cr = 0
                    

                k['J9 - Description/Narration'].append('purchase')
                k['J3 - Invoice_Ref_Number'].append(invoice_number)
                k['J4 - Ledger_Name'].append(igst_c5)
                k['J2 - Date'].append(date)
                k['J1 - Journal Number'].append(journal_number)

                k['J7 - Cr Amount'].append(cr)
                k['J6 - Dr Amount'].append(dr)

            def tax_cgst_entry():
                cgst_c5 = 'tax cgst' + ' ' + str(tx) + '%'
                print("Ledger Name - ", cgst_c5)

                c1, c2, c3 = self.ledger.enter_and_retrieve_ledger(cgst_c5.lower())

                if c1 == 'ASSET' or c1 == 'EXPENSE':
                    tc = en['SGST']
                    dr = self.asset_expense.debit_transaction(tc)
                    cr = 0

                else:
                    tc = en['SGST']
                    dr = self.liability_capital_revenue.debit_transaction(tc)
                    cr = 0
                    
                
                k['J9 - Description/Narration'].append('purchase')
                k['J3 - Invoice_Ref_Number'].append(invoice_number)
                k['J4 - Ledger_Name'].append(cgst_c5)
                k['J2 - Date'].append(date)
                k['J1 - Journal Number'].append(journal_number)

                k['J7 - Cr Amount'].append(cr)
                k['J6 - Dr Amount'].append(dr)

            def To_purchase():
                purchase =   en['Sold By']
                print("Ledger Name - ", purchase)

                c1, c2, c3 = self.ledger.enter_and_retrieve_ledger(purchase.lower())

                if c1 == 'ASSET' or c1 == 'EXPENSE':
                    amu = en['Total']
                    cr = self.asset_expense.credit_transaction(amu)
                    dr = 0

                else:
                    amu = en['Total']
                    cr = self.liability_capital_revenue.credit_transaction(amu)
                    dr = 0

                
                k['J9 - Description/Narration'].append('purchase')
                k['J3 - Invoice_Ref_Number'].append(invoice_number)
                k['J4 - Ledger_Name'].append(purchase)
                k['J2 - Date'].append(date)
                k['J1 - Journal Number'].append(journal_number)

                k['J7 - Cr Amount'].append(cr)
                k['J6 - Dr Amount'].append(dr)

            def To_purchase_item():
                purchase = en['Sold By']
                print("Ledger Name - ", purchase)

                c1, c2, c3 = self.ledger.enter_and_retrieve_ledger(purchase.lower())

                if c1 == 'ASSET' or c1 == 'EXPENSE':
                    amu = en['Total']
                    dr = self.asset_expense.debit_transaction(amu)
                    cr = 0

                else:
                    amu = en['Total']
                    dr = self.liability_capital_revenue.debit_transaction(amu)
                    cr = 0

                
                k['J9 - Description/Narration'].append('purchase')
                k['J3 - Invoice_Ref_Number'].append(invoice_number)
                k['J4 - Ledger_Name'].append(purchase)
                k['J2 - Date'].append(date)
                journal_number = 'P00' + str(i) + str(i)
                k['J1 - Journal Number'].append(journal_number)

                k['J7 - Cr Amount'].append(cr)
                k['J6 - Dr Amount'].append(dr)

            def To_Bank():
                purchase = 'To Bank'
                print("Ledger Name - ", purchase)

                c1, c2, c3 = self.ledger.enter_and_retrieve_ledger(purchase.lower())

                if c1 == 'ASSET' or c1 == 'EXPENSE':
                    amu = en['Total']
                    cr = self.asset_expense.credit_transaction(amu)
                    dr = 0

                else:
                    amu = en['Total']
                    cr = self.liability_capital_revenue.credit_transaction(amu)
                    dr = 0

           
                k['J9 - Description/Narration'].append('purchase')
                k['J3 - Invoice_Ref_Number'].append(invoice_number)
                k['J4 - Ledger_Name'].append(purchase)
                k['J2 - Date'].append(date)
                journal_number = 'P00' + str(i+1) + str(i+1)
                k['J1 - Journal Number'].append(journal_number)

                k['J7 - Cr Amount'].append(cr)
                k['J6 - Dr Amount'].append(dr)

            To_Entry()
            tax_igst_entry()
            tax_cgst_entry()
            To_purchase()
            To_purchase_item()
            To_Bank()
            print("==========================================================================")
            print()



# processor = JournalEntryProcessor(df, main_df)
# processor.process_entries()
