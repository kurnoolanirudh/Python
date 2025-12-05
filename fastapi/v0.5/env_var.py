# to create environment variable in the OS 
# export TRIAL_ENV="WORLD" in the linux terminal
# in the above command if export is not used then the variable will only be alive for that terminal session



# to read the env variable set in the OS.
import os 

# any value read in Python from an environment variable will be a str
env_var = os.getenv('TRIAL_ENV', 'World') # World is the default value in case TRIAL_ENV does not exist
print(f"HELLO, {env_var}")