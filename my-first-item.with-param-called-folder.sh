#!/bin/bash
# the shebang line is the path to the bash interpreter

# Create directory if it doesn't exist
if [ ! -d $folder ]; then
  mkdir $folder
fi

# Move into the directory
cd $folder

# Define the file name using Jenkins build number
filename="time_${BUILD_NUMBER}.txt"

# Write the current date and time to a file
echo "Current Date and Time: $(date)" > $filename

# Display the contents of the file
cat $filename
