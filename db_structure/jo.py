import sys
import db_utilities


def insert_row(row):
    Table = db_utilities.ConnectToCardsTable('/Users/leo/Desktop/db/', 'cardnallsins.db')
    Table.connect()
    #Table.drop_table()
    Table.insert_row(row)
    Table.commit()
    Table.close()
    return


def main():
    row = (None, '2014-05-05')
    insert_row(row)


if __name__ == "__main__":
    main()