###################################################
# MySQL connector wrapper for Python 3            #
# by Xicheng Jia, Spring 2018 @Valley Stream, NY  #
###################################################
"""A DBI class Inherited from mysql.connector.MySQLConnection
The Target of this class is to avoid adding password in every code
to initialize the DB connection. The DB credentials were saved in
YAML file and can be referenced by host:port or any meaningful keys
Example:
  import libjxc
  dbh = libjxc.db('127.0.0.1:3306')
  dc = dbh.dict_cursor()
  dc.execute('SELECT user, host FROM mysql.user')
  ret = dc.fetchone()
  print(ret)
  dbh.close()
"""

from mysql.connector import MySQLConnection, errors
import yaml
import os

_config_file = os.path.dirname(__file__) + '/db_config.yml'

class db(MySQLConnection):
  def __init__(self, db_link, **kwargs):
    """Read DB credential from YAML file and initialize the DB"""
    self._dblink = db_link
    try:
      with open(_config_file, 'r') as f: doc = yaml.load(f)
      if db_link in doc:
        """Merged **kwargs, can overwrite the preset args"""
        for k,v in kwargs.items():
          doc[db_link].update({k: v})
        super(db, self).__init__(**doc[db_link])
      else:
        """Must have a db_link entry to access DB through this module"""
        raise ValueError("{} does not have an entry!".format(db_link))
    except:
      raise 
 
  def dict_cursor(self):
    """Return cursor go through the resultset as a dictionary"""
    return self.cursor(dictionary=True)

  @property
  def hostname(self):
    return self._host

  @property
  def dblink(self):
    return self._dblink

  @dblink.setter
  def dblink(self, value):
    self._dblink = value

