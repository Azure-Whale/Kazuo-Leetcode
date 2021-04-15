"""
Run a database query and employee ID's from a database
call an API to get their address one emloyee at a time
write the the employee addresses to a json formatted file (one write)
"""

import boto3
import json
from boto3 import session
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Employee')
some_id = 1
some_name = 'a'
res = table.eq({'EmployeeID':some_id,'Employee_name':some_name})
"""
SELECT ID, Name
FROM Employee
"""
from flask import Flask, request

app = Flask(__name__)
import mysql.connector

if __name__ == '__main__':
    app.run(debug=True)

    @app.route('api.abcd.com/address/id=<employee_id>', methods=['GET'])
    def api_get_address(employee_id):
        connect = mysql.connector.connect(user='..', password='password',
                              host='127.0.0.1',
                              database='employees')
        request.args.get('id')
        cursor = connect.cursor()
        sql_1 = 'SELECT Address FROM Employee WHERE ID = {}'.format(employee_id)
        res = cursor.execute(sql_1).findAll()
        return res



def write_information(res):
    with open('....some file','w') as f:
        f.write(json.dumps(res,indent=4))