import math
import datetime


class AppLogic:
    
    def numCheck(self, x):
        if x:
            x = "".join(x.split())
            x = x.replace(",", "")
            if x[0] == "$" and (x.count("$") == 1):
                x = x.replace("$", "")
            x = x.replace(".", "")
            if not x.isdigit():
                return False
            x = float(x)
            if x >= 0:
                return x
            else:
                return False
        else:
            return False
        

    def entryValidation(self, date, otherParty, grossAmt, address):
        if not self.dateCheck(date):
            raise ValueError("Incorrect Format: Closing Date")
        
        if not self.numCheck(grossAmt):
            raise ValueError("Incorrect Format: Gross Earned")
        
        if not self.numCheck(otherParty):
            raise ValueError("Incorrect Format: $ Other Parties")
        
        if not address:
            raise ValueError("Incorrect Format: Address Input Required")
        
        split, comission, cap_Contribution = self.split_calc(self.numCheck(grossAmt),self.numCheck(otherParty))
        return "Data recorded", split, comission, cap_Contribution
    
    
    """  def entryValidation(self, date, otherParty, grossAmt,address):
        if self.dateCheck(date):
            if self.numCheck(grossAmt):
                grossAmt = self.numCheck(grossAmt)
                if self.numCheck(otherParty):
                    otherParty = self.numCheck(otherParty)
                    if address:
                        pass
                    else:
                        return "Incorrect Format: Address input required"
                else:
                    return "Incorrect Format: $ Other Parties"
            else:
                return "Incorrect Format: Gross Earned"
        else:
            return "Incorrect Format: Closing Date"
        spl, com, capcon = self.split_calc(grossAmt, otherParty)
        return "Data recorded", spl, com, capcon"""
    
    def dateCheck(self,str):
        try: 
            datetime.datetime.strptime(str, "%m/%d/%y")
            return True
        except:
            return False
        
    def split_calc(self, gross, otherParty):
        comission = gross - otherParty
        split = comission * 0.2
        comission = round(comission, 2)
        split = round(split, 2)
        cap_Contribution = split
        return split, comission, cap_Contribution