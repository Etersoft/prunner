prunner - 'Process Runner'
--------------------------

Это простая утилита на питон, реализует запуск и завершение указанных процессов в зависимости от состояния главного процесса.
Ей указывается процесс за которым необходимо следить (pid) и какие программы запустить,
как только главный процесс завершается, все запущенные программы останавливаются.

Depends
-------
- psutil (python module)

Usage
-----
    prunner -p pid [-d dir | -f file | -r '[params]prog args..']

Help
----
    -d | --run-from-dir dir                - run programm from directory
    -f | --run-from-file file              - run programm from file
    -r | --run '[params]prog args..'       - run programm from command line"
    -p | --monitor-pid pid                 - pid of main process (for monitoring)
    -v | --verbose                         - Print info messages
    -V | --version                         - Version info
    --disable-monitor                      - only run process
    -c | --check-period sec                - period for check processes. Default: 5 sec
    -t | --terminate-timeout sec           - timeout for teminate processes (then the processes will be killed). Default: 5 sec

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
    
    [restart] prog1 arg1 arg2
    # comment 1
    [ignore_fail,restart] prog2 arg1 arg2
    # comment 2
    [verbose,shell=False] prog3
    prog4 arg1 arg2
    prog5 arg1

    
    prunner -p PID -f ./runlist.txt

В данном случае, если процесс PID существуют, будут запущены программы указанные в файле 'runlist.txt'.
а как только процесс PID завершится, запущенные программы будут остановлены.

Формат файла
-------------
- каждая команда располагается на новой строке
- строки начинающиеся с '#' считаются коментариями и игнорируются
- Формат строки: [param1=val1,param2,param3=val3] command args..

Параметры [...] не являются обязательными.
Если у параметра не указан 'val', считается, что значение 'True'.

В квадратных скобках можно указать следующие флаги (для запускаемых программ):
- restart[=val]      - Перезапустить процесс в случае вылета. Если указан val, то он задаёт количество разрешённых перезапусков, после которого prunner завершит работу с ошибкой. По умолчанию процессы не перезапускаются.
- restart_pause=sec  - Пауза между попытками перезапуска, сек. По умолчанию: 5 сек (не может быть меньше --check-period)
- verbose            - выводить stdout,stderr на экран. По умолчанию False
- shell=0            - Запуска без shell. По умолчанию: shell=True


Пояснения к 'restart'
- **"restart = -1"** - Не перезапускать процесс в случае вылета или неудачного пуска. По сути это 'запустить один раз'. Это действие по умолчанию.
- **"restart = 0"**  - Постоянно перезапускать. Можно также просто указать [restart]
- **"restart > 0"**  - задаёт количество разрешённых перезапусков, после которого считается prunner вылетит с ошибкой


Example 3 (run from command line)
---------------------------------
    prunner -p PID -r '[restart] prog1 arg1 arg2' -r '[restart=0,verbose] prog2 arg1 arg2' --run '[shell=0,ignore_fail=0] prog3 arg1 arg2'


Example 4 
---------
    prunner -p PID -d ./child.d -f runlist.txt -r '[restart=2] prog1 arg1 arg2'
Т.е. можно указывать и каталог и файл и -r одновременно
