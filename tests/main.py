import os
import subprocess

# Define the Docker Compose file path
compose_file_path = '../docker-compose.yml'

# Define the environment variables for the database configuration
db_user = 'devops'
db_password = 'password'
db_host = 'localhost'
db_port = 5432

def create_database():
    # Create the database using the pg_dump tool
    try:
        subprocess.run(['pg_dump', '-U', db_user, '-h', db_host, '-p', str(db_port), 'postgres', '-c', '-s', 'template1', '|', 'psql', '-U', db_user, '-h', db_host, '-p', str(db_port), 'mydb'])
    except subprocess.CalledProcessError as e:
        print(f"Failed to create database: {e}")

def main():
    # Create the database
    create_database()

if __name__ == '__main__':
    main()