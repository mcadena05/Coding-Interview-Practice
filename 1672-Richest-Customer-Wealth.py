def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        temp = 0

        for account in accounts:
            for j in range(len(account)):
                temp += account[j]
            
            if temp > wealth:
                wealth = temp
            
            temp = 0
        return wealth    