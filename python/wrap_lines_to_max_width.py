
from textwrap import TextWrapper

def wrap_lines(max_width: int, input_file: str) -> None:
    """
    Wrap lines in a file to the given max width
    """
    output_file = f'{input_file}_wrapped'
    wrapper = TextWrapper(width=max_width, initial_indent=' ', subsequent_indent=' ')
    with open(input_file, mode='r') as file:
        lines = [line.strip() for line in file.readlines()]
    
    wrapped_lines = wrapper.wrap(' '.join(lines))

    with open(output_file, mode='w') as new_file:
        new_file.write('\n'.join(wrapped_lines) + '\n')
