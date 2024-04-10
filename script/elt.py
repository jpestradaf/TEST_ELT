import subprocess
import time

#run connection process (async)
def wait_for_postgres(host, max_retries=3, delay_seconds=3):
    retries=0
    while retries < max_retries:
        try:
            result = subprocess.run(
                ["pg_isready", "-h", host],
                check=True,
                capture_output=True, text=True
            )
            if "accepting connection" in result.stdout:
                print("Postgres connected")
                return True
        except subprocess.CalledProcessError as e:
            print(f'Postgres error: {e}')
            retries += 1
            print(
                f'Retrying in {delay_seconds} seconds... (Attempt {retries}/{max_retries})'
            )
            time.sleep(delay_seconds)
    print("Max retries has been reached. Code Exit!")
    return False       

if not wait_for_postgres(host='init_postgres'):
    exit(1)
     
#debugger
print('script running...!')

#Configuration from init (source) postgreSQL
source_config = {
    'dbname': 'source_db',
    'user': 'postgres',
    'password': 'secret',
    'host': 'init_postgres'}

#Configuration from last (dest) postgreSQL
dest_config = {
    'dbname': 'dest_db',
    'user': 'postgres',
    'password': 'secret',
    'host': 'last_postgres'}

s_command = ['pg_dump', 
 '-U', source_config['user'],
 '-h', source_config['host'],
 '-d', source_config['dbname'],
 '-f', 'data_dump.sql',
 '-w'  
]

subprocess_env = dict(PGPASSWORD=source_config['password'], check=True)

# async process - source
subprocess.run(s_command, env=subprocess_env)

d_command = ['psql', 
 '-U', dest_config['user'],
 '-h', dest_config['host'],
 '-d', dest_config['dbname'],
 '-f', 'data_dump.sql',
 '-a'  
]

subprocess_env = dict(PGPASSWORD=dest_config['password'], check=True)

# async process - dest
subprocess.run(d_command, env=subprocess_env)

#debugger
print('Ending script...!')