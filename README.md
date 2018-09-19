# Python-Script

## Http_Check.py
  ---> http_check.py -u example.com

## Icinga Check_Mysql_Query.py

  ### icinga commands 
    object CheckCommand "check_mysql_query" {
    import "plugin-check-command"

    command = [ PluginDir + "/check_mysql_query.py" ]
    arguments = {
      "-H" = "$service.vars.host$"
      "-d" = "$service.vars.db$"
      "-u" = "$service.vars.user$"
      "-p" = "$service.vars.passwd$"
      "-q" = "$service.vars.query$"

      }
    }
  ### İcinga Service 
    object Service "Kocnet Proccess Control" {
    import "generic-service"
    host_name = "Hostname"
    check_command = "check_mysql_query"
    vars.host = "xxx.xxx.xxx.xxx"
    vars.db = "db name"
    vars.user = "username"
    vars.passwd = "password"
    vars.query = "select COUNT(1) AS xxxxxx"
    max_check_attempts = 10
    check_interval = 30s
    retry_interval = 60s
    }
  ### Test icinga 
    ---> /usr/lib64/nagios/plugins/check_mysql_query.py -H xx.xx.xx.xx -d dbname -u username -p Password -q "select * from user"
