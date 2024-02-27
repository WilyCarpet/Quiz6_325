store_inventory = []

class OrderDetails:
    def __init__(self,customerInfo, items, shipAddr):
        self.customerInfo = customerInfo
        self.items = items
        self.shipAddr = shipAddr
    
    def storeCustomerInfo(self, customerInfo):
        self.customerInfo = customerInfo
    
    def storeItems(self,items):
        self.items = items
    
    def storeShippingAddress(self, shipAddr):
        self.shipAddr = shipAddr

    def getCustomerInfo(self):
        return self.customerInfo
    
    def getItems(self):
        return self.items
    
    def getShippingAddress(self):
        return self.shipAddr
    
class ManageInventory:
    def __init__(self,inventroy):
        self.inventory = inventroy

    def checkInventory(self, orderDetails):
        for inv in self.inventory: 
            if inv == orderDetails.items:
                if inv.supply > 0:
                    return True
                else:
                    return False
        #If item in order detail is not listed in inventory
        return False
    
    def updateInventory(self,orderDetails):
        for item in orderDetails.items:
            for inv in self.inventory:
                #after order, update inventory of products bought
                if inv == item:
                    inv.supply -= 1


class OrderValidation:
    def __init__(self, orderDetails):
        self.orderDetails = orderDetails
    
    def checkavailability(self):
        available = ManageInventory().checkInventory(self.orderDetails)
        return available
    

    
    
class EmailSender:
    def __init__(self,email_service):
        self.email_service = email_service
    
    def sendConfirmation(self, OrderDetails, email):
        #Generate email content beased on order
        self.email_service.send_email(email, "Order Confirmation")


class CalculateTotal:
    def __init__(self, taxRate):
        self.taxRate = taxRate

    def calculateTotal(self,orderDetails):
        subtotal = sum(item.price for item in orderDetails.items)
        tax = subtotal * self.taxRate
        return subtotal + tax


class Order:
    def __init__(self, taxRate, email_service,user,shipAddr):
        self.items = []
        self.user = user
        self.orderDetails = OrderDetails(user.info,self.items,shipAddr)
        self.manageInventory = ManageInventory(store_inventory)
        self.orderValidation = OrderValidation(self.orderDetails)
        self.EmailSender = EmailSender(email_service)
        self.CalculateTotal = CalculateTotal(taxRate)

    def addToOrder(self, item):
        self.items.append(item)
    
    def checkout(self):
        if self.orderValidation.checkavailability():
            self.manageInventory.updateInventory(self.orderDetails)
            self.CalculateTotal.calculateTotal(self.orderDetails)
            self.EmailSender.sendConfirmation(self.orderDetails,self.user.email)
        else:
            print('Error has occured at checkout')



