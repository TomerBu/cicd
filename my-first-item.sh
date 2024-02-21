#!/bin/bash
# the shebang line is the path to the bash interpreter

# Create directory if it doesn't exist
if [ ! -d "demo-ci-cd" ]; then
  mkdir demo-ci-cd
fi

# Move into the directory
cd demo-ci-cd

# Define the file name using Jenkins build number
filename="time_${BUILD_NUMBER}.txt"

# Write the current date and time to a file
echo "Current Date and Time: $(date)" > $filename

# Display the contents of the file
cat $filename
