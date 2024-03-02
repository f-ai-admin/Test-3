import pandas as pd

path = "C:\\Users\\user\\Downloads\\Convert_pdf_file_into_the_excel_file\\Rule_Setup\\Accounting_Library\\B_Setup\\B_1_Ledger_Setup\\"

class LedgerManager:
    def __init__(self):
        
        self.main_df = pd.read_excel(path+'Output_Ledger_Library.xlsx', engine='openpyxl')

    def enter_and_retrieve_ledger(self, C5):
        if C5.lower() in list(self.main_df['C5']):
            print(f"Ledger Name {C5} already present")
            c1 = self.main_df.loc[self.main_df['C5'] == C5, 'C1'].iloc[0]
            c2 = self.main_df.loc[self.main_df['C5'] == C5, 'C2'].iloc[0]
            c3 = self.main_df.loc[self.main_df['C5'] == C5, 'C3'].iloc[0]
            return c1, c2, c3

        C3 = input("Enter C3 (Account Name): ")
        C4 = input("Enter C4 (Sub ledger): ")
        
        if (self.main_df.loc[self.main_df['C3'] == C3, 'C5'] == '').any(): 
            if C4.lower() == 'none':
                self.main_df.loc[self.main_df['C3'] == C3, 'C4'] = C3
            else:
                self.main_df.loc[self.main_df['C3'] == C3, 'C4'] = C4

            self.main_df.loc[self.main_df['C3'] == C3, 'C5'] = C5.lower()
            c1 = self.main_df.loc[self.main_df['C3'] == C3, 'C1'].iloc[0]
            c2 = self.main_df.loc[self.main_df['C3'] == C3, 'C2'].iloc[0]
            c3 = self.main_df.loc[self.main_df['C3'] == C3, 'C3'].iloc[0]
            c4 = self.main_df.loc[self.main_df['C3'] == C3, 'C4'].iloc[0]
            c5 = self.main_df.loc[self.main_df['C3'] == C3, 'C5'].iloc[0]
            self.main_df.to_excel(path+'Output_Ledger_Library.xlsx',index = False)
            return c1, c2, c3

        else:
            if C4.lower() == 'none':
                C4 = C3
            
            c1 = self.main_df[self.main_df['C3'] == C3]['C1'].iloc[0]
            c2 = self.main_df[self.main_df['C3'] == C3]['C2'].iloc[0]
            c3 = self.main_df[self.main_df['C3'] == C3]['C3'].iloc[0]
            g_code = self.main_df[self.main_df['C3'] == C3]['G_CODE'].iloc[0]

            new_data = {'C1': c1, 'C2': c2, 'C3': c3, 'C4': C4, 'C5': C5.lower(), 'G_CODE': g_code}
            self.main_df = self.main_df.append(new_data, ignore_index=True)
            self.main_df.to_excel(path+'Output_Ledger_Library.xlsx',index = False)
            return c1, c2, c3
