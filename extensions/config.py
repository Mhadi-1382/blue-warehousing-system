
"""
Settings and configuration database
"""

from colorama import Fore
import MySQLdb
import os

try:
    mySQL = MySQLdb.connect(
        os.getenv('DB_HOST', 'localhost'),
        os.getenv('DB_USER', 'root'),
        os.getenv('DB_PASSWORD', ''),
        os.getenv('DB_NAME', 'blue')
    )
    
    print(Fore.GREEN + " * Database conected." + Fore.WHITE)
except:
    print(Fore.RED + " * Database not conect." + Fore.WHITE)
