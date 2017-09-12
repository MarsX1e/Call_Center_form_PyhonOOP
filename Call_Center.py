class Call(object):
    def __init__(self,caller_name,caller_phone_number,time_of_call,reason_for_call):
        self.unique_id=None
        self.caller_name=caller_name
        self.caller_phone_number=caller_phone_number
        self.time_of_call=time_of_call
        self.reason_for_call=reason_for_call
    def display(self):
        print "unique id is",str(self.unique_id())
        print "caller's name is",self.caller_name
        print "phone number is",self.caller_phone_number
        print "it came in at",self.time_of_call
        print "it calls because",self.reason_for_call
class CallCenter(object):
    def __init__(self):
        self.calls=[]
        self.queue_size=len(self.calls)
    def add(self,call):
        self.calls.append(call)
        self.queue_size=len(self.calls)
        call.unique_id=self.queue_size
        return self
    def remove(self):
        self.calls.pop(0)
        self.queue_size=len(self.calls)
        return self
    def info(self):
        for number in self.calls:
            print number.caller_name,"from",str(number.caller_phone_number)
        return self
    def kill(self,number):
        for indx in range(0,len(self.calls)):
            if self.calls[indx].caller_phone_number==number:
                self.calls.pop(indx)
    def sort(self):
        end=len(self.calls)
        print end
        for value in range(1,end):
            callername=0
            print value
            for count in range(0,len(self.calls)-1):
                if self.calls[count].unique_id>self.calls[count+1].unique_id:
                    temp=self.calls[count].unique_id
                    self.calls[count].unique_id=self.calls[count+1].unique_id
                    self.calls[count+1].unique_id=temp           
        return self
Jack=Call("Jack","234-123-4567","13:21","shit in pants")
Johnson=Call("Johnson","213-123-8654","14,11","choke on candy")
Brain=Call("Bran","123-126-3355","14:45","I need money")
nineoneone=CallCenter()
nineoneone.add(Jack).add(Johnson).add(Brain)
print nineoneone.info()
nineoneone.sort().info()


'''
def take_call():
    print "What is your name?"
    name = raw_input()
    print "What is your reason for calling?"
    reason = raw_input()
    print "Please confirm your phone number"
    num = raw_input()
    print "Please stay on the line while we proccess your call"
    return Call(name, num, reason)
Here is using rawinput to add call. 

'''