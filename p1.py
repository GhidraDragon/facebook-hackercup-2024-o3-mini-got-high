def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    
    for case in range(1, t + 1):
        n = int(data[index])
        k = int(data[index+1])
        index += 2
        times = []
        for _ in range(n):
            times.append(int(data[index]))
            index += 1
            
        times.sort()  # sort in increasing order
        
        total_time = 0
        # Use iterative greedy strategy
        while n > 3:
            # Option 1: send the two fastest then return fastest
            costA = times[0] + 2 * times[1] + times[n-1]
            # Option 2: send fastest with slowest and return fastest twice
            costB = 2 * times[0] + times[n-2] + times[n-1]
            total_time += min(costA, costB)
            n -= 2  # two slowest are moved to the other side
            
        if n == 3:
            total_time += times[0] + times[1] + times[2]
        elif n == 2:
            total_time += times[1]
        elif n == 1:
            total_time += times[0]
            
        result = "YES" if total_time <= k else "NO"
        results.append(f"Case #{case}: {result}")
    
    sys.stdout.write("\n".join(results))
    
if __name__ == '__main__':
    solve()