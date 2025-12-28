from typing import List


def simple_moving_average(values: List[float], window: int) -> List[float]:
    """Return simple moving average (SMA) of the input values.

    The returned list has the same length as `values`. The first `window-1`
    entries will be `None` to indicate insufficient data for the window.
    """
    if window <= 0:
        raise ValueError("window must be > 0")
    if not values:
        return []

    sma: List[float] = [None] * len(values)  # type: ignore
    cumsum = 0.0
    for i, v in enumerate(values):
        cumsum += v
        if i >= window:
            cumsum -= values[i - window]
        if i >= window - 1:
            sma[i] = cumsum / window
    return sma
