1.0

## Инструкция

### Создание установочного файла

установить pyinstaller через cmd (если не установлен)
 - pip install pyinstaller

 создать исполняемый файл (предварительно переместившись в директорию где находиться скрипт (cd путь/к/файлу))
 - pyinstaller --onefile internet_restoration_NEED_SET_admin_rights.py / internet_restoration_NOT_NEED_SET_admin_rights.py

 ### Запуск скрипта

 - internet_restoration_NEED_SET_admin_rights.exe запускается от имени администратора (правой кнопкой мыши -> запуск от имени администратора / либо можно зайти в "свойства" -> "совместимость" -> и поставить галку "Запускать эту программу от имени администратора" -> "Ok" либо "Применить")  
 !!! ЕСЛИ ПЕРЕМЕСТИТЬ ИСПОЛНЯЕМЫЙ ФАЙЛ В ДРУГУЮ ДИРЕКТОРИЮ - НАСТРОЙКИ ЗАПУСКА ОТ АДМИНИСТРАТОРА СЛЕТАЮТ И ИХ НАДО ВЫСТАВЛЯТЬ СНОВА !!!

 - internet_restoration_NOT_NEED_SET_admin_rights.exe запускается просто двойным кликом, либо по нажатию "Enter", без выбора "Запуск от имени администратора", но исполняется от имени Администратора