usage: uroot [-h] [-d DIFFDIR] [-t TMPDIR] [-f] [cmd_arg [cmd_arg ...]]

Simple sandboxing without superuser privileges.

Иногда хочется установить какой-нибудь пакетик для временного пользования,
а прав не хватает. Утилита uroot позволяет справиться с такой напастью,
создавая песочницу с помощью unionfs поверх корневой файловой системы.

Вот пример использования:

    user@host:~$ uroot
    user@host:/$ fakeroot apt-get install -y ruby
    ....
    Setting up ruby (1:1.9.3) ...
    user@host:/$ ruby -e 'print "Hello World!\n"'
    Hello World! 
    user@host:/$ exit
    exit
    user@host:~$ ruby -e 'print "Goodbye World!\n"'
    bash: ruby: command not found

Если не используется опция -d, то для хранения изменений создается
временная директория. Можно переопределить место где она будет создаваться
с помощью опции -t.

positional arguments:
  cmd_arg

optional arguments:
  -h, --help            show this help message and exit
  -d DIFFDIR, --diffdir DIFFDIR
                        Create named diff-directory, if this option is given
                        then diff-directory is not removed upon program
                        completion. Otherwise diff-directory will be
                        considered temporary and will be removed eventually.
                        You can choose where to create temporary diff-dirs
                        with -t option.
  -t TMPDIR, --tmpdir TMPDIR
  -f, --force-unmount   После завершения процесса
                        uroot, файловая система unionfs
                        будет отмонтирована лениво
                        (см. man umount), но если указана
                        опция -f, то отмонтирование
                        будет принудительным, а если
                        понадобится, то и с убийством
                        всех оппозиционно
                        настроенных процессов.

