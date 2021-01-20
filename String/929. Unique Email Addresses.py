class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #1. iterate each email
        #2. implement cleaning
        #4. record it in the dict
        #5. return the length of the dict
        
        def formated(email):
            first_name, domain_name = email.split('@')
            first_name = first_name.replace('.','')
            for i in range(len(first_name)):
                if first_name[i]=='+':
                    first_name = first_name[:i]
                    break
            return first_name +'@' + domain_name
        
        visited = set()
        for email in emails:
            email = formated(email)
            if email in visited:
                continue
            else:
                visited.add(email)
        
        return len(visited)


https://leetcode.com/problems/unique-email-addresses/