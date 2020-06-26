### 1.1. Исследовать функционал одного модуля не из стандартной библиотеки (например, requests) и создать фрагмент ЭОР с описанием и примерами его использования при работе в Jupyter Notebook (Typora, встроенный редактор Markdown сервиса GitHub) и в скриптовом виде. Для выполнения задания использовать Jupyter Notebook (Typora, встроенный редактор Markdown сервиса GitHub), опубликовать результат выполнения задания в портфолио в HTML и PDF формате. 

# vk_api

vk_api – Python модуль для создания скриптов для социальной сети Вконтакте (vk.com API wrapper)

```
import vk_api

vk_session = vk_api.VkApi('+71234567890', 'mypassword')
vk_session.auth()

vk = vk_session.get_api()

print(vk.wall.post(message='Hello world!'))
```

Установка
```
$ pip install vk_api
```

VkApi (основной класс)
class vk_api.vk_api.VkApi(login=None, password=None, token=None, auth_handler=None, captcha_handler=None, config=<class 'jconfig.jconfig.Config'>, config_filename='vk_config.v2.json', api_version='5.92', app_id=6222115, scope=140492255, client_secret=None, session=None)[source]
Parameters:	
* login (str) – Логин ВКонтакте (лучше использовать номер телефона для автоматического обхода проверки безопасности)
* password (str) – Пароль ВКонтакте (если пароль не передан, то будет попытка использовать сохраненные данные)
* token (str) – access_token
* auth_handler – Функция для обработки двухфакторной аутентификации, должна возвращать строку с кодом и булево значение, означающее, стоит ли запомнить это устройство, для прохождения аутентификации.
* captcha_handler – Функция для обработки капчи, см. captcha_handler()
* config (jconfig.base.BaseConfig) – Класс для сохранения настроек
* config_filename – Расположение config файла для jconfig.config.Config
* api_version (str) – Версия API
* app_id (int) – app_id Standalone-приложения
* scope (int or str) – Запрашиваемые права, можно передать строкой или числом. См. VkUserPermissions
* client_secret – Защищенный ключ приложения для Client Credentials Flow авторизации приложения (https://vk.com/dev/client_cred_flow). Внимание: Этот способ авторизации устарел, рекомендуется использовать сервисный ключ из настроек приложения.
* login и password необходимы для автоматического получения токена при помощи Implicit Flow авторизации пользователя и возможности работы с веб-версией сайта (включая vk_api.audio.VkAudio)

Parameters:	
* session (requests.Session) – Кастомная сессия со своими параметрами(из библиотеки requests)

auth(reauth=False, token_only=False)[source]
Аутентификация

Parameters:	
* reauth – Позволяет переавторизоваться, игнорируя сохраненные куки и токен
* token_only –
Включает оптимальную стратегию аутентификации, если необходим только access_token

Например если сохраненные куки не валидны, но токен валиден, то аутентификация пройдет успешно

При token_only=False, сначала проверяется валидность куки. Если кука не будет валидна, то будет произведена попытка аутетификации с паролем. Тогда если пароль не верен или пароль не передан, то аутентификация закончится с ошибкой.

Если вы не делаете запросы к веб версии сайта используя куки, то лучше использовать token_only=True

check_sid()[source]
Проверка Cookies remixsid на валидность

server_auth()[source]
Серверная авторизация

code_auth(code, redirect_url)[source]
Получение access_token из code

captcha_handler(captcha)[source]
Обработчик капчи (http://vk.com/dev/captcha_error)

Parameters:	captcha – объект исключения Captcha
need_validation_handler(error)[source]
Обработчик проверки безопасности при запросе API
(http://vk.com/dev/need_validation)
Parameters:	error – исключение
http_handler(error)[source]
Обработчик ошибок соединения

Parameters:	error – исключение
too_many_rps_handler(error)[source]
Обработчик ошибки “Слишком много запросов в секунду”.
Ждет полсекунды и пробует отправить запрос заново
Parameters:	error – исключение
auth_handler()[source]
Обработчик двухфакторной аутентификации

get_api()[source]
Возвращает VkApiMethod(self)

Позволяет обращаться к методам API как к обычным классам. Например vk.wall.get(…)

method(method, values=None, captcha_sid=None, captcha_key=None, raw=False)[source]
Вызов метода API

Parameters:	
method (str) – название метода
values (dict) – параметры
captcha_sid – id капчи
captcha_key (str) – ответ капчи
raw (bool) – при False возвращает response[‘response’] при True возвращает response (может понадобиться для метода execute для получения execute_errors)
class vk_api.vk_api.VkUserPermissions[source]
Bases: enum.IntEnum

Перечисление прав пользователя. Список прав получается побитовым сложением (x | y) каждого права. Подробнее в документации VK API: https://vk.com/dev/permissions

NOTIFY = 1
Пользователь разрешил отправлять ему уведомления (для flash/iframe-приложений). Не работает с этой библиотекой.

FRIEND = 2
Доступ к друзьям.

PHOTOS = 4
Доступ к фотографиям.

AUDIO = 8
Доступ к аудиозаписям. При отсутствии доступа к закрытому API аудиозаписей это право позволяет только загрузку аудио.

VIDEO = 16
Доступ к видеозаписям.

STORIES = 64
Доступ к историям.

PAGES = 128
Доступ к wiki-страницам.

ADD_LINK = 256
Добавление ссылки на приложение в меню слева.

STATUS = 1024
Доступ к статусу пользователя.

NOTES = 2048
Доступ к заметкам пользователя.

MESSAGES = 4096
Доступ к расширенным методам работы с сообщениями.

WALL = 8192
Доступ к обычным и расширенным методам работы со стеной.

ADS = 32768
Доступ к расширенным методам работы с рекламным API.

OFFLINE = 65536
Доступ к API в любое время. Рекомендуется при работе с этой библиотекой.

DOCS = 131072
Доступ к документам.

GROUPS = 262144
Доступ к группам пользователя.

NOTIFICATIONS = 524288
Доступ к оповещениям об ответах пользователю.

STATS = 1048576
Доступ к статистике групп и приложений пользователя, администратором которых он является.

EMAIL = 4194304
Доступ к email пользователя.

MARKET = 134217728
Доступ к товарам.
