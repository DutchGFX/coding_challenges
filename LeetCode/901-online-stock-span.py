class StockSpanner:

    def __init__(self):
        self.stack = []  # stack such that stack[i] < stack[i+1]
        self.cnt = -1  # index of the current day. -1 since we don't have any days yet

    def append(self, price: int):
        """
        Increments the counter and appends a new stock to the stack

        Parameters
        ----------
        price : int
            price of the stock on the current day
        """
        self.cnt += 1
        self.stack.append((price, self.cnt))

    def next(self, price: int) -> int:
        """
        We are going to create a monotonic stack, where `stack[i] > stack[i+1]` for all `i`.
        Our goal is to find the most recent day that has a higher price than today.
        - If the price today is less than the price yesterday, we are done, and the span is 1
        - If the price is higher, the span is at least the span of the previous day, so we are OK that we've already
        popped those items off the stack
        - In essence, our stack contains the most recent price that is greater than the next item in the stack

        Parameters
        ----------
        price : int
            price of the stock today

        Returns
        -------
        span : int
            number of days (incl. today) where the price is <= today's price
        """

        # if the first iteration, append to stack and return
        # the default value of span=1
        if not self.stack:
            self.append(price)
            return 1

        # we know that every value after index stack[-1][0] is DECREASING,
        # so if we are larger than this, our span is at least that.
        while self.stack and price >= self.stack[-1][0]:
            _, idx = self.stack.pop(-1)

        # if no values were larger, set prev index to -1
        idx = self.stack[-1][1] if self.stack else -1

        # append the price
        self.append(price)
        return self.cnt - idx
