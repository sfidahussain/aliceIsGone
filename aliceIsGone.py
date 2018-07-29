import sqlite3

con = sqlite3.connect('pcfb.sqlite')

## Creating the tables
##con.execute("create table people (id integer primary key, name varchar, position varchar, phone varchar, office varchar);")
##con.execute("create table experiment ( id integer primary key, name varchar, researcher integer, description text, foreign key(researcher) references people(id))")

con.execute('insert into people values (0, \'Alice\', \'Research Director\', 555-123-0001, \'4b\')')
con.execute('insert into people values (1, \'Bob\', \'Research assistant\', 555-123-0002, \'17\')')
con.execute('insert into people values (2, \'Charles\', \'Research assistant\', 555-123-0001, \'24\')')
con.execute('insert into people values (3, \'David\', \'Research assistant\', 555-123-0001, \'8\')')
con.execute('insert into people values (4, \'Edwards\', \'Toadie\', \'None\', \'Basement\')')

con.execute('insert into experiment values (0, \'EBV Vaccine trial\', 0, \'A vaccine trial\')')
con.execute('insert into experiment values (1, \'Flu antibody study\', 2, \'Study of the morphology of flu antibodies\')')

r = con.execute('select * from people')

for i in r:
    print(i)

r = con.execute('select p.name, e.name from people as p join experiment as e where e.researcher == p.id')

for i in r:
    print('Name: %s\n\tExperiment: %s' % (i[0],i[1]))

## Write a script to add a new user and experiment to the database;
## To add a new user:
con.execute('insert into people values (5, \'New User\', \'New User\', \'New User\', \'New User\')')

## To add a new experiment:
con.execute('insert into experiment values (2, \'New Experiment\', 2, \'New Experiment\')')

## Reassign her experiments to the new user
## Take the experiments that were Alices and set it to a new user
con.execute('UPDATE experiment SET researcher = 5 WHERE id = 2;')

## Remove Alice
con.execute('delete from people where name=\'Alice\'');
print('After deleting Alice')

r = con.execute('select * from people')

for i in r:
    print(i)

## Print out all of the experiment names with who owns each experiment.
r = con.execute('select p.name, e.name from people as p join experiment as e where e.researcher == p.id')

print('Printing out experiments after deleting Alice: ')
for i in r:
    print('Name: %s\n\tExperiment: %s' % (i[0],i[1]))