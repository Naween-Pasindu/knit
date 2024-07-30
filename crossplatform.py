import os

if os.name == 'posix':  # For Unix-like systems
    import pwd
    import grp
    # Unix-specific code here
elif os.name == 'nt':  # For Windows
    import win32security
    # Windows-specific code here