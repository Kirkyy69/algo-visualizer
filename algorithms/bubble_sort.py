NAME = "Bubble Sort" 
TYPE = "sort"

def run(numbers):
    steps = []
    data = numbers.copy()
    steps.append({ 
        "type": "finished",  
        "array": data.copy()

    })
    return steps