# Запуск приложения:
## 0. Установите пакетный менеджер conda:
https://conda.io/projects/conda/en/latest/user-guide/install/index.html

## 1. Установите пакеты из requirements.txt
```
conda install --file requirements.txt
```

**!NOTE:** 
В проекте используется conda, но модуля vk в этом пакетном менеджере нет, поэтому его нужно будет установить через pip:
```
pip install vk
```

## 2. Запустите main.py

**!NOTE:** 
Для корректного запуска нужно запустить сервер Postgresql. Для корректной работы необходим только запуск, никаких других действий выполнять не нужно.

**!NOTE:** id поста вводится в формате: 
-число_число

Примеры id поста:
-111873189_3426, -97919489_28390, -141052304_844
