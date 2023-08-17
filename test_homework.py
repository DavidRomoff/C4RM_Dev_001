import sqlite3

def test_math():

  # Read the SQL code from the file
  with open('math.sql', 'r') as file:
      sql_query = file.read().strip()

  # Create an in-memory database
  conn = sqlite3.connect(':memory:')

  # Execute the SQL code from the file
  result = conn.execute(sql_query).fetchone()

  # Close the connection
  conn.close()

  # Extact the answer
  answer = result[0]

  # Check the answer
  assert(answer == 10)

def test_text():

  # Read the SQL code from the file
  with open('text.sql', 'r') as file:
      sql_query = file.read().strip()

  # Create an in-memory database
  conn = sqlite3.connect(':memory:')

  # Execute the SQL code from the file
  result = conn.execute(sql_query).fetchone()

  # Close the connection
  conn.close()

  # Extact the answer
  answer = result[0]

  # Check the answer
  assert(answer == 'way')