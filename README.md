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

