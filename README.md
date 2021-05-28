# Простой шаблон Qt (Pyside2) приложения организующий структуру файлов придерживаясь архитектуры MVC

Данный шаблон создается с целью демонстрации и быстрого использования для будущих небольших проектов в виде шаблона.

Несмотря на то, что в Qt представлена концепция [Model/View Programming](https://doc-snapshots.qt.io/qtforpython-5.15/overviews/model-view-programming.html), данный пример реализует отличающийся архитектурный дизайн, а именно [MVС](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller). 

## Структура папок

```commandline
>
│   run.py #  
│           
├───config/ # Содержит глобальные настройки приложения.
├───main/ # Основная дирректория с файлами прилоения.
│   │   __init__.py
│   │   
│   ├───controllers/ # Содержит контроллеры приложения.
│   │       main_control.py
│   │       __init__.py
│   │           
│   ├───models/ # Содержит модели приложения.
│   │       main_model.py
│   │       __init__.py
│   │           
│   ├───resources/ # Содержит "скомпилированные" и не только ресурсы приложения.
│   │   │   file_rc.py
│   │   │   file_rc.qrc
│   │   │   __init__.py
│   │   │   
│   │   ├───css/
│   │   ├───img/
│   │   ├───languages/
│   │   └───qt_designs
│   │           ui_main.ui
│   │           
│   └───views/  # Содержит представления приложения
│           main_view.py
│           ui_main.py
│           __init__.py
│           
├───services/ # Содержит все необходимые для приложения элементы.
│   │   __init__.py
│   │   
│   ├───storages/ # Содержит реализацию хранилищ данных используемых приложением.
│   │       __init__.py
│   │       
│   ├───widgets/ # Содержит автономные элементы пользовательского интерфейса.
│   │       __init__.py
│   │       
│   └───workers/ # Содержит реализацию обработчиков для выполнения длительных и/или блокирующих задач.
│           __init__.py
│           
├───static/ # Содержит статические файлы которые используются в приложении.
│   │   README.md
│   │   
│   ├───docs/
│   ├───icons/
│   └───imgs/
└───tools/
        __init__.py
```

## Main

### Controllers (Контролеры) 

Каждый контроллер реализован как отдельный класс, который содержит бизнес-логику приложения.

Контроллер выполняет логику, а затем устанавливает данные в модели.

### Models (Модели)

Каждая модель реализуется как отдельный класс, который содержит данные и состояние программы.

Модель может содержать только логику связанную с инициализацией или изменением данных.

### Views (Представления)

Каждое представление реализованно как отдельный класс, который содержит минимум код подключения к сигналам.

Представление не должно содержать бизнес-логику приложения.
Все что делает представление — устанавливает связь между событиями элементов окна и функцией описанной в контроллере.
А также, прослушивает какие были выполнены изменения в модели (через сигналы).

## Services

Содержит все необходимые для приложения элементы.
Каждый элемент является автономным и доступен для основного приложения описанного в main.
Сервисы должны реализовываться так, чтобы делать возможным их повторное использование.

### Storages

Содержит элементы приложения реализующие хранилище данных используемых приложением.

Как правило, данные хранилища не имеют своего представления и хранят специфическую информацию
востребованную многими представлениями, но не относящуюся к состоянию данных приложений.
Хранилища могут быть реализованны как пара Controller-Model, которы обеспечивают доступ к данным
и поддерживают консистентность этих данных. Хранилища данных могут обеспечивать блокировку работы с данными
и информировать об их доступности в настоящий момент времени.

Однако, является возможным, если для конкретного хранилища может быть реализован свое собственное представление.
Ключевая суть хранилищ заключается в предоставлении доступа к одним и тем же данным для разных
наблюдателей (представлений) что бы они смогли отобразить их в различных контекстах и/или с различных точек зрения.

### Widget

Содержит автономные элементы пользовательского интерфейса.

Каждый виджет реализуется через концепцию MVC, где в модели хранится только та информация,
которая характеризует данный виджет. В контроллере виджета реализуется логика необходимая
для управления виджета и связи виджета и модели.

### Workers

Содержит все необходимые для приложения элементы.
Каждый элемент является автономным и доступен для основного приложения описанного в main.
Сервисы должны реализовываться так, чтобы делать возможным их повторное использование.
