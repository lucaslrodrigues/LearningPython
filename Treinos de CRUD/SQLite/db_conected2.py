import logging

def fetch_data(self):
    connection = self.connect()
    cursor = connection.cursor()
    self.init_cursor(cursor)
    logging.info("Importando pedidos pro ERP")
    cursor.execute(
        '''
            select * from users
        '''
    )
    data = self.row2json(cursor)
