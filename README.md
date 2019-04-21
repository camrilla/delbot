DelBot: Discord Delete Script
==========================

.. image:: https://img.shields.io/pypi/pyversions/discord.py.svg


### Description: 
> A Discord selfbot that mass deletes messages.

#### Features:
 * Quick deletion of messages in a channel
 * Mass delete private messages

### Installation:
##### Download zip or:
``` {.sourceCode .bash}
$ git clone https://github.com/camrilla/delbot.git
```

##### In the project directory:
``` {.sourceCode .bash}
$ python3 pip install -r requirements.txt
```

#### Add your token

##### Watch to learn how to obtain your token. Do not share your token with anyone.
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/tI1lzqzLQCs/0.jpg)](http://www.youtube.com/watch?v=tI1lzqzLQCs)

##### After obtaining your token, please add it it to the delbot/src/conf.py.

### Usage:


##### Run script
``` {.sourceCode .bash}
$ python3 bot.py
```

##### Delete messages in a channel
###### Type in target channel
``` {.sourceCode .bash}
?rm
```
``` {.sourceCode .bash}
?rm 100
```

##### Delete all private messages
###### Type in any channel
``` {.sourceCode .bash}
?rm private
```