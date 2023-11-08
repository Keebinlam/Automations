# install Camelot
# install TK
# install ghostscript
import camelot
#lattice does now work for me
tables = camelot.read_pdf('foo.pdf',
                          pages='1', flavor='stream')
print(tables)

tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')  # to a csv file
print(tables[0].df)  # to a df
