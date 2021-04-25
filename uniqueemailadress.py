class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        #seperate the local and domain name
        
        
        
        emails_set = set()
        
        for email in emails:
            
            #split it into local and domain name
            
            split_email = email.split("@")
            
            local = split_email[0]
            domain = "@" + split_email[1]
            
            #split local + sign and remove it
            local = local.split("+")[0]
            
            #split local again on . and ignore it
            local = "".join(local.split("."))
            
            #readd local and domain and add it to the set
            
            new_email = local + domain
            print(new_email)
            emails_set.add(new_email)
            
        
        #return length
        return len(emails_set)
        
