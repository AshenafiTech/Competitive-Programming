class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)  # Find the maximum cost in the array
        count = [0] * (max_cost + 1)  # Frequency array
        
        # Fill frequency array
        for cost in costs:
            count[cost] += 1
        
        ice_cream_count = 0  # Number of ice creams bought
        
        # Iterate over the cost values in sorted order
        for cost in range(1, max_cost + 1):
            if count[cost] > 0:
                # Determine how many we can buy at this price
                num_to_buy = min(count[cost], coins // cost)
                ice_cream_count += num_to_buy
                coins -= num_to_buy * cost  # Deduct coins
                
                if coins == 0:  # Stop if we run out of money
                    break
        
        return ice_cream_count
