/usr/local/tango/bin/tango_admin --add-server XiaomiAirPurifier/airpurifier01 XiaomiAirPurifier my/home/airpurifier01

# <exec/inst> - 这似乎代表你要添加的服务器的可执行文件或实例。这可能是可执行文件名称和实例标识符的组合。
# <class> - 这是服务器的类别。它指定了服务器将提供或管理的服务类型。
# <dev list> - 这是服务器将管理或与之关联的设备列表，需要用逗号分隔。

python3 XiaomiAirPurifier.py airpurifier01

sudo /usr/local/tango/bin/tango restart

