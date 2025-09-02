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
        
    def entryValidation(self, date, otherParty, grossAmt):
        if self.dateCheck(date):
            if self.numCheck(grossAmt):
                grossAmt = self.numCheck(grossAmt)
                if self.numCheck(otherParty):
                    otherParty = self.numCheck(otherParty)
                else:
                    return "Incorrect Format: $ Other Parties"
            else:
                return "Incorrect Format: Gross Earned"
        else:
            return "Incorrect Format: Closing Date"
        print(date)
        print(otherParty)
        print(grossAmt)

    def dateCheck(self,str):
        try: 
            datetime.datetime.strptime(str, "%m/%d/%y")
            return True
        except:
            return False