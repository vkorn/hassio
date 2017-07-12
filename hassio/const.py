"""Const file for HassIO."""
from pathlib import Path

HASSIO_VERSION = '0.43'

URL_HASSIO_VERSION = ('https://raw.githubusercontent.com/home-assistant/'
                      'hassio/master/version.json')
URL_HASSIO_VERSION_BETA = ('https://raw.githubusercontent.com/home-assistant/'
                           'hassio/dev/version.json')

URL_HASSIO_ADDONS = 'https://github.com/home-assistant/hassio-addons'

HASSIO_DATA = Path("/data")

HASSIO_PUBLIC_CLUSTER_PORT = 9123
HASSIO_API_PORT = 80

RUN_UPDATE_INFO_TASKS = 28800
RUN_UPDATE_SUPERVISOR_TASKS = 29100
RUN_UPDATE_ADDONS_TASKS = 57600
RUN_RELOAD_ADDONS_TASKS = 28800
RUN_RELOAD_SNAPSHOTS_TASKS = 72000
RUN_WATCHDOG_HOMEASSISTANT = 15
RUN_CLEANUP_API_SESSIONS = 900
RUN_REGENERATE_CLUSTER_KEY = 300
RUN_PING_CLUSTER_MASTER = 60

RESTART_EXIT_CODE = 100

FILE_HASSIO_ADDONS = Path(HASSIO_DATA, "addons.json")
FILE_HASSIO_CONFIG = Path(HASSIO_DATA, "config.json")
FILE_HASSIO_HOMEASSISTANT = Path(HASSIO_DATA, "homeassistant.json")

SOCKET_DOCKER = Path("/var/run/docker.sock")
SOCKET_HC = Path("/var/run/hassio-hc.sock")

LABEL_VERSION = 'io.hass.version'
LABEL_ARCH = 'io.hass.arch'
LABEL_TYPE = 'io.hass.type'

META_ADDON = 'addon'
META_SUPERVISOR = 'supervisor'
META_HOMEASSISTANT = 'homeassistant'

JSON_RESULT = 'result'
JSON_DATA = 'data'
JSON_MESSAGE = 'message'

RESULT_ERROR = 'error'
RESULT_OK = 'ok'

ATTR_DATE = 'date'
ATTR_ARCH = 'arch'
ATTR_HOSTNAME = 'hostname'
ATTR_TIMEZONE = 'timezone'
ATTR_OS = 'os'
ATTR_TYPE = 'type'
ATTR_SOURCE = 'source'
ATTR_FEATURES = 'features'
ATTR_ADDONS = 'addons'
ATTR_VERSION = 'version'
ATTR_LAST_VERSION = 'last_version'
ATTR_BETA_CHANNEL = 'beta_channel'
ATTR_NAME = 'name'
ATTR_SLUG = 'slug'
ATTR_DESCRIPTON = 'description'
ATTR_STARTUP = 'startup'
ATTR_BOOT = 'boot'
ATTR_PORTS = 'ports'
ATTR_MAP = 'map'
ATTR_OPTIONS = 'options'
ATTR_INSTALLED = 'installed'
ATTR_DETACHED = 'detached'
ATTR_STATE = 'state'
ATTR_SCHEMA = 'schema'
ATTR_IMAGE = 'image'
ATTR_ADDONS_REPOSITORIES = 'addons_repositories'
ATTR_REPOSITORY = 'repository'
ATTR_REPOSITORIES = 'repositories'
ATTR_URL = 'url'
ATTR_MAINTAINER = 'maintainer'
ATTR_PASSWORD = 'password'
ATTR_TOTP = 'totp'
ATTR_INITIALIZE = 'initialize'
ATTR_SESSION = 'session'
ATTR_LOCATON = 'location'
ATTR_BUILD = 'build'
ATTR_DEVICES = 'devices'
ATTR_ENVIRONMENT = 'environment'
ATTR_HOST_NETWORK = 'host_network'
ATTR_NETWORK = 'network'
ATTR_TMPFS = 'tmpfs'
ATTR_PRIVILEGED = 'privileged'
ATTR_USER = 'user'
ATTR_SYSTEM = 'system'
ATTR_SNAPSHOTS = 'snapshots'
ATTR_HOMEASSISTANT = 'homeassistant'
ATTR_FOLDERS = 'folders'
ATTR_SIZE = 'size'
ATTR_TIMEOUT = 'timeout'
ATTR_AUTO_UPDATE = 'auto_update'
ATTR_CUSTOM = 'custom'
ATTR_IS_MASTER = 'is_master'
ATTR_MASTER_KEY = 'master_key'
ATTR_NODE_KEY = 'node_key'
ATTR_NODE_NAME = 'node_name'
ATTR_MASTER_IP = 'master_ip'
ATR_KNOWN_NODES = 'nodes'
ATTR_IP = 'ip'
ATTR_IS_ACTIVE = 'is_active'
ATTR_LAST_SEEN = 'last_seen'
ATTR_CLUSTER_WRAP = 'wrap'

STARTUP_INITIALIZE = 'initialize'
STARTUP_BEFORE = 'before'
STARTUP_AFTER = 'after'
STARTUP_ONCE = 'once'

BOOT_AUTO = 'auto'
BOOT_MANUAL = 'manual'

STATE_STARTED = 'started'
STATE_STOPPED = 'stopped'
STATE_NONE = 'none'

MAP_CONFIG = 'config'
MAP_SSL = 'ssl'
MAP_ADDONS = 'addons'
MAP_BACKUP = 'backup'
MAP_SHARE = 'share'

ARCH_ARMHF = 'armhf'
ARCH_AARCH64 = 'aarch64'
ARCH_AMD64 = 'amd64'
ARCH_I386 = 'i386'

REPOSITORY_CORE = 'core'
REPOSITORY_LOCAL = 'local'

FOLDER_HOMEASSISTANT = 'homeassistant'
FOLDER_SHARE = 'share'
FOLDER_ADDONS = 'addons/local'
FOLDER_SSL = 'ssl'

SNAPSHOT_FULL = 'full'
SNAPSHOT_PARTIAL = 'partial'

HTTP_HEADER_X_FORWARDED_FOR = 'X-Forwarded-For'
HTTP_HEADER_X_NODE_KEY = 'X-Node-Key'

CLUSTER_NODE_MASTER = 'master'
