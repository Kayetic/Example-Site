import time

# Get the current time and date
timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')

# Construct the file name with the timestamp
filename = f'data_{timestamp}.txt'

# Save the text to the file
with open(filename, 'w') as f:
    f.write('Hello, World!')
