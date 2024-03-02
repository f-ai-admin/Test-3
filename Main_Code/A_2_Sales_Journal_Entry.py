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
        self.sys_a = Asset_Expense_Rule()
        self.sys_b = Liability_Capital_Revenue_Rule()
        self.ledger = LedgerManager()

    def process_entries(self, k):
        for i in range(len(self.df)):
            en = self.df.iloc[i]
            tx = en['Tax']
            date = en['Invoice Date']
            invoice_number = en['Invoice Number']
            journal_number = 'S00' + str(i)

            def To_Entry():
                l1 = en['To']
                print(l1)
                c1, c2, c3 = self.ledger.enter_and_retrieve_ledger(l1.lower())
            
                if c1 == 'ASSET' or c1 == 'EXPENSE':
                    dr = self.sys_a.debit_transaction(en['Total'])
                    cr = 0
                else:
                    dr = self.sys_b.debit_transaction(en['Total'])
                    cr = 0

                k['J9 - Description/Narration'].append('Sales')
                k['J3 - Invoice_Ref_Number'].append(invoice_number)
                k['J4 - Ledger_Name'].append(l1)
                k['J2 - Date'].append(date)
                k['J1 - Journal Number'].append(journal_number)
                k['J6 - Dr Amount'].append(dr)
                k['J7 - Cr Amount'].append(cr)

            def tax_igst_entry():
                igst_c5 = 'tax igst' + ' ' + str(tx) + '%'
                print(igst_c5)
                c1, c2, c3 = self.ledger.enter_and_retrieve_ledger(igst_c5.lower())

                amu = en['Tax IGST']
                if c1 == 'ASSET' or c1 == 'EXPENSE':
                    cr = self.sys_a.credit_transaction(amu)
                    dr = 0
                else:
                    cr = self.sys_b.credit_transaction(amu)
                    dr = 0

                k['J9 - Description/Narration'].append('Sales')
                k['J3 - Invoice_Ref_Number'].append(invoice_number)
                k['J4 - Ledger_Name'].append(igst_c5)
                k['J2 - Date'].append(date)
                k['J1 - Journal Number'].append(journal_number)
                k['J7 - Cr Amount'].append(cr)
                k['J6 - Dr Amount'].append(dr)

            def tax_cgst_entry():
                cgst_c5 = 'tax cgst' + ' ' + str(tx) + '%'
                c1, c2, c3 = self.ledger.enter_and_retrieve_ledger(cgst_c5.lower())

                if c1 == 'ASSET' or c1 == 'EXPENSE':
                    tc = en['Tax CGST']
                    cr = self.sys_a.credit_transaction(tc)
                    dr = 0
                else:
                    tc = en['Tax CGST']
                    cr = self.sys_b.credit_transaction(tc)
                    dr = 0

                k['J9 - Description/Narration'].append('Sales')
                k['J3 - Invoice_Ref_Number'].append(invoice_number)
                k['J4 - Ledger_Name'].append(cgst_c5)
                k['J2 - Date'].append(date)
                k['J1 - Journal Number'].append(journal_number)
                k['J7 - Cr Amount'].append(cr)
                k['J6 - Dr Amount'].append(dr)

            def To_Sales():
                sales = 'To Sales'
                print(sales)
                c1, c2, c3 = self.ledger.enter_and_retrieve_ledger(sales.lower())

                if c1 == 'ASSET' or c1 == 'EXPENSE':
                    amu = en['Amount']
                    cr = self.sys_a.credit_transaction(amu)
                    dr = 0
                else:
                    amu = en['Amount']
                    cr = self.sys_b.credit_transaction(amu)
                    dr = 0

                k['J9 - Description/Narration'].append('Sales')
                k['J3 - Invoice_Ref_Number'].append(invoice_number)
                k['J4 - Ledger_Name'].append(sales)
                k['J2 - Date'].append(date)
                k['J1 - Journal Number'].append(journal_number)
                k['J7 - Cr Amount'].append(cr)
                k['J6 - Dr Amount'].append(dr)

            To_Entry()
            tax_igst_entry()
            tax_cgst_entry()
            To_Sales()
            print("==========================================================================")
            print()

# Usage
# processor = JournalEntryProcessor(df, main_df)
# processor.process_entries()
