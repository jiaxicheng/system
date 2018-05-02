###################################################
# MySQL connector wrapper for Python 3            #
# by Xicheng Jia, Spring 2018 @Valley Stream, NY  #
###################################################
"""SQL related funcions to simplify creating database queries
"""
_insert_types = {
    'insert': 'INSERT',
    'replace': 'REPLACE',
    'insert_ignore': 'INSERT IGNORE'
}

def set_insert_sql(table, *fields, insert_type='insert'):
  """Generate SQL to INSERT/REPLACE/INSERT IGNORE row data into table
  Example:
    import libjxc
    fields = ['user', 'host', 'passwd']
    SQL_INSERT_IGNORE = libjxc.set_insert_sql('test.user', *fields, insert_type='insert_ignore')
    ...
    # below 'row' is a dictionary( i.e. a line feed from CSV file)
    # cursor is from MySQL db handler
      data = [ row[k] if k in row else '' for k in fields ]
      cursor.execute(SQL_INSERT_IGNORE, data)
    ...
  """
  return "{} INTO {} ({}) VALUES ({})".format(
      _insert_types[insert_type.lower().replace(' ', '_')]
    , table
    , ", ".join(fields)
    , ", ".join(['%s'] * len(fields))
  )


