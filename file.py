import pyodbc
import pandas as pd
import requests as req
import os.path


# conn_str = ("Driver={SQL Server Native Client 11.0};"
# conn_str = ("Driver={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.0.so.1.1};"
conn_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=ofadev.id;"
            "Database=dbRMTools_Dev3;"
            "UID=sa;"
            "PWD=smo4dm1n;")
conn = pyodbc.connect(conn_str)
# print(conn)

# df = pd.read_sql_query('SELECT id, post_title, post_status, guid, post_mime_type FROM Tbl_Ren_Paper_Post WHERE NULLIF(post_mime_type, '') IS NOT NULL', conn)
df = pd.read_sql_query("SELECT * FROM Tbl_Ren_Paper_Post WHERE NULLIF(post_mime_type, ' ') IS NOT NULL", conn)
# print(df)
print(df.guid)
print(df.post_mime_type)

# url = df.guid
url= "http://www.computersolution.tech/wp-content/uploads/2016/05/tutorialspoint-logo.png"
r = req.get(url, allow_redirects=True)
if url.find('/'):
    # print(url.rsplit('/', 1)[1])
    filename = url.rsplit('/', 1)[1]
    filedir = 'wwwroot/' + filename

    file_exists = os.path.exists(filedir)

    if file_exists:
        print(file_exists)
        print(f'The file {filedir} exists')
    else :
        print(f'The file {filedir} does not exist')
        open(filedir, 'wb').write(r.content)

