import pandas
from fdb import connect, fbcore
from Parser import parse
# 308898, 308901

args = parse()

# connection to database
try:
    con = connect(
        args.database,
        user=args.user,
        password=args.password,
        charset='UTF8'
    )
except fbcore.DatabaseError:
    print('Invalid credentials, cannot connect to the database')
    con = None

if con:
    cur = con.cursor()
    cur.execute('select "VALUE", "TIME" from MASDATARAW where ITEMID = ' + args.itemid)
    df = pandas.DataFrame(cur.fetchall(), columns=['VALUE', 'TIME'])
    cur.execute('select "NAME" from MASDATAITEMS where ITEMID = ' + args.itemid)
    name = cur.fetchall()[0][0]
    result = ''
    result += 'Item name: ' + name + '\n'
    df.sort_values('TIME')

    # summary statistics
    result += 'Values vary from ' + str(df['VALUE'].min()) + ' to ' + str(df['VALUE'].max()) + '\n'
    result += 'Mean: ' + str(df['VALUE'].mean()) + '\n'
    result += 'Median: ' + str(df['VALUE'].median()) + '\n'
    result += 'Standard Deviation: ' + str(df['VALUE'].std()) + '\n'
    with open(args.output + '/stat_' + args.itemid + '.txt', 'w') as file:
        file.write(result)

    # figures
    plt = df.boxplot()
    plt.set_title(name)
    plt.get_figure().savefig(args.output + '/fig_boxplot_' + args.itemid + '.pdf')

    plt = df.plot.line(x='TIME', y='VALUE')
    plt.set_ylabel('Value')
    plt.set_xlabel('Time')
    plt.set_title(name)
    plt.get_figure().savefig(args.output + '/fig_line_' + args.itemid + '.pdf')
