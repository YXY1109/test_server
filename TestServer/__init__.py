from TestServer.base.common import isMyWindows

# https://www.xinzipanghuang.net/1415-2/


if not isMyWindows():
    import pymysql

    pymysql.version_info = (1, 4, 13, "final", 0)
    pymysql.install_as_MySQLdb()
