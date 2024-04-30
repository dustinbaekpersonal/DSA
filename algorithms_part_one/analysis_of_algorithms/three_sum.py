"""Python implementation of three sum."""
import logging
import time
import random

logging.basicConfig(level=logging.INFO)

class ThreeSum:
    """Find all combinations of three integers whose sum is zero."""
    def __init__(self, array: list[int]):
        self.array = array
    
    def brute_force_find_combination(self) -> int:
        """Brute force approach to append combinations of three integers whose sum is zero to result list."""
        if len(self.array) < 3:
            raise ValueError("Input array should have at least three integers.")

        result = []
        for i in range(len(self.array)):
            for j in range(i+1, len(self.array)):
                for k in range(j+1, len(self.array)):
                    if (self.array[i] + self.array[j] + self.array[k]) == 0:
                        result.append((self.array[i], self.array[j], self.array[k]))
                        # logging.info(f"{result}")
        return len(result)
        
if __name__ == "__main__":
    # input_integers: list[int] = [30, -40, -20, -10, 40, 0, 10, 5]
    
    N = 1_000
    input_integers = [random.randint(-100, 100) for _ in range(N)]
    logging.info(f"Input integers: {input_integers}")
    ts = ThreeSum(array=input_integers)
    start = time.time()
    res = ts.brute_force_find_combination()
    end = time.time()
    print(res)
    print("Time taken", end-start)