class Solution:

    def deleteDuplicates(self, head):
    
        if head == None:
        
            return head
    
        temp = head 
    
        while(temp.next):
        
            if(temp.val == temp.next.val):
            
                temp.next = temp.next.next
                
            else:
            
                temp = temp.next 
    
        return head
