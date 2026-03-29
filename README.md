# Pipeline CLI

Simple CLI tool to process numbers using a chain of operations.

## Available operations

- even — keep even numbers
- odd — keep odd numbers
- double — multiply each number by 2
- square — square each number
- sort — sort numbers

## Run

```bash
python pipeline_cli.py
```

## Input

- Enter numbers separated by space
- Enter operations separated by space

### Example

nums: 1 2 3 4 5  
operations: even double

## Help

Type `help` in operations input to show available operations again.

## Example output

input: 1, 2, 3, 4, 5  
operations: even, double  
result: 4, 8
