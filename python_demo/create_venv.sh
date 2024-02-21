# create a virtual environment for the project

# create a virtual environment
python3 -m venv venv

# activate the virtual environment
source venv/bin/activate

# update pip after activating the virtual environment
pip install --upgrade pip

# install the required packages if the requirements.txt file exists
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi


################################USAGE###################################
# chmod +x create_venv.sh###otherwise you'll get permission denied######
# source create_venv.sh
################################DESCRIPTION#############################
# The source command is used to execute the script######################
# in the current shell environment.#####################################
########################################################################





#  to deactivate the virtual environment, run the following command:
# deactivate

