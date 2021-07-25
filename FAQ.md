
## FAQ

### How to install it
You will need to install it via this site [/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL](/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL). Once it is installed you will be asked to restart ZeroNet and then refresh the site.

### How to use it
You will be presented with a form to add a torrent via either a magnet link or a .torrent file. To properly test if the plugin is working please click on the `sintel` link which will fill the form with the Sintel movie magnet and then submit.

You will need to wait a bit for it to connect to peers and start downloading the film. It will then show the video  player and you can start to watch Sintel as it is being downloaded.

### How to stop it
Once you have stopped ZeroNet or disabled the plugin (using [/Plugins](/Plugins)) the torrent will not be shared anymore.

### Where is the file saved
The file will be saved in your `data` folder under the folder of the site that it has been requested from (so here `1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL`) under a `downloads` folder (e.g `data/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/downloads`).

This should be accessible in ZeroNet via this link [http://127.0.0.1:43110/list/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/list/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL](http://127.0.0.1:43110/list/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/list/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/). You can look for the `downloads` folder if you have added torrent file via the `1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL` site and want to access it.

### How can I hide my identity
Use a no-logging VPN.

### Where can it be used
It can only be used in site that supports and have implemented the specific api of the plugin. Documentation will be available soon. Devs can also take a look at this file for the available actions implemented by the plugin (https://github.com/rllola/zeronet-torrent-plugin-example/blob/master/app/stores/Site.js)
