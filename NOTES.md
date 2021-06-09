# Notes

### Create a plugin

To add a plugin to ZeroNet you can create a new folder with the name of your plugin in the `plugins` folder.

example :
```
cd plugins
mkdir Example
touch __init__.py ExamplePlugin.py
```

in `__init__.py` :
```
import ExamplePlugin
```

in `ExamplePlugin.py` :
```
from Plugin import PluginManager

@PluginManager.registerTo("UiWebsocket")
class UiWebsocketPlugin(object):

    # Create a new action that can be called using zeroframe api
    def actionHelloWorld(self, to):
        self.response(to, {'message':'Hello World'})
```

Example of code calling helloWorld action using zeroframe api
```
import ZeroFrame from 'zeroframe'

var zeroframe = new ZeroFrame()

zeroframe.cmd('helloWorld', {}, (response) => {
  console.log(response) // print 'Hello World' message
})
```

## Build libtorrent python bindings


### For Linux (deprecated)

We download boost 1.74 (min required). You will need `gcc`, `git` and `wget` installed.

```
$ make libtorrent
$ export BOOST_BUILD_PATH=${PWD}/boost_1_74_0/tools/build
$ export BOOST_ROOT=${PWD}/boost_1_74_0
$ make build-libtorrent
```

Test:
```
$ make test
```