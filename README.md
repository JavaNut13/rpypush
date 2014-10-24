## RPy Push

Uses Python, [RPIO](http://pythonhosted.org/RPIO/) and [Pushbullet](http://pushbullet.com) to notify you when inputs happen on your GPIO puns. Hopefully this will eventually become some kind of library/ interface thing and make it easy to use Pushbullet to control electronics with a Raspberry Pi.

You need to install RPIO for this to work:

```
sudo easy_install -U RPIO
```

`CODE` should be your pushbullet access token, from [here](https://www.pushbullet.com/account).