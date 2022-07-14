from datetime import datetime
from fdb import connect
import pandas


class Job:
    def __init__(self, database, user, pwd):
        self.con = connect(
            database,
            user=user,
            password=pwd,
            charset='UTF8'
        )
        self.cur = self.con.cursor()
        self.cur.execute(
            'select a.RDB$RELATION_NAME from RDB$RELATIONS a where COALESCE(RDB$SYSTEM_FLAG, 0) = 0 and RDB$RELATION_TYPE = 0'
        )
        self.tables = []
        for i in self.cur.fetchall():
            self.tables.append(i[0].strip())

        self.last_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    def work(self):
        new_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        for table in self.tables:
            self.cur.execute("select rdb$field_name from rdb$relation_fields where rdb$relation_name = '" + table + "'")
            columns = []
            for col in self.cur.fetchall():
                columns.append(col[0].strip())
            if 'TIME' in columns:
                self.cur.execute(
                    "select * from " + table + " where 'TIME' between '" +
                    self.last_time +
                    "' and '" +
                    new_time +
                    "'"
                )
                df = pandas.DataFrame(self.cur.fetchall(), columns=columns)
                df.to_csv(table.lower() + '_' + self.last_time.replace(':', '_') + '.csv', index=False, encoding='utf-8')
        self.last_time = new_time
