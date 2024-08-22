my_dict={'Дмитрий':1981 , 'Иван':1986 , 'Павел':1988 , 'Катя':2005}
print(my_dict)
print(my_dict['Иван'])
my_dict['Александра']=2016
print(my_dict)
print(my_dict['Александра'])
my_dict.update(({'Борис':1962 , 'Татьяна':1962}))
print(my_dict)
a = my_dict.pop('Павел')
print(my_dict)
print(a)
print(my_dict)
my_set={5,53,903,53,5,903 ,'Lada','Niva' ,'Niva' ,'Lada'}
print(my_set)
my_set.discard(903)
print(my_set)

