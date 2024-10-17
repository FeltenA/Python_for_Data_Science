import os
import time


def ft_tqdm(lst: range) -> None:
    """Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested."""

    terminal_size = os.get_terminal_size().columns
    length = len(list(lst))
    start_time = time.time()

    for i, item in enumerate(lst, start=1):
        bar_size = terminal_size - 5
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time
        remaining = (length - i) / speed
        m_elapsed, s_elapsed = divmod(elapsed_time, 60)
        m_remaining, s_remaining = divmod(remaining, 60)
        time_info = f"| {i}/{length} [{m_elapsed:02.0f}:{s_elapsed:02.0f}"
        time_info += f"<{m_remaining:02.0f}:{s_remaining:02.0f}"
        time_info += f", {speed:6.2f}it/s]"
        bar_size -= len(time_info)
        progress = f"{i / length:4.0%}|"
        progress += f"{'█' * int(i / length * bar_size):<{bar_size}}"
        print("\r" + progress + time_info, end="", flush=True)
        yield item
