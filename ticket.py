import json
class TicketDB(object):
    def createDB(self):
        self.db = {'dbversion': 1, 'activities': []}
    def loadDB(self,file):
        self.db = json.load(file)
    def saveDB(self,file):
        json.dump(self.db,file)
    def addActivity(self,activityName):
        """
        Usage: addActivity(<activity name>)
        Return value: Activity ID (string)
        """
        self.db['activities'].append({'activityName': activityName, 'tickets': {}})
        return len(self.db['activities'])-1
    def addTicket(self,activityID,ticketID):
        """
        Usage: addTicket(<activity name>, <ticket ID>)
        Return value: ticket ID
        """
        self.db['activities'][activityID]['tickets'][ticketID] = True
        return ticketID
    def editTicket(self,activityID,ticketID,enabled):
        self.db['activities'][activityID]['tickets'][ticketID] = enabled
    def checkTicket(self,activityID,ticketID):
        """
        Usage: checkTicket(<activity ID>, <ticket ID>)
        Return codes:
            0: OK
            1: Ticket Desabled
            2: Ticket Not Found
        """
        try:
            if self.db['activities'][activityID]['tickets'][ticketID] == True:
                del self.db['activities'][activityID]['tickets'][ticketID]
                return 0
            elif self.db['activities'][activityID]['tickets'][ticketID] == False:
                return 1
        except:
            return 2
