prunner - 'Process Runner'
--------------------------

Это простая утилита на питон, реализует запуск и завершение указанных процессов в зависимости от состояния главного процесса.
Ей указывается процесс за которым необходимо следить (pid) и какие программы запустить,
как только главный процесс завершается, все запущенные программы останавливаются.

Depends
-------
- psutil

Usage
-----
    prunner -p main_pid [-d dir | -f file]

Help
----
    -d | --run-from-dir dir       - run programm from directory
    -f | --run-from-file file     - run programm from file
    -p | --monitor-pid pid        - pid of main process (for monitoring)
    -v | --verbose                - Print info messages
    --disable-monitor             - only run process
    -c | --check-period sec       - period for check processes. Default: 5 sec
    -t | --terminate-timeout sec  - timeout for teminate processes (then the processes will be killed). Default: 5 sec

Example 1 (run from directory)
------------------------------

    child.d/
        prog1
        prog2
        prog3
    
    prunner -p PID -d ./child.d

Если процесс PID существуют, будут запущены программы из каталога child.d,
а как только процесс PID завершится, запущенные программы будут остановлены.

Example 2 (run from file)
-------------------------
    cat runlist.txt
    
    [restart] prog1
    # comment 1
    [ignore_fail,restart] prog2
    # comment 2
    [verbose,shell=False] prog3
    prog4
    prog5

    
    prunner -p PID -f ./runlist.txt

В данном случае, если процесс PID существуют, будут запущены программы указанные в файле 'runlist.txt'.
а как только процесс PID завершится, запущенные программы будут остановлены.

Формат файла
-------------
- каждая команда располагается на новой строке
- строки начинающиеся с '#' считаются коментариями и игнорируются
- Формат строки: [param1=val1,param2,param3=val3] command

Параметры [...] не являются обязательными.
Если у параметра не указан 'val', считается, что значение 'True'.

В квадратных скобках можно указать следующие флаги (для запускаемых программ):
- restart     - перезапустить процесс в случае вылета. По умолчанию: False
- verbose     - выводить stdout,stderr на экране. По умолчанию False
- ignore_fail - игнорировать вылет или завершение процесса. По умолчанию True
- shell=False - Запуска без shell. По умолчанию: shell=True

<code>
"restart=0,ignore_fail=1" - игнорировать завершение или отказ запуска и не перезапускать
"restart=1,ignore_fail=0" - попытаться перезапустить процесс и если не удалось, завершить работу программы
"restart=0,ignore_fail=0" - завершить работу программы если процесс не запустился или завершился во время работы
"restart=1,ignore_fail=1" - игнорировать неудачные запуски, но пытаться снова перезапускать
</code>

Example 3 
---------
    prunner -p PID -d ./child.d -f runlist
Т.е. можно указывать и каталог и файл одновременно
