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

## Install libtorrent


### For Linux

Be sure to have libboost-all-dev installed.

```
cd libtorrent
git checkout RC_1_1_
./bootstrap.sh
./configure --enable-python-binding
make install
```

Test :
```
python
>> import libtorrent
``` 
