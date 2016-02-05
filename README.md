## Firebase storage plugin for errbot


### About
[Errbot](http://errbot.io) is a python chatbot, this storage plugin allows you to use it with
[Google Firebase](http://firebase.com) as a persistent storage.

### Installation


1. Go to [Google Firebase](http://firebase.com) and create an account, developers account are free.
2. First you need to clone this repository somewhere, for example:
 ```bash
 mkdir /home/gbin/err-storage
 cd /home/gbin/err-storage
 git clone https://github.com/errbotio/err-storage-firebase
 ```

3. Then you need to add this section to your config.py, following the previous example:
 ```python
 BOT_EXTRA_STORAGE_PLUGINS_DIR='/home/gbin/err-storage'
 STORAGE = 'Firebase'
 STORAGE_CONFIG = {
    'data_url': 'https://radiant-bear-6933.firebaseio.com/',
    'secret': '6F51OL7rAOBCcq2sU36cAHh0z01Vneq29LpQkx58',
    'email': 'gbin@gootz.net'}
 ```
 You can find your secret from your project page (which is the same as the data_url) and click on the bottom left on "secrets".
 You can either use the one there or create a new one.
 
 Start your bot in text mode: `errbot -T` to give it a shot.
 
 If you want to migrate from the local storage to firebase, you should be able to backup your data (with STORAGE commented)
 then restore it back with STORAGE uncommented.