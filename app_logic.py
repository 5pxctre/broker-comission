import math
import datetime
from database import Database

class AppLogic:
    def __init__(self):
        self.db = Database()

    def numCheck(self, x):
        if x:
            x = "".join(x.split())
            x = x.replace(",", "").replace("$", "")
            try:
                val = float(x)
                if val >= 0:
                    return val
                return False
            except ValueError:
                return False
        return False

    def entryValidation(self, date, otherParty, grossAmt, address):
        if not self.dateCheck(date):
            raise ValueError("Incorrect Format: Closing Date")
        
        grossVal = self.numCheck(grossAmt)
        if grossVal is False:
            raise ValueError("Incorrect Format: Gross Earned")
        
        partyVal = self.numCheck(otherParty)
        if partyVal is False:
            if otherParty == "" or otherParty is None:
                partyVal = 0.0
            else:
                raise ValueError("Incorrect Format: $ Other Parties")
        
        if not address:
            raise ValueError("Incorrect Format: Address Input Required")
        
        split, commission, cap_Contribution = self.split_calc(grossVal, partyVal)

        # --- CHANGED: Passing 'partyVal' (Other Parties) to DB ---
        self.db.add_listing(address, grossVal, split, commission, partyVal)

        return "Data recorded", split, commission, cap_Contribution
    
    def fetch_history(self):
        return self.db.get_all_listings()

    def dateCheck(self, str):
        try: 
            datetime.datetime.strptime(str, "%m/%d/%y")
            return True
        except:
            return False
        
    def split_calc(self, gross, otherParty):
        commission = gross - otherParty
        split = commission * 0.2
        commission = round(commission, 2)
        split = round(split, 2)
        cap_Contribution = split
        return split, commission, cap_Contribution