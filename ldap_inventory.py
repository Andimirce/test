#!/usr/bin/env python3
from ldap3 import Server, Connection, ALL
import json

LDAP_SERVER = 'ldap://'CPTR-DC1.commprog.com
USER = 'commprog\\ansible_user'
PASSWORD = 'Celsi$olNota22!'
BASE_DN = 'DC=commprog,DC=com'

server = Server(LDAP_SERVER, get_info=ALL)
conn = Connection(server, USER, PASSWORD, auto_bind=True)
conn.search(BASE_DN, '(objectClass=computer)', attributes=['dNSHostName'])

hosts = [e['attributes']['dNSHostName'] for e in conn.response if 'dNSHostName' in e['attributes']]

inventory = {
    "all": {
        "hosts": hosts,
        "vars": {}
    }
}

print(json.dumps(inventory, indent=2))
