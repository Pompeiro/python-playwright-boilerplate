## Poetry

In case of setting up local poetry env sure to point to correct python3.11 path
~~~
poetry env use /home/maciej/.pyenv/shims/python3.11
~~~

## Environment Variables

~~~
$ cp env.template .env
~~~

## Build

To build:
~~~
$ make build
~~~

## Tests

To run in headed mode open connection with container display:
~~~
$ xhost +
~~~
If still you got the display error like:
~~~
║ Looks like you launched a headed browser without having a XServer running.                     ║
║ Set either 'headless: true' or use 'xvfb-run <your-playwright-app>' before running Playwright. ║
║                                                                                                ║
║ :heart: Playwright Team
3:22
[pid=82][err] [82:95:0411/131323.746464:ERROR:bus.cc(399)] Failed to connect to the bus: Failed to connect to socket /run/dbus/system_bus_socket: No such file or directory
[pid=82][err] [82:82:0411/131323.794324:ERROR:ozone_platform_x11.cc(239)] Missing X server or $DISPLAY
[pid=82][err] [82:82:0411/131323.794358:ERROR:env.cc(255)] The platform failed to initialize.  Exiting.
~~~
or
~~~
E       =========================== logs ===========================
E       <launching> /root/.cache/ms-playwright/firefox-1403/firefox/firefox -no-remote -wait-for-browser -foreground -profile /tmp/playwright_firefoxdev_profile-4mkDa7 -juggler-pipe -silent
E       <launched> pid=190
E       [pid=190][err] Authorization required, but no authorization protocol specified
E       [pid=190][err] Error: cannot open display: :0
E       [pid=190] <process did exit: exitCode=1, signal=null>
E       [pid=190] starting temporary directories cleanup
E       ============================================================
~~~
Then run:
~~~
ls /tmp/.X11-unix
~~~
The message will be like:
~~~
X1  X99
~~~
And then copy .env file and change the DISPLAY variable from:
```console
$ cp env.template .env
```
~~~
DISPLAY=0
~~~
to:
~~~
DISPLAY=1
~~~

To run tests:
~~~
$ make test
~~~
To run specific test in debug mode:
~~~
$ SPEC=test_normal_user_can_navigate_with_reports_icon make test-spec
~~~
To run tests in headed mode with slowmo 800ms:
~~~
$ make test-headed
~~~

## Local development
In case [Errno 13] Permission denied: 'src/tests/conftest.py' and so on:
~~~
sudo chown -R $(whoami) .
~~~

## Allure
New UI
~~~
http://localhost:5252/allure-docker-service-ui/
~~~
Backend
~~~
http://localhost:5050/allure-docker-service/
~~~
