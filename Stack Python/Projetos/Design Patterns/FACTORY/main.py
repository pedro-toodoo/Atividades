from factory import MysqlFactory

usecase = MysqlFactory.create()
response = usecase.do_something(True)

print(response)

